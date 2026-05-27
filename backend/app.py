from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from config import Config
from models import db
from routes import register_routes


# CREATE FLASK APP FIRST
app = Flask(__name__)

# LOAD CONFIG
app.config.from_object(Config)

# ENABLE CORS (AFTER app is created)
CORS(app, resources={r"/*": {"origins": "*"}})

# INITIALIZE DATABASE
db.init_app(app)

# INITIALIZE JWT
jwt = JWTManager(app)

# REGISTER ROUTES
register_routes(app)


# CREATE DATABASE TABLES
with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
