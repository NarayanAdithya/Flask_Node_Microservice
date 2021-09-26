var fs = require('fs');

// json file with the data
var data = fs.readFileSync('app.json');

var elements = JSON.parse(data);
const express = require("express");
const app = express();

// To solve the cors issue
const cors=require('cors');
	
app.listen(5001,'0.0.0.0',function(){console.log("Server Start at the Port");});

	
app.use(express.static('public'));
app.use(cors());

// when get request is made, alldata() is called
app.get('/elements', alldata);

function alldata(request, response) {
	
	// Returns all information about the elements
	response.send(elements);
}

app.get('/products/:element/', searchElement);

function searchElement(request, response) {
	var word = request.params.element;
	word = word.slice(0).toLowerCase();
	
	if(elements[word]) {
		var reply = elements[word];		
	}
	else {
		var reply = {
			status:"Not Found"
		}
	}
	
	response.send(reply);
}

