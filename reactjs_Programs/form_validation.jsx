import React, { useState } from 'react';

export default function FormValidation() {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [errors, setErrors] = useState({});

  function validate() {
    const e = {};
    if (!name.trim()) e.name = 'Name is required';
    if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) e.email = 'Invalid email';
    setErrors(e);
    return Object.keys(e).length === 0;
  }

  function submit(e) {
    e.preventDefault();
    if (validate()) {
      alert(`Submitted: ${name} <${email}>`);
      setName(''); setEmail(''); setErrors({});
    }
  }

  return (
    <div style={{padding:20, fontFamily:'Arial'}}>
      <h2>Form Validation</h2>
      <form onSubmit={submit} noValidate>
        <div>
          <label>Name:</label><br/>
          <input value={name} onChange={ev => setName(ev.target.value)} />
          {errors.name && <div style={{color:'red'}}>{errors.name}</div>}
        </div>
        <div style={{marginTop:8}}>
          <label>Email:</label><br/>
          <input value={email} onChange={ev => setEmail(ev.target.value)} />
          {errors.email && <div style={{color:'red'}}>{errors.email}</div>}
        </div>
        <button type="submit" style={{marginTop:12}}>Submit</button>
      </form>
    </div>
  );
}
