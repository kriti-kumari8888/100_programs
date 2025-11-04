// websocket_chat.js
// Simple WebSocket chat server using the `ws` package. To run: npm install ws && node websocket_chat.js

const WebSocket = require('ws');
const wss = new WebSocket.Server({ port: 8080 });

wss.on('connection', function connection(ws) {
  ws.on('message', function message(msg) {
    console.log('received: %s', msg);
    // broadcast to others
    wss.clients.forEach(function each(client) {
      if (client !== ws && client.readyState === WebSocket.OPEN) {
        client.send(msg);
      }
    });
  });
  ws.send('Welcome to the WebSocket chat!');
});

console.log('WebSocket server listening on ws://localhost:8080');
