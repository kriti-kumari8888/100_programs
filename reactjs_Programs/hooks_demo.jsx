import React, { useState, useEffect } from 'react';

// small custom hook: useWindowWidth
function useWindowWidth() {
  const [width, setWidth] = useState(window.innerWidth);
  useEffect(() => {
    function onResize() { setWidth(window.innerWidth); }
    window.addEventListener('resize', onResize);
    return () => window.removeEventListener('resize', onResize);
  }, []);
  return width;
}

export default function HooksDemo() {
  const width = useWindowWidth();
  return (
    <div style={{padding:20, fontFamily:'Arial'}}>
      <h2>Hooks Demo</h2>
      <p>Window width: {width}px</p>
      <p>Resize the browser to see updates.</p>
    </div>
  );
}
