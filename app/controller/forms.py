"""
创建并编写用户表单文件
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired,Email,EqualTo,ValidationError
from ..models.User import User

# 创建用户登录表单
class LoginForm(FlaskForm):
    # DataRequired：数据不可为空的验证器
    username = StringField('用户名', validators=[DataRequired()])
    password = PasswordField('密码', validators=[DataRequired()])
    remember_me = BooleanField('记住密码', default=False)
    submit = SubmitField('登录')

# 创建用户注册表单
class RegistrationForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired()])
    email = StringField('邮箱', validators=[DataRequired(), Email()])
    password = PasswordField('密码', validators=[DataRequired()])
    password2 = PasswordField('确认密码', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('注册')

    def validate_username(self, username):
        """自定义username验证器 若数据库表中已存在该用户，则报错"""
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('该用户名已被使用')

    def validate_email(self, email):
        """自定义email验证器   若数据库表中已存在该用户，则报错"""
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('该邮箱已被使用')
