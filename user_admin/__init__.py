from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_jwt_extended import JWTManager
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)

# SQLite configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # SQLite URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking

# Other configurations
app.config['SECRET_KEY'] = 'e40ad44dd967df3ab659133e'
app.config['JWT_SECRET_KEY'] = '4d03d355e1864a7ead290a4d02af180e'
app.config['JWT_TOKEN_LOCATION'] = ['cookies']
app.config['JWT_COOKIE_CSRF_PROTECT'] = True  

# Initialize extensions
csrf = CSRFProtect(app)
jwt = JWTManager(app)
db = SQLAlchemy(app)
hashing = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "employee_login"
login_manager.login_message_category = 'info'

# Import routes and blueprints
from user_admin import routes
from user_admin.employee_search import employee_search_bp

# Register blueprints
app.register_blueprint(employee_search_bp, url_prefix="/admin/employee/search")
