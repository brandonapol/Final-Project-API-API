from flask import Blueprint, request, jsonify, redirect
from helpers import token_required
from models import db, User

api = Blueprint('api',__name__, url_prefix='/api')

@api.route('/getdata')
def getdata():
    return redirect ('https://stackoverflow.com/questions/18206630/how-can-i-redirect-to-another-url-and-pass-a-list-object-using-flask')