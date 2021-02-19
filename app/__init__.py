import logging
import os
from flask import Flask, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from logging.handlers import SMTPHandler, RotatingFileHandler
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel, lazy_gettext as _l


# initiate the Flask app
app = Flask(__name__)

# uses config.py file for configuration
app.config.from_object(Config)

# uses SQLAlchemy as database management
db = SQLAlchemy(app)

# uses Flask_Migrate extension for database migration management
migrate = Migrate(app, db)

# uses Flask_Login to manage the user's logged-in state
login = LoginManager(app)
login.login_view = 'login'

# uses flask_mail to send emails
mail = Mail(app)

# uses flask_bootstrap to style html
bootstrap = Bootstrap(app)

# uses flask_moment to access moment.js in flask
moment = Moment(app)

# uses flask_babel for translation
babel = Babel(app)

if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)
    
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')

# works with Accept-Language to use users' prefered language
@babel.localeselector
def get_locale():
    #return request.accept_languages.best_match(app.config['LANGUAGES'])
    #return 'de'
    #return 'es'
    #return 'fr'
    #return 'nl'
    #return 'ru'
    #return 'sv'
    #return 'zh'

from app import routes, models, errors
