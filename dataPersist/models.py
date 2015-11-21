#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dataPersist.db import BaseModel

__author__ = 'yujinghui'
from sqlalchemy import Column
from sqlalchemy.types import Integer, String

class Resume(BaseModel):
    __tablename__ = 'resume'
    id = Column(Integer, primary_key=True)
    realName = Column(String(11))
    sex = Column(String(11))
    intro = Column(String(50))


class Education(BaseModel):
    __tablename__ = 'education'
    id = Column(Integer, primary_key=True)
    uid = Column(Integer)
    school = Column(String(11))
    major = Column(String(11))
    timeRange = Column(String(13))


class Work(BaseModel):
    __tablename__ = 'work'
    id = Column(Integer, primary_key=True)
    uid = Column(Integer)
    corpName = Column(String(11))
    vocation = Column(String(11))
    timeRange = Column(String(13))
