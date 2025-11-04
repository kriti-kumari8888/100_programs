// react_counter.jsx
// Simple React counter component. To run, create a React project (create-react-app) and paste into a component file.

import React, { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);
  return (
    <div style={{textAlign: 'center', marginTop: 40}}>
      <h1>Counter: {count}</h1>
      <button onClick={() => setCount(c => c + 1)}>Increment</button>
      <button onClick={() => setCount(c => c - 1)} style={{marginLeft:10}}>Decrement</button>
    </div>
  );
}
