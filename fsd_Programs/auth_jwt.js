// auth_jwt.js
// Minimal JWT auth demonstration using jsonwebtoken. To run: npm install jsonwebtoken express && node auth_jwt.js

const express = require('express');
const jwt = require('jsonwebtoken');
const app = express();
app.use(express.json());
const SECRET = process.env.JWT_SECRET || 'change-me';

app.post('/login', (req, res) => {
  const {username} = req.body || {};
  if (!username) return res.status(400).json({error: 'username required'});
  const token = jwt.sign({user: username}, SECRET, {expiresIn: '1h'});
  res.json({token});
});

function auth(req, res, next) {
  const h = req.headers.authorization || '';
  const token = h.replace(/^Bearer\s+/i, '');
  try {
    req.user = jwt.verify(token, SECRET);
    next();
  } catch (e) {
    res.status(401).json({error: 'unauthorized'});
  }
}

app.get('/me', auth, (req, res) => {
  res.json({user: req.user});
});

app.listen(4000, () => console.log('Auth demo listening on http://localhost:4000'));
