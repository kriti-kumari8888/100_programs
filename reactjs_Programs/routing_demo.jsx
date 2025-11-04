import React, { useState } from 'react';

// Minimal routing demo without react-router: simple state-based "pages".
export default function RoutingDemo() {
  const [page, setPage] = useState('home');
  return (
    <div style={{padding:20, fontFamily:'Arial'}}>
      <nav style={{marginBottom:12}}>
        <button onClick={() => setPage('home')}>Home</button>
        <button onClick={() => setPage('about')} style={{marginLeft:8}}>About</button>
        <button onClick={() => setPage('contact')} style={{marginLeft:8}}>Contact</button>
      </nav>

      {page === 'home' && <div><h2>Home</h2><p>Welcome to the home page.</p></div>}
      {page === 'about' && <div><h2>About</h2><p>This is a small routing demo.</p></div>}
      {page === 'contact' && <div><h2>Contact</h2><p>Email: example@example.com</p></div>}
    </div>
  );
}
