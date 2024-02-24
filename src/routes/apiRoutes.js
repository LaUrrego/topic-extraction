const express = require('express');
const router = express.Router();
const contextController = require('../controllers/contextController');

router.post('/context', contextController.processRequest);

module.exports = router