# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'yujinghui'

from flask import Blueprint, render_template, request

yujinghui = Blueprint('yujinghui', __name__, static_url_path="/yujinghui/static",
                      static_folder="static/",
                      template_folder='templates/')

from dataPersist.models import Resume, Education, Work
from traceback import format_exc


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
        print "the command from terminal", comm
        return comm
    except:
        print format_exc()

