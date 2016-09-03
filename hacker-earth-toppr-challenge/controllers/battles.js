var models = require('../models');

module.exports.set = function(app) {
    app.get('/list', function(req, res) {
        models.Battles.findAll({ attributes: ['name', 'location', 'region'] }).then(function(battles) {
            if (battles) {
                res.status(200).send(battles);
            } else {
                res.status(500).send('Something went wrong!');
            }
        }).catch(function(err) {
            res.status(500).send('Something went wrong');
        });
    });

    app.get("/count", function(req, res) {
        models.Battles.findAndCountAll({ attributes: ['name'] }).then(function(battles) {
            if (battles) {
                res.status(200).send('' + battles.count);
            } else {
                res.status(500).send('Something went wrong!');
            }
        }).catch(function(err) {
            res.status(500).send('Something went wrong');
        });
    });
}
