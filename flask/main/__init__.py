from flask import Flask, render_template
from config import Config
from .api.routes import api

from flask_cors import CORS
from helpers import JSONEncoder

app = Flask(__name__)
CORS(app)

app.register_blueprint(api)

app.json_encoder = JSONEncoder
app.config.from_object(Config)