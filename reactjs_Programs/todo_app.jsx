import React, { useState } from 'react';

export default function TodoApp() {
  const [items, setItems] = useState([]);
  const [text, setText] = useState('');

  function addItem() {
    if (!text.trim()) return;
    setItems([...items, { id: Date.now(), text: text.trim() }]);
    setText('');
  }

  function remove(id) {
    setItems(items.filter(i => i.id !== id));
  }

  return (
    <div style={{padding:20, fontFamily:'Arial'}}>
      <h2>Todo App</h2>
      <div>
        <input value={text} onChange={e => setText(e.target.value)} placeholder="Add todo" />
        <button onClick={addItem} style={{marginLeft:8}}>Add</button>
      </div>
      <ul>
        {items.map(i => (
          <li key={i.id} style={{marginTop:8}}>
            {i.text} <button onClick={() => remove(i.id)} style={{marginLeft:8}}>Remove</button>
          </li>
        ))}
      </ul>
    </div>
  );
}
