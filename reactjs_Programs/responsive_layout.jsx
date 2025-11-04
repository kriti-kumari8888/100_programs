import React from 'react';

export default function ResponsiveLayout() {
  const boxStyle = {padding:20, fontFamily:'Arial'};
  return (
    <div style={boxStyle}>
      <h2>Responsive Layout</h2>
      <div style={{display:'flex', flexWrap:'wrap'}}>
        {[1,2,3,4,5,6].map(i => (
          <div key={i} style={{flex:'1 0 200px', margin:6, padding:12, border:'1px solid #ccc', borderRadius:6}}>
            <h4>Card {i}</h4>
            <p>Content for card {i}.</p>
          </div>
        ))}
      </div>
      <p style={{marginTop:12}}>Resize the window — the cards wrap responsively.</p>
    </div>
  );
}
