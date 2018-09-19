import logging
logging.basicConfig(level=logging.DEBUG)


def build(key):
    """ Build the most basic flask app. """
    from flask import Flask
    app = Flask(__name__)
    app.config['SECRET_KEY'] = key
    return app


def upgrade(app):
    """ Upgrade http to websocket. """
    from flask_socketio import SocketIO
    return SocketIO(app)


def basic(app):
    """ The app is split in serveral files
    to keep things organized. Thats why we import
    our routes events and helper functions. """
    from application.routes import routes, crud
    from application.events import connect, chat
    routes.add(app)
    crud.add(app)
    connect.add(app.socket)
    chat.add(app.socket)


def connect_mongo(app):
    """ Returns the mongo client so make sure
    to let a variable point to it. """
    from pymongo import MongoClient
    return MongoClient('mongodb://data:27017/')


def connect_redis(app):
    """ Note that the host is 'cache' as the
    name of the docker-service. """
    import redis
    return redis.StrictRedis(host='cache', port=6379, db=0)


def bprint(app):
    """ Schema to add a blueprint and its events. """
    from application.blueprints.bprint import routes, events
    routes.add(app)
    events.add(app.socket)


def react(app):
    from application.blueprints.react import routes, events
    routes.add(app)
    events.add(app.socket)


def admin(app):
    from application.blueprints.admin  import routes, events
    routes.add(app)
    events.add(app.socket)


def make(key):
    """ Builds the app with all features.
    note that the app can be build out of
    the single functions. We dont need make(). """
    app = build(key)
    app.socket = upgrade(app)
    app.client = connect_mongo(app)
    app.cache = connect_redis(app)
    basic(app)
    admin(app)
    react(app)
    return app


app = make('secret key') # We need to pass the secret key.
