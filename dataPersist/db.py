#!/usr/bin/env python
# -*- coding: utf-8 -*-



from dbpool import dataConnectionPool

class FieldException(Exception):
    def __init__(self):
        pass


class BaseModel(object):
    pool = dataConnectionPool

    def __init__(self):
        self.__sql__ = ""

    def select(self, *args):
        self.__sql__ = '''select {} from {}'''.format(",".join(args), self.__tablename__)
        return self

    def filter(self, **kwars):
        if self.__sql__:
            self.__sql__ = self.__sql__
            con = self.pool.getConn()
            cur = con.cursor()
            cur.execute(self.__sql__)
            res = cur.fetchall()
            return self
        else:
            raise FieldException()

        return self

    def insert(self):
        return "OK"

    def update(self, **kwargs):
        return self

    def where(self):
        return "OK"


class Resume(BaseModel):
    __tablename__ = 'resume'

    def __init__(self):
        self.id = ""
        self.realName = ""
        self.sex = ""
        self.intro = ""
        self.userName = ""
        self.password = ''


if __name__ == "__main__":
    re = Resume()
    print re.select("userName", "intro").filter(name="jinghuiace@gmail.com", )
