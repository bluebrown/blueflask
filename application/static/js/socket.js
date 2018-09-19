// Instanciate socket.io connection.

let socket = io.connect('http://' + document.domain + ':' + location.port);


  // Emit test message and wait for response.
  socket.on('connect', function() {
      let message = {data: 'connection request'};
      socket.emit('request connection', JSON.stringify(message));
      console.log(message);
      
  });

  //Log response upon established client-server connection via socket.io.
  socket.on('accept connection', function(response) {
      response = JSON.parse(response);
      console.log(response);
  });
