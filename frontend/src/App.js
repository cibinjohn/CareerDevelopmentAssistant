import React, { useState, useRef, useEffect } from "react";
import "./App.css";

function StructuredMessage({ data }) {
  const [expanded, setExpanded] = useState(false);

  return (
    <div className="structured-message">
      <p className="main-summary">{data.summary}</p>
      <button
        className="details-toggle"
        onClick={() => setExpanded((prev) => !prev)}
      >
        {expanded ? "Hide details" : "Show details"}
      </button>
      {expanded && (
        <div className="details-panel">
          <div className="detail-row">
            <span className="detail-label">Topic</span>
            <span className="detail-value">{data.topic}</span>
          </div>
          <div className="detail-row">
            <span className="detail-label">Sources</span>
            <span className="detail-value">
              {data.sources.length ? data.sources.join(", ") : "None"}
            </span>
          </div>
          <div className="detail-row">
            <span className="detail-label">Tools used</span>
            <span className="detail-value">
              {data.tools_used.length ? data.tools_used.join(", ") : "None"}
            </span>
          </div>

          {data.chunks && data.chunks.length > 0 && (
            <div className="chunks-section">
              <div className="chunks-label">Retrieved Chunks</div>
              {data.chunks.map((chunk, i) => (
                <div key={i} className="chunk-item">
                  <span className="chunk-number">#{i + 1}</span>
                  <span className="chunk-text">{chunk}</span>
                </div>
              ))}
            </div>
          )}

        </div>
      )}
    </div>
  );
}

function MessageBubble({ msg }) {
  if (msg.sender === "user") {
    return (
      <div className="message-row user-row">
        <div className="bubble user-bubble">{msg.text}</div>
      </div>
    );
  }

  return (
    <div className="message-row bot-row">
      <div className="bot-avatar">CA</div>
      <div className="bubble bot-bubble">
        {msg.type === "structured" ? (
          <StructuredMessage data={msg.data} />
        ) : (
          msg.text.split("\n").map((line, i) => (
            <span key={i}>{line}{i < msg.text.split("\n").length - 1 && <br />}</span>
          ))
        )}
      </div>
    </div>
  );
}

function App() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const chatEndRef = useRef(null);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const clearChat = () => setMessages([]);

  const sendMessage = async () => {
    if (!input.trim() || loading) return;

    const userMessage = { sender: "user", text: input };
    setMessages((prev) => [...prev, userMessage]);
    setMessages((prev) => [...prev, { sender: "bot", type: "text", text: "Thinking..." }]);
    setLoading(true);

    const currentInput = input;
    setInput("");

    try {
      const response = await fetch("http://127.0.0.1:8000/chat-stream", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: currentInput }),
      });

      const data = await response.json();
      const res = data.response;

      let botMessage;
      if (res && res.type === "structured") {
        botMessage = { sender: "bot", type: "structured", data: res.data };
      } else if (res && res.type === "text") {
        botMessage = { sender: "bot", type: "text", text: res.data };
      } else {
        botMessage = { sender: "bot", type: "text", text: "No response received." };
      }

      setMessages((prev) => {
        const updated = [...prev];
        updated[updated.length - 1] = botMessage;
        return updated;
      });

    } catch (err) {
      console.error("Fetch error:", err);
      setMessages((prev) => {
        const updated = [...prev];
        updated[updated.length - 1] = {
          sender: "bot",
          type: "text",
          text: "Error: could not get response.",
        };
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <div className="chat-container">

        <div className="chat-header">
          <div className="header-left">
            <div className="header-avatar">CA</div>
            <div className="header-info">
              <span className="header-name">Career Assistant</span>
              <span className="header-status">
                <span className="status-dot"></span>online
              </span>
            </div>
          </div>
          <button className="clear-btn" onClick={clearChat} title="Clear chat">
            Clear
          </button>
        </div>

        <div className="chat-box">
          {messages.length === 0 && (
            <div className="empty-state">
              <div className="empty-avatar">CA</div>
              <p className="empty-title">Career Assistant</p>
              <p className="empty-subtitle">Ask me anything about your IT career, research topics, or calculations.</p>
            </div>
          )}
          {messages.map((msg, index) => (
            <MessageBubble key={index} msg={msg} />
          ))}
          <div ref={chatEndRef} />
        </div>

        <div className="input-area">
          <input
            className="input-field"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask something..."
            onKeyDown={(e) => e.key === "Enter" && sendMessage()}
            disabled={loading}
          />
          <button
            className="send-btn"
            onClick={sendMessage}
            disabled={loading || !input.trim()}
          >
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
              <line x1="22" y1="2" x2="11" y2="13"></line>
              <polygon points="22 2 15 22 11 13 2 9 22 2"></polygon>
            </svg>
          </button>
        </div>

      </div>
    </div>
  );
}

export default App;