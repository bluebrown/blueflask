function systemMessage(parent, msg) {
  let sys = $('<p class="is-system">').append(msg);
  parent.append(sys);
};

function userMessage(parent, name, msg) {
  let usr = $('<span class="usr">').append(name);
  let _msg = $('<span>').append(msg);
  let chatMessage = $('<p class="chat-message">').append(usr,' ',_msg);
  parent.append(chatMessage);
};

// Emit message to the server using socket.io.
function sendMessage() {
  let message = {
    username: $('#input-usr').val(),
    message: $('#textarea-msg').val()
  };
  socket.emit('send message',  JSON.stringify(message) );
};

// Post message recieved from server emit.
socket.on('post message', function(message) {
  response = JSON.parse(message);
  userMessage(
    $('#chat-text'),
    response.data.username,
    response.data.message
  );
  $('#textarea-msg').val('').focus();
});

socket.on('decline message', function(message){
  response = JSON.parse(message);
  systemMessage( $('#chat-text'), response.data );
  $('#textarea-msg').attr('class', 'textarea is-danger');
  $('#textarea-msg').val('').focus();
});

//Log response upon established client-server connection via socket.io.
socket.on('accept connection', function(response) {
    systemMessage( $('#chat-text'), JSON.parse(response).data );
    let sys = document.getElementsByClassName('is-system');
    sys.fadeOut(3500);
    document.getElementById('chat-text').removeChild(sys);
});
