# !/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
from traceback import format_exc
from flask import Flask, render_template, request, redirect, url_for, session, g
from blueprint.yujinghui.view import yujinghui
from blueprint.zhengyinghao.view import zhengyinghao
from dataPersist.models import Resume

app = Flask('Resume', template_folder="templates/",
            static_folder="assets/",
            static_path="/assets")

app.register_blueprint(yujinghui)
app.register_blueprint(zhengyinghao)

app.jinja_env.variable_start_string = '{{ '

app.jinja_env.variable_end_string = ' }}'


@app.route("/", methods=['GET'])
def index():
    try:
        return render_template("index.html")
    except:
        print format_exc()


@app.route("/login", methods=['GET', 'POST'])
def login():
    try:
        postName = request.form["form-username"]
        postpassword = request.form["form-password"]
        resu = Resume.query.filter(Resume.userName == postName).first()
        m = hashlib.md5(postpassword)
        if m.hexdigest() == resu.password:
            session['user'] = postName
            return redirect(url_for("yujinghui.commUI"))
        else:
            return ""
    except:
        print format_exc()


if __name__ == '__main__':
    app.secret_key = 'In0rderToUseSessionKeyisNeed'
    app.run(port=9007)
