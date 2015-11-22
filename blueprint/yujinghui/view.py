# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'yujinghui'

from flask import Blueprint, render_template, request, redirect, url_for, session, g
from functools import wraps
from traceback import format_exc

yujinghui = Blueprint('yujinghui', __name__, static_url_path="/yujinghui/static",
                      static_folder="static/",
                      template_folder='templates/')

from dataPersist.models import Resume, Education, Work
from traceback import format_exc


def isAuth(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session['user']:
            return f(*args, **kwargs)

    return decorated_function


@yujinghui.route('/yujinghui', methods=['GET', ])
def resume():
    try:
        resu = Resume.query.filter(Resume.realName == "于敬晖").first()
        educ = Education.query.filter(Education.uid == resu.id).all()
        work = Work.query.filter(Work.uid == resu.id).all()
        return render_template("yujinghui.html", resu=resu, educ=enumerate(educ), work=enumerate(work))
    except:
        print format_exc()


@yujinghui.route('/commUI', methods=['GET', ])
def commUI():
    try:
        return render_template("command.html")
    except:
        print format_exc()


@yujinghui.route('/exeComm', methods=['POST', ])
def exeComm():
    try:
        comm = request.form['commands']
        return comm
    except:
        print format_exc()


@isAuth
@yujinghui.route('/modify', methods=['POST', 'GET'])
def modify():
    try:
        return "modify"
    except KeyError:
        print format_exc()
        return redirect(url_for('Resume.index'))
