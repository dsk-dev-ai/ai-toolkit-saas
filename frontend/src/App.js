import "./styles/main.css";

function App() {
  return (
    <div className="app">
      <header className="navbar">
        <h1>AI Toolkit SaaS</h1>
      </header>

      <main className="container">
        <h2>Generate AI Content</h2>

        <textarea
          placeholder="Enter your prompt..."
          className="input-box"
        />

        <button className="generate-btn">Generate</button>

        <div className="output-box">
          <p>AI response will appear here...</p>
        </div>
      </main>
    </div>
  );
}

export default App;