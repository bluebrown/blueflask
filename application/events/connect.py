def add(socket):
    """"Add socket events to socket.io."""

    from flask_socketio import emit
    import json

    @socket.on('request connection')
    def handle_connection(message):
        """Check new connection and broadcast info json."""
        validate = json.loads(message)
        response = {'data': 'user connected'}
        emit('accept connection', json.dumps(response), broadcast=True)
