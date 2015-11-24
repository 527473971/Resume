# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'yujinghui'

from flask import Blueprint, render_template, request, redirect, url_for, session, jsonify
from functools import wraps
from traceback import format_exc

member = Blueprint('member', __name__, static_url_path="/yujinghui/static",
                      static_folder="static/",
                      template_folder='templates/')

from dataPersist.models import Resume, Education, Work
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
def resume(myDomain):
    print myDomain
    try:
        resu = Resume.query.filter(Resume.myDomain == myDomain).first()
        educ = Education.query.filter(Education.uid == resu.id).all()
        work = Work.query.filter(Work.uid == resu.id).all()
        return render_template("member.html", resu=resu, educ=enumerate(educ), work=enumerate(work))
    except:
        print format_exc()