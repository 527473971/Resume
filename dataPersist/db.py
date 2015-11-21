#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


cfg_info = {
    "dbhost": "localhost",
    "dbport": 3306,
    "dbpasswd": "",
    "dbuser": "root",
    "dbname": "myowndemo"
}


host = cfg_info['dbhost']
port = cfg_info['dbport']
passwd = cfg_info['dbpasswd']
user = cfg_info['dbuser']
db = cfg_info['dbname']

link = 'mysql+mysqlconnector://%s:%s@%s:%s/%s?charset=utf8mb4' % (user, passwd, host, port, db)

BaseModel = declarative_base()

engine = create_engine(link, convert_unicode=True, pool_recycle=3600)

db_session = scoped_session(sessionmaker(autocommit=True,
                                         autoflush=False,
                                         bind=engine))
BaseModel.query = db_session.query_property()
