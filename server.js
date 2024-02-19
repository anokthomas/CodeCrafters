const express = require('express');
const mongoose = require('mongoose');
const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');

const app = express();
const PORT = 3000;

mongoose.connect('mongodb://localhost:27017/crud', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

app.use(express.json());

// User model
const User = mongoose.model('User', new mongoose.Schema({
  username: String,
  password: String,
}));

// Register route
app.post('/register', async (req, res) => {
  const { username, password } = req.body;
  const hashedPassword = bcrypt.hashSync(password, 8);

  try {
    const user = await User.create({
      username,
      password: hashedPassword,
    });

    res.status(201).send(user);
  } catch (error) {
    res.status(500).send(error);
  }
});

// Login route
app.post('/login', async (req, res) => {
  const { username, password } = req.body;

  try {
    const user = await User.findOne({ username });

    if (!user || !bcrypt.compareSync(password, user.password)) {
      throw new Error('Invalid username or password');
    }

    const token = jwt.sign({ username }, 'your-secret-key', { expiresIn: '1h' });

    res.status(200).send({ token });
  } catch (error) {
    res.status(401).send({ error: error.message });
  }
});

// Protected route
app.get('/protected', (req, res) => {
  try {
    const token = req.headers.authorization.split(' ')[1];
    const decoded = jwt.verify(token, 'your-secret-key');

    res.status(200).send(decoded);
  } catch (error) {
    res.status(401).send({ error: error.message });
  }
});

app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${3000}`);
});