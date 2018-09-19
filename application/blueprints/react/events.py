def add(socket):

    from flask_socketio import emit
    import json
    from application.blueprints.react import handler


    @socket.on('post')
    def handle(request):

        request = json.loads(request)

        if handler.validate(request):
            handler.store(request)
            return emit('accept', json.dumps(request))

        else:
            return emit('decline',{'meta':'333','payload':'bad request'})
