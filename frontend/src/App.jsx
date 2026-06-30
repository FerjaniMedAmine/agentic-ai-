//
import { useState } from 'react'
import './App.css'

function App() {
  const [input, setInput] = useState('')
  const [messages, setMessages] = useState([
    {
      id:1,
      role: 'assistant',
      text: 'Hello! How can I help you today?',
    },
  ])

  async function handleSubmit(event) {
    event.preventDefault()

    if (input.trim() === '') {
      return
    }

    const userMessage = {
      id: Date.now(),
      role: 'user',
      text: input,
    }

    setMessages([...messages, userMessage])
    setInput('')

    const response = await fetch('http://127.0.0.1:8001/chat', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        message: input,
      }),
    })

    const data = await response.json()

    const assistantMessage = {
      id: Date.now() + 1,
      role: 'assistant',
      text: data.response,
    }

    setMessages([...messages, userMessage, assistantMessage])
  }




  function handleNewChat() {
    setMessages([
      {
        role: 'assistant',
        text: 'Hello! How can I help you today?',
      },
    ])

    setInput('')
  }

  return (
    <div className="app">
      <header className="sidebar">
        <h2>AI Assistant</h2>
        <button onClick={handleNewChat}>+ New Chat</button>
      </header>

      <main className="chat-container">
        
        <section className="messages">
          {messages.map((message) => (
            <div key={message.id} className={`message ${message.role}`}>
              {message.text}
            </div>
          ))}
        </section>

        <form className="chat-input" onSubmit={handleSubmit}>
          <input
            type="text"
            placeholder="Ask me anything..."
            value={input}
            onChange={(event) => setInput(event.target.value)}
          />

          <button type="submit">Send</button>
        </form>
      </main>
    </div>
  )
}
// lilfou9 well done
export default App

