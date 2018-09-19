def add(socket):

    from flask_socketio import emit
    import json

    @socket.on('send message')
    def handle_chat_message(message):
        """Broadcast the recieved message if its valid."""
        validate = json.loads(message)
        if validate['message'] != '':
            valid = {'data': validate}
            emit('post message', json.dumps(valid), broadcast=True)
        else:
            emit('decline message', json.dumps({'data': 'no text'}));
