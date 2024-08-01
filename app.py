from flask import Flask
from routes import init_route
from config import Config
from model import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    init_route(app)
    db.init_app(app)
    return app