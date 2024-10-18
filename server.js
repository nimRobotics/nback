const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse incoming JSON data
app.use(express.json());

// Allow cross-origin requests (if necessary)
app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
    next();
});

// Route to receive data
app.post('/receive-data', (req, res) => {
    console.log('Received data:', req.body);  // Log received data
    res.json({ message: 'Data received successfully!' });
});

// Start the server
app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
