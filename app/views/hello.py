from flask.views import View
from flask import render_template
# 标准类视图:均继承自flask.views.View类
class HelloWorld(View):
    methods = ['GET']
    # 该方法相当于视图函数，所有的逻辑操作都要放在这个里面完成,且也必须要返回一个值，与视图函数的使用相同
    def dispatch_request(self):

        user = {'nickname': 'Super.Wong'}
        posts = [
            {
                'author': {'nickname': '李白'},
                'body': '举头望明月，低头思故乡'
            },
            {
                'author': {'nickname': '李清照'},
                'body': '知否，知否，应是绿肥红瘦'
            }
        ]
        return render_template('hello/hello.html', title='测试', user=user, posts=posts)

