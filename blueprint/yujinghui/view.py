__author__ = 'yujinghui'

# !/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

yujinghui = Blueprint('yujinghui', __name__,
                      template_folder='templates/')

@yujinghui.route('/yujinghui', methods = ['GET',])
def resume():
    return render_template("yujinghui.html")
