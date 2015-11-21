# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'yujinghui'

from flask import Blueprint, render_template

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
        print resu.realName
        return render_template("yujinghui.html", resu=resu, educ=enumerate(educ), work=enumerate(work))
    except:
        print format_exc()
