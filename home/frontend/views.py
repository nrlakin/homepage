from flask import render_template, flash, redirect
from home import app
from home.frontend import frontend

@frontend.route('/', methods=['GET'])
@frontend.route('/index', methods=['GET'])
def index():
    return render_template('index.html')
