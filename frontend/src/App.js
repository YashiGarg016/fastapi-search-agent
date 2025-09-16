import React, { useState } from "react";
import axios from "axios";
import "./App.css"; // Optional: for styling

function App() {
  const [query, setQuery] = useState("");
  const [googleResults, setGoogleResults] = useState([]);
  const [duckResults, setDuckResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSearch = async () => {
    if (!query.trim()) return;

    setLoading(true);
    setError("");
    setGoogleResults([]);
    setDuckResults([]);

    try {
      const res = await axios.get(`http://localhost:8000/search?query=${query}`);

      // Optional log for debugging
      console.log("Raw backend response:", res.data);

      // Updated mapping: use res.data.results.google and res.data.results.duckduckgo
      const googleData = Array.isArray(res.data.results?.google)
        ? res.data.results.google.map((item) => ({
            title: item.title || "No title",
            link: item.link,
            displayLink: item.displayLink || item.link,
            snippet: item.snippet || "",
            source: "google",
          }))
        : [];

      const duckData = Array.isArray(res.data.results?.duckduckgo)
        ? res.data.results.duckduckgo.map((item) => ({
            title: item.title || item.Text || "No title",
            link: item.link || item.FirstURL || "#",
            displayLink: item.displayLink || item.FirstURL || item.link || "#",
            snippet: item.snippet || item.Text || "",
            source: "duckduckgo",
          }))
        : [];

      console.log("Mapped Google:", googleData);
      console.log("Mapped DuckDuckGo:", duckData);

      setGoogleResults(googleData);
      setDuckResults(duckData);
    } catch (err) {
      console.error("Error fetching results:", err);
      setError("Something went wrong. Please try again later.");
    }

    setLoading(false);
  };

  return (
    <div className="App">
      <h1>Smart Search Agent 🔎</h1>

      <div className="search-box">
        <input
          type="text"
          value={query}
          placeholder="Search for something cool"
          onChange={(e) => setQuery(e.target.value)}
        />
        <button onClick={handleSearch}>Search</button>
      </div>

      {loading && <p>Loading...</p>}
      {error && <p className="error">{error}</p>}

      <div className="side-by-side">
        <div className="provider">
          <h2>🔍 Google Results</h2>
          {googleResults.length === 0 ? (
            <p>No Google results found.</p>
          ) : (
            googleResults.map((item, i) => (
              <div key={i} className="card">
                <h3>{item.title}</h3>
                <a href={item.link} target="_blank" rel="noopener noreferrer">
                  {item.displayLink || item.link}
                </a>
                <p>{item.snippet}</p>
                <span className="source-tag google">🔍 Google</span>
              </div>
            ))
          )}
        </div>

        <div className="provider">
          <h2>🕵️ DuckDuckGo Results</h2>
          {duckResults.length === 0 ? (
            <p>No DuckDuckGo results found.</p>
          ) : (
            duckResults.map((item, i) => (
              <div key={i} className="card">
                <h3>{item.title}</h3>
                <a href={item.link} target="_blank" rel="noopener noreferrer">
                  {item.displayLink || item.link}
                </a>
                <p>{item.snippet}</p>
                <span className="source-tag duckduckgo">🕵️ DuckDuckGo</span>
              </div>
            ))
          )}
        </div>
      </div>
    </div>
  );
}

export default App;