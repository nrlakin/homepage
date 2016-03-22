from flask import render_template, flash, redirect, send_file, url_for
from home import app
from home.frontend import frontend

@frontend.route('/', methods=['GET'])
@frontend.route('/index', methods=['GET'])
def index():
    return render_template('index.html',
                            title='Home')

@frontend.route('/about')
def about():
    return render_template('about.html',
                            title='About This Page')

@frontend.route('/resume')
def get_resume():
    return render_template('resume.html',
                            title='Resume')

@frontend.route('/download/<path:filename>')
def download(filename):
    return send_file('/'.join(['static','download', filename]))
