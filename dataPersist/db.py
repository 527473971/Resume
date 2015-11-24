#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dataPersist.dbpool import dataConnectionPool

cfg_info = {
    "dbhost": "localhost",
    "dbport": 3306,
    "dbpasswd": "root",
    "dbuser": "root",
    "dbname": "resume"
}

host = cfg_info['dbhost']
port = cfg_info['dbport']
passwd = cfg_info['dbpasswd']
user = cfg_info['dbuser']
db = cfg_info['dbname']


class BaseModel(object):
    __tableName__ = ""

    @classmethod
    def select(cls, *args):
        sql = '''select * from {}'''.format(cls.__tableName__)

        return ""

    @classmethod
    def filter(cls, **kwars):
        sql = '''where  {}'''.format(cls.__tableName__)
        pass

    @classmethod
    def insert(cls):
        pass

    @classmethod
    def update(cls):
        pass

    @classmethod
    def where(cls):
        pass

class Resume(BaseModel):
    __tableName__ = "resume"

