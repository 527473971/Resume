from flask import Flask
from blueprint.yujinghui.view import yujinghui
from blueprint.zhengyinghao.view import zhengyinghao

app = Flask(__name__, static_folder='static', static_path='/static')

app.register_blueprint(yujinghui)
app.register_blueprint(zhengyinghao)

app.jinja_env.variable_start_string = '{{ '

app.jinja_env.variable_end_string = ' }}'

@app.before_request
def user_interceptor(exception=None):
    print "interceptor end..."

@app.route('/', methods = ['GET',])
def index():
    return "this is a homepage about resume"

if __name__ == '__main__':
    app.run(port=9007)
