import React, { useState } from 'react';

function Modal({children, onClose}){
  return (
    <div style={{position:'fixed', left:0, top:0, right:0, bottom:0, background:'rgba(0,0,0,0.5)', display:'flex', alignItems:'center', justifyContent:'center'}}>
      <div style={{background:'#fff', padding:20, borderRadius:6, minWidth:300}}>
        {children}
        <div style={{textAlign:'right', marginTop:12}}>
          <button onClick={onClose}>Close</button>
        </div>
      </div>
    </div>
  );
}

export default function ModalDemo(){
  const [open, setOpen] = useState(false);
  return (
    <div style={{padding:20, fontFamily:'Arial'}}>
      <h2>Modal Demo</h2>
      <button onClick={() => setOpen(true)}>Open Modal</button>
      {open && <Modal onClose={() => setOpen(false)}>
        <h3>Hello from Modal</h3>
        <p>This is a simple modal implementation using pure React & CSS-in-JS.</p>
      </Modal>}
    </div>
  );
}
