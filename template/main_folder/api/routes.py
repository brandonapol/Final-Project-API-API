from flask import Blueprint, request, jsonify
from helpers import token_required
from models import db, User

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return {'yee': 'haw'}

# Add routes