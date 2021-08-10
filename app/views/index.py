"""
首页视图类
"""
from flask.views import View
from flask import render_template
from flask_login import login_required


class IndexView(View):
    methods = ['GET']
    # 通过login_required装饰器限制该视图只能登录用户访问
    decorators = [login_required]

    def dispatch_request(self):
        posts = [
            {
                'author': {'username': '李白'},
                'body': '举头望明月，低头思故乡'
            },
            {
                'author': {'username': '李清照'},
                'body': '知否，知否，应是绿肥红瘦'
            }
        ]

        return render_template('index/index.html', title='首页', posts=posts)
