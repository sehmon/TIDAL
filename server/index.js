var path = require('path')
var express = require('express')
var app = express()
var server = require('http').createServer(app)
var io = require('socket.io')(server)
var bodyParser = require('body-parser')

app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())

var carMoving = false
var currFood;

io.on('connection', function (socket) {
  console.log('Client connected')
  socket.on('add food', function (food) {
    console.log('added', food.name)
  })
})

app.use(express.static('static'))

app.get('/', function (req, res) {
  res.sendFile(path.join(__dirname+'/index.html'))
})

app.get('/status', function (req, res) {
  res.json({food: currFood})
})

app.post('/status', function (req, res) {
  if (req.body.food.name != currFood) {
      console.log("New Food Detected: " + req.body.food.name)
      currFood = req.body.food;
  }
  console.log(currFood);
})

server.listen(3000, function () {
  console.log('Listening on port 3000...')
})
