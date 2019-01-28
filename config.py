import os

# TODO: You need to replace the next values with the appropriate values for your configuration

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = os.environ.get('DB_CONNECTION_URI') or 'postgresql://ezplanner:passw0rd@localhost/ezplanner'