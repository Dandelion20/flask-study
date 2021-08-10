import os
# ----------FLASK-WTF扩展库配置--------- #
# 激活跨站点请求伪造保护
CSRF_ENABLED = True
# CSRF被激活时，用于令牌加密，表单验证
SECRET_KEY = 'you-will-never-guess'

# ----------Mysql数据库配置--------- #
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:205599lj*@localhost:3306/flaskdb'
SQLALCHEMY_TRACK_MODIFICATIONS = False