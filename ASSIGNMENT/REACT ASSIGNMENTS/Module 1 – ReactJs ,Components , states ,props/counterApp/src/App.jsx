import React, { useState } from "react";
import "./App.css";

function App() {
  const [count, setCount] = useState(0);

  return (
    <div className="container">
      <h1>Counter App</h1>
      <img className="logo" src="https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg" alt="React Logo" />
      <h2 className="counter">{count}</h2>
      <button className="button increment" onClick={() => setCount(count + 1)}>
        Increment
      </button>
      <button className="button decrement" onClick={() => setCount(count - 1)}>
        Decrement
      </button>
    </div>
  );
}

export default App;
