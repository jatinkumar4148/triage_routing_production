
import React, { useEffect, useState } from "react";
import "./App.css";

const HISTORY_KEY = "triage-routing-history";

export default function App() {
  const [text, setText] = useState("");
  const [res, setRes] = useState(null);
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState([]);
  const [showHistory, setShowHistory] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    const stored = window.localStorage.getItem(HISTORY_KEY);
    if (stored) {
      try {
        setHistory(JSON.parse(stored));
      } catch (e) {
        console.warn("Failed to parse history", e);
        window.localStorage.removeItem(HISTORY_KEY);
      }
    }
  }, []);

  const saveHistory = (newHistory) => {
    setHistory(newHistory);
    window.localStorage.setItem(HISTORY_KEY, JSON.stringify(newHistory));
  };

  const submit = async () => {
    if (!text.trim()) {
      setError("Please enter a ticket description.");
      return;
    }
    setLoading(true);
    setError(null);

    try {
      const r = await fetch("/api/triage", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text }),
      });

      if (!r.ok) {
        throw new Error(`Server returned ${r.status}`);
      }

      const d = await r.json();
      const { rag_context, ...cleanResult } = d;
      setRes(cleanResult);

      const entry = {
        id: Date.now(),
        text,
        result: cleanResult,
        createdAt: new Date().toISOString(),
      };
      saveHistory([entry, ...history]);
      setText("");
    } catch (err) {
      console.error(err);
      setError(err.message || "Request failed");
    } finally {
      setLoading(false);
    }
  };

  const clearHistory = () => {
    saveHistory([]);
    setShowHistory(false);
  };

  const removeHistoryEntry = (id) => {
    const updated = history.filter((entry) => entry.id !== id);
    saveHistory(updated);
  };

  const formatDate = (iso) => {
    return new Date(iso).toLocaleString();
  };

  return (
    <div className="app-shell">
      <div className="card hero-card">
        <div className="hero-header">
          <div>
            <p className="eyebrow">AI-powered</p>
            <h1>AI Triage & Routing</h1>
          </div>
        </div>

        <p className="hero-copy">
          Describe an issue and get instant category, priority, and routing guidance. Your actions are saved in history below.
        </p>

        <div className="button-group">
          <button className="primary-button" onClick={submit} disabled={loading}>
            {loading ? "Processing..." : "Submit ticket"}
          </button>
          <button className="secondary-button" onClick={() => setShowHistory(!showHistory)}>
            {showHistory ? "Hide History" : "Show History"}
          </button>
          <button className="ghost-button" onClick={clearHistory} disabled={history.length === 0}>
            Clear History
          </button>
        </div>
      </div>

      <div className="card form-card">
        <textarea
          className="message-input"
          placeholder="Describe your issue..."
          value={text}
          onChange={(e) => setText(e.target.value)}
        />
      </div>

      {error && <div className="alert-banner">{error}</div>}

      {res && (
        <div className="card result-card">
          <div className="card-title">Triage Result</div>
          <pre className="result-block">{JSON.stringify(res, null, 2)}</pre>
        </div>
      )}

      {showHistory && (
        <div className="card history-card">
          <div className="card-title">History</div>
          {history.length === 0 ? (
            <div className="empty-state">No history yet. Submit a ticket to save it.</div>
          ) : (
            <div className="history-list">
              {history.map((entry) => (
                <div key={entry.id} className="history-item">
                  <div className="history-item-header">
                    <div>
                      <div className="history-date">{formatDate(entry.createdAt)}</div>
                      <div className="history-ticket">{entry.text}</div>
                    </div>
                    <button className="delete-button" onClick={() => removeHistoryEntry(entry.id)}>
                      Delete
                    </button>
                  </div>
                  <pre className="history-result">{JSON.stringify(entry.result, null, 2)}</pre>
                </div>
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  );
}
