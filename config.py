import os
basedir = os.path.abspath(os.path.dirname(__file__))

if os.environ.get('DATABASE_URL') is None:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'home.db')
else:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_RECORD_QUERIES = True
DATABASE_QUERY_TIMEOUT = 0.5

WTF_CSRF_ENABLED = True

if os.environ.get('CSRF_SECRET') is None:
    SECRET_KEY = 'tough secret'
else:
    SECRET_KEY = os.environ.get('CSRF_SECRET')

# Mail server settings
MAIL_SERVER = 'smtp.googlemail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

# Bad practice!
TWILIO_SID="ACf8ca05c046a335b7789028f35cb1d64c"
TWILIO_TOKEN="f2f6b1863787fc500b564c70c63c8989"
