# !/usr/bin/env python
# -*- coding: utf-8 -*-
from traceback import format_exc
from flask import Flask, render_template, \
    request, session, jsonify
from flask import make_response
from sqlalchemy import Table
from blueprint.member.view import member
from Utils.Utils import create_validata_code, genMd5, sendVerifyEmail
import io
from dataPersist.dbpool import dataConnectionPool

app = Flask('Resume', template_folder="templates/",
            static_folder="assets/",
            static_path="/assets")

app.register_blueprint(member)

app.jinja_env.variable_start_string = '{{ '

app.jinja_env.variable_end_string = ' }}'


@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()

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
        if resu is None:
            return jsonify({"status": 0, "msg": "用户不存在"})
        if genMd5(postpassword) == resu.password:
            session['user'] = postName
            return jsonify({"status": 1, "msg": "登录成功", "nexturl": resu.myDomain})
        else:
            return jsonify({{"status": 0, "msg": "用户或密码错误"}})
    except:
        print format_exc()


@app.route("/register", methods=['GET', 'POST'])
def register():
    try:
        if request.method == "POST":
            print request.method
            authcode = request.form['form-verify']
            email = request.form['form-username']
            password = request.form['form-password']
            name = request.form['form-name']
            print '==>', authcode.upper(), session["auth_code"].upper()
            if session["auth_code"].upper() == authcode.upper():

                registerSuccess = "OK"
                print "registerSuccess", registerSuccess
                if registerSuccess:
                    try:
                        emailUrl = sendVerifyEmail(email)
                        return jsonify({"status": 1,
                                        "msg": "记得去确认" + (
                                            "<a href='" + emailUrl + "'>邮件</a>。" if len(
                                                emailUrl) > 0 else '邮件') + "啊!", "nexturl": "setting"})
                    except:
                        print "send verfiy email fails" + format_exc()
                        return jsonify({"status": 0, "msg": "邮件发送有问题"})

            else:
                return jsonify({"status": 0, "msg": "验证码有问题"})
        else:
            return render_template("register.html")
    except:
        print format_exc()


@app.route("/authCode", methods=['GET', ])
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



@app.route("/setting", methods=['GET', ])
def setting():
    # 对自己的主页进行设置
    try:
        return render_template("setting.html")
    except:
        print format_exc()


if __name__ == '__main__':
    init_db()
    app.secret_key = 'In0rderToUseSessionKeyisNeed'
    app.run(port=9007)
