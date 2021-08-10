"""
项目的初始化
"""
from flask import Flask
from .views.hello import HelloWorld
from .views.login import LoginView,LogoutView,RegisterView
from .views.index import IndexView
from .config import *
from flask_migrate import Migrate

# from .models.model import User,Post
from .models.User import User

from .exts import db,loginmanager
from flask_login import LoginManager

# 登录管理:flask_login常用的类是LoginManager，对象创建完成就可以和Flask应用来完成登录相关功能

loginmanager.session_protection = 'strong'
loginmanager.login_view = 'base.login'
# 实例化flask_migrate
migrate = Migrate()

def create_app():
    """应用工厂函数"""
    # instance_relative_config：设置配置文件以instance文件夹为相对文件夹
    # 即config.py配置文件放置在instance文件夹下。
    app = Flask(__name__, instance_relative_config=True)
    # 加载config配置文件
    app.config.from_object(config)
    # 初始化数据库
    db.init_app(app)
    migrate.init_app(app, db)
    # 初始化登陆扩展flask-login
    loginmanager.init_app(app)
    loginmanager.login_view='login'
    # 重写需要登录提示信息
    loginmanager.login_message = '请登录后访问此页面'
    # 注册hello视图URL,view_func  指定这个url对应的是哪个函数（对于类视图我们要进行注册）
    # View.as_view(’<指定函数的名称>’),as_view中的参数用来指定绑定的是哪个类的dispatch_request方法
    app.add_url_rule('/hello', view_func=HelloWorld.as_view('hello'))

    # 注册index首页视图URL
    app.add_url_rule('/index', view_func=IndexView.as_view('index'))

    # 注册Register注册视图URL
    app.add_url_rule('/register', view_func=RegisterView.as_view('register'))


    # 注册Login登录视图URL
    app.add_url_rule('/login', view_func=LoginView.as_view('login'))

    # 注册Logout退出视图URL
    app.add_url_rule('/logout', view_func=LogoutView.as_view('logout'))
    try:
        # 确保 app.instance_path 存在
        os.makedirs(app.instance_path)
    except OSError:
        pass

    return app
