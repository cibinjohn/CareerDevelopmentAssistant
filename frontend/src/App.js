import React, { useState, useRef, useEffect } from "react";
import "./App.css";

function App() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);
  const chatEndRef = useRef(null);

  // Auto-scroll
  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { sender: "user", text: input };
    setMessages((prev) => [...prev, userMessage]);
    setMessages((prev) => [...prev, { sender: "bot", text: "Thinking..." }]);

    try {
      const response = await fetch("http://127.0.0.1:8000/chat-stream", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: input }),
      });

      const data = await response.json();
      const res = data.response;

      let formatted = "";

      if (res && res.type === "structured") {
        const r = res.data;
        formatted = [
          `📌 Topic: ${r.topic}`,
          `📝 Summary: ${r.summary}`,
          `🔗 Sources: ${r.sources.length ? r.sources.join(", ") : "None"}`,
          `🛠 Tools Used: ${r.tools_used.length ? r.tools_used.join(", ") : "None"}`,
        ].join("\n");
      } else if (res && res.type === "text") {
        formatted = res.data;
      } else {
        formatted = "No response received.";
      }

      setMessages((prev) => {
        const updated = [...prev];
        updated[updated.length - 1] = { sender: "bot", text: formatted };
        return updated;
      });

    } catch (err) {
      console.error("Fetch error:", err);
      setMessages((prev) => {
        const updated = [...prev];
        updated[updated.length - 1] = { sender: "bot", text: "Error: could not get response." };
        return updated;
      });
    }

    setInput("");
  };

  return (
    <div className="app">
      <div className="chat-container">
        <h2 className="title">Career Assistant</h2>

        <div className="chat-box">
          {messages.map((msg, index) => (
            <div
              key={index}
              className={`message ${msg.sender === "user" ? "user" : "bot"}`}
            >
              {msg.text.split("\n").map((line, i) => (
                <div key={i}>{line}</div>
              ))}
            </div>
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