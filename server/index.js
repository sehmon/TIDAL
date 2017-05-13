var path = require('path');
var app = require('express')();
var server = require('http').createServer(app);
var io = require('socket.io')(server);

io.on('connection', function(){
  console.log("Client connected");
});

app.get('/', function(req, res) {
      res.sendFile(path.join(__dirname+'/index.html'));
});

server.listen(3000);
