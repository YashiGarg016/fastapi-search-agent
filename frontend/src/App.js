import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleSearch = async () => {
    if (!query) return;
    setLoading(true);
    try {
      const res = await axios.get(`http://127.0.0.1:8000/search?query=${query}`);
      setResults(res.data.results || []);
    } catch (err) {
      console.error(err);
      setResults([]);
    }
    setLoading(false);
  };

  return (
    <div className="App">
      <h1>Smart Search Agent</h1>
      <div className="search-box">
        <input
          type="text"
          value={query}
          placeholder="Search for something interesting..."
          onChange={(e) => setQuery(e.target.value)}
        />
        <button onClick={handleSearch}>Search</button>
      </div>
      {loading ? <p>Loading...</p> : null}
      <div className="results">
        {results.map((item, i) => (
          <div key={i} className="card">
            <h3>{item.title}</h3>
            <a href={item.link} target="_blank" rel="noopener noreferrer">
              {item.displayLink || item.link}
            </a>
            <p>{item.snippet}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;