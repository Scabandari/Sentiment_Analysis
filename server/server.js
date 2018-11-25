// server.js
// Tutorial used as an example to get started for this server:
// https://scotch.io/tutorials/build-a-restful-api-using-node-and-express-4
// BASE SETUP
// =============================================================================

// call the packages we need
var express = require("express"); // call express
var app = express(); // define our app using express
var bodyParser = require("body-parser");

// configure app to use bodyParser()
// this will let us get the data from a POST
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

var port = process.env.PORT || 8001 // set our port

// ROUTES FOR OUR API
// =============================================================================
var router = express.Router(); // get an instance of the express Router

// test route to make sure everything is working (accessed at GET http://localhost:8080/api)
router.get("/", function(req, res) {
	res.json({ message: "hooray! welcome to our api!" });
});

// more routes for our API will happen here

// REGISTER OUR ROUTES -------------------------------
// all of our routes will be prefixed with /api
app.use("/api", router);

// START THE SERVER
// =============================================================================
app.listen(port);
console.log("Magic happens on port " + port);

var mongoose = require("mongoose");
mongoose.connect("mongodb://ryan:pass@ds119490.mlab.com:19490/basicproject");
var Twitter = require("./models/models");

// ROUTES FOR OUR API
// =============================================================================
var router = express.Router(); // get an instance of the express Router

// middleware to use for all requests
router.use(function(req, res, next) {
	// do logging
	console.log("Something is happening.");
	next(); // make sure we go to the next routes and don't stop here
});

// test route to make sure everything is working (accessed at GET http://localhost:8080/api)
router.get("/", function(req, res) {
	res.json({ message: "hooray! welcome to our api!" });
});

// more routes for our API will happen here

// REGISTER OUR ROUTES -------------------------------
// all of our routes will be prefixed with /api
app.use("/api", router);

router
	.route("/twitter")

	// create a bear (accessed at POST http://localhost:8080/api/bears)
	.post(function(req, res) {
		var bear = new Twitter(); // create a new instance of the Bear model
		bear.ticker = req.body.ticker;
		bear.sentiment = req.body.sentiment; // set the bears name (comes from the request)

		// save the bear and check for errors
		bear.save(function(err) {
			if (err) res.send(err);

			res.json({ message: "created!" });
		});
	})

	// get all the bears (accessed at GET http://localhost:8080/api/bears)
	.get(function(req, res) {
		Twitter.find(function(err, bears) {
			if (err) res.send(err);

			res.json(bears);
		});
	});
router
	.route("/twitter/:bear_id")

	// get the bear with that id (accessed at GET http://localhost:8080/api/bears/:bear_id)
	.get(function(req, res) {
		Twitter.findById(req.params.bear_id, function(err, bear) {
			if (err) res.send(err);
			res.json(bear);
		});
	})
	// update the bear with this id (accessed at PUT http://localhost:8080/api/bears/:bear_id)
	.put(function(req, res) {
		// use our bear model to find the bear we want
		Twitter.findById(req.params.bear_id, function(err, bear) {
			if (err) res.send(err);

			bear.sentiment = req.body.sentiment; // update the bears info

			// save the bear
			bear.save(function(err) {
				if (err) res.send(err);

				res.json({ message: "sentiment updated!" });
			});
		});
	});

// REGISTER OUR ROUTES -------------------------------
// all of our routes will be prefixed with /api
app.use("/api", router);
