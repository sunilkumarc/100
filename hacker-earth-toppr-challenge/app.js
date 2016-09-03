var express = require('express');
var battles_controller = require('./controllers/battles.js');
var bodyParser = require('body-parser');

var app = express();

// Middleware to parse json body
app.use(bodyParser.json());

app.get('/', function(req, res) {
    res.status(200).send("Server Working!");
});

battles_controller.set(app);

var port = Number(process.env.PORT || 8000)
app.listen(port);
console.log('Got Minint App Working!');
