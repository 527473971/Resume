#!/usr/bin/env python
# -*- coding: utf-8 -*-



from dbpool import dataConnectionPool
from traceback import format_exc


class CHAR(object):
    def __init__(self, length):
        pass


class VARCHAR(object):
    def __init__(self, length):
        pass


class INT(object):
    def __init__(self, length):
        pass

    def __repr__(self):
        return "INT"


class BaseModel(object):
    pool = dataConnectionPool
    __tablename__ = "your table name"

    def __init__(self):
        self.__sql__ = ""
        self.__columns__ = ''

    # 不能单独使用,后面一定要接上where
    def select(self, *args):
        self.__sql__ = '''select {} from {}'''.format(",".join(args), self.__tablename__)
        self.__columns__ = self.__selfDefinedAttr__ if args == ('*',) else args
        self.__sqltype__ = "select"
        return self

    # 不能单独使用,where
    def update(self, **kwargs):
        columnName = ','.join(["{} = {}".format(key, kwargs[key])
                               if isinstance(getattr(self, key), INT)
                               else "{} = '{}'".format(key, kwargs[key]) for key in kwargs.keys()])
        self.__sql__ = '''update {} set {}'''.format(self.__tablename__, columnName)
        self.__sqltype__ = "update"
        return self

    def where(self, **kwargs):
        condition_tuple = ["{} = {}".format(key, kwargs[key]) if kwargs[key] and isinstance(getattr(self, key),
                                                                                            INT) else "{} = '{}'".format(
            key, kwargs[key]) for key in kwargs.keys()]
        if self.__sql__:
            if len(condition_tuple) > 0:
                self.__sql__ = "{} where {}".format(self.__sql__, "and ".join(condition_tuple))
            print "where :", self.__sql__
            con = self.pool.getConn()
            try:
                cur = con.cursor()
                res = cur.execute(self.__sql__)
                if self.__sqltype__ == "select":
                    ress = cur.fetchall()
                    resumes = list()
                    for res in ress:
                        tmp = type(self.__tablename__, (), {})()
                        print self.__columns__
                        for i, column in enumerate(self.__columns__):
                            setattr(tmp, column, res[i])
                            print '====>', column, res[i]
                        resumes.append(tmp)
                    return resumes
                elif self.__sqltype__ == "update":
                    con.commit()
                    return res
            except:
                print format_exc()
            finally:
                self.pool.release(con)
            return self
        else:
            raise Exception("sql是空得")

    def insert(self, **kwargs):
        self.__sqltype__ = "insert"
        columns, values = [], []
        for key in kwargs.keys():
            columns.append(key)
            if isinstance(getattr(self, key), INT):
                values.append(kwargs[key])
            else:
                values.append("'{}'".format(kwargs[key]))
        self.__sql__ = '''insert into {}({}) values({})'''. \
            format(self.__tablename__, ','.join(columns), ','.join(values))
        print self.__sql__
        try:
            con = self.pool.getConn()
            cur = con.cursor()
            res = cur.execute(self.__sql__)
            con.commit()
            return res
        except:
            print format_exc()
        finally:
            self.pool.release(con)


# 类名要和__tablename__ 保持一致,属性名和数据库字段也要保持一致
class resume(BaseModel):
    __tablename__ = 'resume'
    # 这里需要能够动态生成才行啊,我勒个去的啊
    __selfDefinedAttr__ = ('id', 'realName', 'sex', 'intro', 'username', 'password')

    id = INT(11)
    realName = VARCHAR(30)
    sex = CHAR(1)
    intro = VARCHAR(50)
    username = VARCHAR(30)
    password = CHAR(32)
    myDomain = VARCHAR(30)


class education(BaseModel):
    __tablename__ = 'education'
    __selfDefinedAttr__ = ('id', 'uid', 'school', 'major', 'timeRange',)
    id = INT(11)
    uid = INT(11)
    school = VARCHAR(11)
    major = VARCHAR(11)
    timeRange = VARCHAR(13)


class work(BaseModel):
    __tablename__ = 'work'
    __selfDefinedAttr__ = ('id', 'uid', 'corpName', 'vocation', 'timeRange',)
    id = INT(11)
    uid = INT(11)
    corpName = VARCHAR(11)
    vocation = VARCHAR(11)
    timeRange = VARCHAR(13)


'''
    使用方法如下
    # re = resume()
    # res = re.update(username="jinghuiace@gmail.com").where(id=1)
    # res = re.select("username").where(id=1)
    # res = re.insert(username="zhengyinghao@gmail.com", password="helloworld", realName='郑英豪')
'''
