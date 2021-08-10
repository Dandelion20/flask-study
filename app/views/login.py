"""
登录、注册、退出的视图函数
"""

from flask.views import View
from flask import flash, redirect, render_template, url_for,request
from werkzeug.urls import url_parse
from flask_login import current_user,login_user,logout_user

# 引入用户登录表单
from app.controller.forms import LoginForm,RegistrationForm


from ..exts import db,loginmanager
from ..models.User import User

# 编写user_loader回调函数,用于从数据库加载用户信息，此函数将会被Flask-Login扩展使用
@loginmanager.user_loader
def load_user(id):
    """加载用户信息回调,以主键在数据库中搜索用户,返回主键对应的行"""
    return User.query.get(int(id))

# 登录视图类
class LoginView(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        # 若全局变量中已存在解析出的用户信息，且用户已验证通过，则直接跳转至首页（检验用户是否登录，若登录则跳转到首页）
        # current_user 是flask_login扩展提供的一个代理对象，视图和模板均能访问
        if current_user.is_authenticated:
            return redirect(url_for('index'))

        # 加载登录Form表单
        form = LoginForm()
        # 登录Form表单提交验证通过，跳转至首页
        if form.validate_on_submit():
            # 根据用户名查询本地用户信息
            user = User.query.filter_by(username=form.username.data).first()
            print(user)
            # 用户不存在或密码校验失败，增加闪现消息，并重定向到登录页
            if not user or not user.check_password(form.password.data):
                print(user.check_password(form.password.data))
                flash('用户名或密码有误')
                return redirect(url_for('login'))

            # 用户校验通过，进行用户登录，并重定向到首页
            login_user(user, remember=form.remember_me.data)
            # 实现next的重定向处理
            next_page = request.args.get('next', '')
            if not next_page or not url_parse(next_page).decode_netloc():
                next_page = url_for('index')
            return redirect(next_page)

        # GET请求，直接展示登录页面
        return render_template('login/login.html', title='登录', form=form)

# 登出视图类
class LogoutView(View):
    methods = ['GET']

    def dispatch_request(self):
        logout_user()
        return redirect(url_for('index'))

class RegisterView(View):
    methods = ['GET', 'POST']

    def dispatch_request(self):
        if current_user.is_authenticated:
            return url_for('index')

        form = RegistrationForm()
        # 校验成功，创建用户信息，跳转至登录页面
        print(form.validate_on_submit())
        if form.validate_on_submit():
            user = User(username=form.username.data, email=form.email.data)
            user.set_password(form.password.data)
            print(user)
            db.session.add(user)
            db.session.commit()
            flash('祝贺，你现在已成为一个注册用户！')
            return redirect(url_for('login'))

        return render_template('login/register.html', title='注册', form=form)
