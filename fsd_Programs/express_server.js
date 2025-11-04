// express_server.js
// Minimal Express server. To run: npm init -y && npm install express && node express_server.js

const express = require('express');
const app = express();
const port = process.env.PORT || 3000;

app.use(express.json());

app.get('/', (req, res) => res.send('Hello from Express server!'));

app.get('/api/health', (req, res) => res.json({status: 'ok'}));

app.post('/api/echo', (req, res) => res.json({you_sent: req.body}));

app.listen(port, () => console.log(`Express server listening on http://localhost:${port}`));
