import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.redis import FlaskRedis
from twilio.rest import TwilioRestClient
# from config import basedir

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)
redis_store = FlaskRedis(app)

twilio = TwilioRestClient(app.config['TWILIO_SID'], app.config['TWILIO_TOKEN'])

# from home.api import api as api_module
from home.frontend import frontend as frontend_module

# app.register_blueprint(api_module, url_prefix='/api/v0.1')
app.register_blueprint(frontend_module, url_prefix=None)

if not app.debug and os.environ.get('HEROKU') is None:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('tmp/homepage.log', 'a', 1*1024*1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('Homepage server startup')

if os.environ.get('HEROKU') is not None:
    import logging
    stream_handler = logging.StreamHandler()
    app.logger.addHandler(stream_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Homepage server startup')

from . import models, errors
