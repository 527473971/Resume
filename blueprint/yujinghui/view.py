__author__ = 'yujinghui'

# !/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, abort
from flask import Flask, request, g, redirect, url_for
from jinja2 import TemplateNotFound
import json, random, datetime, threading
from sqlalchemy import or_, between

yujinghui = Blueprint('yujinghui', __name__,
                      template_folder='templates/')

@yujinghui.route('/yujinghui', methods = ['GET',])
def resume():
    print "ensure route"
    return render_template("yujinghui.html")
