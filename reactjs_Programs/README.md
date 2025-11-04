# reactjs_Programs

This folder contains 10 small React example component files (ES6 + JSX). These are standalone component files you can use inside a React project (Create React App, Vite + React, etc.).

Files included:
- `hello_world.jsx` - Simple Hello World component.
- `counter_app.jsx` - A counter using useState.
- `todo_app.jsx` - Simple todo list (add/remove).
- `list_fetch.jsx` - fetch() demo (uses jsonplaceholder.typicode.com).
- `form_validation.jsx` - Simple form with validation.
- `routing_demo.jsx` - Minimal state-based routing demo (no react-router).
- `context_demo.jsx` - Demonstrates React Context for a theme toggle.
- `hooks_demo.jsx` - Custom hook demo (window width).
- `modal_demo.jsx` - Simple modal implementation.
- `responsive_layout.jsx` - Responsive cards layout demo.

How to use
1. Create a React project (example using Create React App):
   npx create-react-app my-app
   cd my-app
2. Copy one of the example files into `src/` (for example `src/hello_world.jsx`).
3. Replace `src/App.js` contents with:

```jsx
import React from 'react';
import HelloWorld from './hello_world.jsx';

export default function App() {
  return <HelloWorld />;
}
```

4. Start the dev server:

```powershell
npm start
```

Notes
- These examples avoid external packages so they should run in a default React setup.
- `list_fetch.jsx` fetches data from an external public API (jsonplaceholder). Make sure you have internet when testing that demo.
- If you want, I can turn each example into a small independent project, or create an index menu app that lets you pick and run any demo inside a single project.
