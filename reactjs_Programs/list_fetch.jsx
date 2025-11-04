import React, { useEffect, useState } from 'react';

export default function FetchList() {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    let mounted = true;
    setLoading(true);
    fetch('https://jsonplaceholder.typicode.com/posts')
      .then(res => res.json())
      .then(data => {
        if (mounted) setItems(data.slice(0, 10));
      })
      .catch(err => { if (mounted) setError(err.message); })
      .finally(() => { if (mounted) setLoading(false); });
    return () => { mounted = false; };
  }, []);

  if (loading) return <div style={{padding:20}}>Loading...</div>;
  if (error) return <div style={{padding:20}}>Error: {error}</div>;

  return (
    <div style={{padding:20, fontFamily:'Arial'}}>
      <h2>Fetch Demo</h2>
      <ul>
        {items.map(i => <li key={i.id}><strong>{i.id}.</strong> {i.title}</li>)}
      </ul>
    </div>
  );
}
