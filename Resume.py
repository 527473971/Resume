from flask import Flask

from blueprint.yujinghui.view import yujinghui
from blueprint.zhengyinghao.view import zhengyinghao

app = Flask(__name__, static_folder='static', static_path='/activity/static', template_folder='templates')

app.register_blueprint(yujinghui, url_prefix='/yujinghui')
app.register_blueprint(zhengyinghao, url_prefix='/zhengyinghao')

app.jinja_env.variable_start_string = '{{ '

app.jinja_env.variable_end_string = ' }}'

if __name__ == '__main__':
    app.run()
