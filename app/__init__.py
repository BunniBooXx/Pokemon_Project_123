from flask import Flask
from .models import db, User
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager
from .auth import auth
from .social import social


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(auth)
app.register_blueprint(social)

db.init_app(app)

migrate = Migrate(app,db)
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


from . import routes 