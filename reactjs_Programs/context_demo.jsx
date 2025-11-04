import React, { createContext, useContext, useState } from 'react';

const ThemeContext = createContext();

function ThemeToggle() {
  const {dark, setDark} = useContext(ThemeContext);
  return (
    <div>
      <label>
        <input type="checkbox" checked={dark} onChange={e => setDark(e.target.checked)} /> Dark
      </label>
    </div>
  );
}

export default function ContextDemo() {
  const [dark, setDark] = useState(false);
  const style = {padding:20, fontFamily:'Arial', background: dark ? '#222' : '#fff', color: dark ? '#eee' : '#000', minHeight:200};

  return (
    <ThemeContext.Provider value={{dark, setDark}}>
      <div style={style}>
        <h2>Context Demo (Theme)</h2>
        <ThemeToggle />
        <p>The current theme is <strong>{dark ? 'Dark' : 'Light'}</strong>.</p>
      </div>
    </ThemeContext.Provider>
  );
}
