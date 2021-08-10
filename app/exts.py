from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# 实例化 SQLAlchemy
db = SQLAlchemy()

loginmanager = LoginManager()