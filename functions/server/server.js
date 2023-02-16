//Authentication Express API Server
//Consists of an API, Endpoint. Two API's:
//POST: Login returning a Token 
//GET:  Resource endpoint to get employee information for login users.
//Server.js

const express = require('express');
const myapp = express();

myapp.get("/employees", (req, res) => {
    return res
        .status(401)
        .json({message: "Please login to access this resource" });
});

myapp.listen(5000, {} => {
    console.log("API Server is localhost:5000");
});
