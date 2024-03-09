const express = require('express');
const apiRoutes = require('./routes/apiRoutes');
const cors = require('cors');
require('dotenv').config();

const corsOptions = {
    origin: "*",
};

const app = express();

app.use(express.json());
app.use(cors(corsOptions));
app.use('/api', apiRoutes); 

module.exports = app;