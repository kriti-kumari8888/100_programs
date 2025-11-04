import React, { useState } from 'react';

export default function CounterApp() {
  const [count, setCount] = useState(0);
  return (
    <div style={{padding:20, fontFamily:'Arial'}}>
      <h2>Counter App</h2>
      <p style={{fontSize:24}}>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
      <button onClick={() => setCount(count - 1)} style={{marginLeft:8}}>Decrement</button>
      <button onClick={() => setCount(0)} style={{marginLeft:8}}>Reset</button>
    </div>
  );
}
