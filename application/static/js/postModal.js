function openModal(){
  $('.modal').attr('class', 'modal is-active');
};

function closeModal(){
  $('.modal').attr('class', 'modal');
};

function postRequest(){
  obj = {data: 'this is data'};
  json = JSON.stringify(obj);
  socket.emit('post', json );
  console.log(json);
};

socket.on('accept', function(response){
  console.log(response);
});

socket.on('decline', function(response){
  console.log(response);
});
