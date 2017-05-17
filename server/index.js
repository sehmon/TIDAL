var path = require('path')
var express = require('express')
var app = express()
var server = require('http').createServer(app)
var io = require('socket.io')(server)
var bodyParser = require('body-parser')

app.use(bodyParser.urlencoded({ extended: false }))
app.use(bodyParser.json())

var carMoving = false

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
  res.json({forward: carMoving})
})

app.post('/status', function (req, res) {
  carMoving = (req.body.newCarValue === true)
  res.send('Changed carMoving to: ' + carMoving.toString())
  console.log('Changed carMoving to: ' + carMoving.toString())
})

server.listen(3000, function () {
  console.log('Listening on port 3000...')
})
