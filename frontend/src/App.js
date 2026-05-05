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
        {expanded ? "▲ Hide Details" : "▼ Show Details"}
      </button>
      {expanded && (
        <div className="details-panel">
          <div className="detail-row">
            <span className="detail-label">📌 Topic</span>
            <span className="detail-value">{data.topic}</span>
          </div>
          <div className="detail-row">
            <span className="detail-label">🔗 Sources</span>
            <span className="detail-value">
              {data.sources.length ? data.sources.join(", ") : "None"}
            </span>
          </div>
          <div className="detail-row">
            <span className="detail-label">🛠 Tools Used</span>
            <span className="detail-value">
              {data.tools_used.length ? data.tools_used.join(", ") : "None"}
            </span>
          </div>
        </div>
      )}
    </div>
  );
}

function MessageBubble({ msg }) {
  if (msg.sender === "user") {
    return (
      <div className="message user">
        <span>{msg.text}</span>
      </div>
    );
  }

  if (msg.type === "structured") {
    return (
      <div className="message bot">
        <StructuredMessage data={msg.data} />
      </div>
    );
  }

  return (
    <div className="message bot">
      {msg.text.split("\n").map((line, i) => (
        <div key={i}>{line}</div>
      ))}
    </div>
  );
}

function App() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);
  const chatEndRef = useRef(null);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const clearChat = () => setMessages([]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { sender: "user", text: input };
    setMessages((prev) => [...prev, userMessage]);
    setMessages((prev) => [...prev, { sender: "bot", text: "Thinking..." }]);

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
        return updated;
      });
    }
  };

  return (
    <div className="app">
      <div className="chat-container">

        <div className="chat-header">
          <h2 className="title">Career Assistant</h2>
          <button className="clear-btn" onClick={clearChat} title="Clear chat">
            🗑 Clear
          </button>
        </div>

        <div className="chat-box">
          {messages.map((msg, index) => (
            <MessageBubble key={index} msg={msg} />
          ))}
          <div ref={chatEndRef} />
        </div>

        <div className="input-box">
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            placeholder="Ask about your IT career..."
            onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          />
          <button onClick={sendMessage}>Send</button>
        </div>

      </div>
    </div>
  );
}

export default App;