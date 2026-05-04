import React, { useState, useRef, useEffect } from "react";
import ReactMarkdown from "react-markdown";
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

    // Add empty bot message (we will stream into this)
    const botMessage = { sender: "bot", text: "" };
    setMessages((prev) => [...prev, botMessage]);

    const response = await fetch("http://127.0.0.1:8000/chat-stream", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text: input }),
    });

    const reader = response.body.getReader();
    const decoder = new TextDecoder("utf-8");

    let done = false;

    while (!done) {
      const { value, done: doneReading } = await reader.read();
      done = doneReading;

      const chunk = decoder.decode(value, { stream: true });

      // 🔥 Clean SSE format (important)
      const lines = chunk.split("\n");
      let textChunk = "";

      lines.forEach((line) => {
        if (line.startsWith("data: ")) {
          textChunk += line.replace("data: ", "");
        }
      });

      if (textChunk) {
        setMessages((prev) => {
          const updated = [...prev];
          updated[updated.length - 1].text += textChunk;
          return updated;
        });
      }
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
              <ReactMarkdown>{msg.text}</ReactMarkdown>
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