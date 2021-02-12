from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# initiate the Flask app
app = Flask(__name__)

# use the config.py file for configuration
app.config.from_object(Config)

# use SQLAlchemy as database management
db = SQLAlchemy(app)

# use Flask-Migrate extension for database migration management
migrate = Migrate(app, db)

# use Flask-Login to manage the user's logged-in state
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models, errors