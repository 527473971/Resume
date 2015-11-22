# !/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
from traceback import format_exc
from flask import Flask, render_template, \
    request, redirect, url_for, session, g
from flask import make_response, stream_with_context
from blueprint.yujinghui.view import yujinghui
from blueprint.zhengyinghao.view import zhengyinghao
from dataPersist.models import Resume
from Utils.Utils import create_validata_code, genMd5
import io

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
        if genMd5(postpassword) == resu.password:
            session['user'] = postName
            print url_for("yujinghui.commUI")
            return redirect(url_for("yujinghui.commUI"))
        else:
            return ""
    except:
        print format_exc()


@app.route("/register", methods=['GET', 'POST'])
def register():
    try:
        if request.method == "POST":
            print request.method
            authcode = request.form['form-verify']
            print '==>', authcode.upper(), session["auth_code"].upper()
            if session["auth_code"].upper() == authcode.upper():
                return "write mysql "
            else:
                return "authcode 有问题"
        else:
            return render_template("register.html")
    except:
        print format_exc()


@app.route("/authCode", methods=['GET',])
def authCode():
    try:
        print "authCode"
        img, auth_code = create_validata_code()
        img_mem = io.BytesIO()
        img.save(img_mem, 'JPEG', quality=95)
        resp = make_response(img_mem.getvalue())
        resp.headers['Content-Type'] = 'image/jpeg'
        session["auth_code"] = auth_code
        print "session.auth_code", session["auth_code"]
        img_mem.close()
        return resp
    except:
        print format_exc()


@app.route("/verify", methods=['GET', 'POST'])
def verify():
    pass


if __name__ == '__main__':
    app.secret_key = 'In0rderToUseSessionKeyisNeed'
    app.run(port=9007)
