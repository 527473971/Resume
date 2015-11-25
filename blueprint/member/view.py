# !/usr/bin/env python
# -*- coding: utf-8 -*-
from dataPersist.db import education, resume, work

__author__ = 'yujinghui'
from flask.ext.login import login_required
from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from functools import wraps
from traceback import format_exc

member = Blueprint('member', __name__, static_url_path="/yujinghui/static",
                   static_folder="static/",
                   template_folder='templates/')

from traceback import format_exc


# 有待修改
def isauth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session['user']:
            return f(*args, **kwargs)

    return decorated_function


@member.route('/commUI', methods=['GET', ])
def commUI():
    try:
        return render_template("command.html")
    except:
        print format_exc()


@member.route('/exeComm', methods=['POST', ])
def exeComm():
    try:
        comm = request.form['commands']
        return comm
    except:
        print format_exc()


@member.route('/<myDomain>', methods=['GET', ])
def resumePage(myDomain):
    try:
        print "myDomain:", myDomain
        resu = resume().select("*").where(myDomain=myDomain)
        educ = education().select("*").where(uid=resu[0].id)
        wrk = work().select("*").where(uid=resu[0].id)
        return render_template("member.html", resu=resu, educ=enumerate(educ), work=enumerate(wrk))
    except:
        print format_exc()

@login_required
@member.route('/setDomain', methods=['POST', ])
def setDomain():
    try:
        dm = request.form[""];
        resu = resume().update(myDomain=dm).where(username=session['user'])
        if resu ==1:
            return jsonify({"status": 1, "msg": "setting domain OK"})
        else:
            return jsonify({"status": 1, "msg": "设置失败请稍后再试"})
    except:
        print format_exc()


@login_required
@member.route('/home/<myDomain>', methods=['POST', ])
def home(myDomain):
    return render_template("register.html")


