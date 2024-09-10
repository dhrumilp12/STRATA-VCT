require('dotenv').config();
const express = require('express');
const bodyParser = require('body-parser'); // Used to parse JSON bodies
const { conversation } = require('./src/agents/ai_agent');
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware to parse JSON bodies
app.use(bodyParser.json());

// Root route to check if server is running
app.get('/', (req, res) => {
  res.send('Hello World!');
});

// Define a POST route to receive user input and return AI response
app.post('/ai-response', (req, res) => {
  const userInput = req.body.input;

  // Use the Bedrock model to generate a response
  conversation.predict({ input: userInput }).then(response => {
    res.json({ reply: response });
  }).catch(error => {
    res.status(500).json({ error: 'Error processing your request', details: error.message });
  });
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});