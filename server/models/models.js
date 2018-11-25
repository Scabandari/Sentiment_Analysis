// app/models/bear.js

var mongoose = require("mongoose");
var Schema = mongoose.Schema;
var Twitter = new Schema({
	ticker: {
		type: String,
		required: true
	},
	sentiment: {
		type: Number,
		required: true
	}
});

module.exports = mongoose.model("twitter", Twitter);
