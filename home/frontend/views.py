from flask import render_template, flash, redirect, send_file, url_for, jsonify
from home import app, redis_store
from home.frontend import frontend

@frontend.route('/runner/<runner_name>', methods=['POST'])
def update_runner(runner_name):
    state = redis_store.get('state')
    if state == 'pre_race':
        redis_store.set(runner_name, 0)
        redis_store.sadd('runners', runner_name)
    elif state == 'racing':
        redis_store.incr(runner_name)
    return jsonify({"message": runner_name+"+1"})

@frontend.route('/slapdash/init', methods=['GET','POST'])
def init_slapdash():
    redis_store.delete('runners')
    redis_store.set('state', 'pre_race')
    return render_template('slapdash.html',
                            title='SlapDash')

@frontend.route('/slapdash/update', methods=['GET'])
def update_slapdash():
    print redis_store.get(runners)

@frontend.route('/test_api', methods=['GET'])
def test_api():
    return jsonify({"message": "hello!"})

@frontend.route('/test_post', methods=['POST'])
def test_post():
    return 201, jsonify({"message": "posted!"})

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
    flash("Downloading " + '/'.join(['static','download', filename]))
    return send_file('/'.join(['static','download', filename]))
