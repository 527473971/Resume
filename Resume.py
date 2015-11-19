from flask import Flask

from blueprint.yujinghui.view import yujinghui
from blueprint.zhengyinghao.view import zhengyinghao

app = Flask(__name__, static_folder='static')

app.register_blueprint(yujinghui, url_prefix='/yujinghui')
app.register_blueprint(zhengyinghao, url_prefix='/zhengyinghao')

app.jinja_env.variable_start_string = '{{ '

app.jinja_env.variable_end_string = ' }}'

@app.before_request
def user_interceptor(exception=None):
    print "interceptor end..."


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9007)
