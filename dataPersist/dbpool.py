#! /usr/bin/env python
# coding=utf-8
import MySQLdb
import collections
from db import host, user, passwd, db
import logging
import logging.config
import threading


class DataConnectionPool():
    @staticmethod
    def instance():
        if not hasattr(DataConnectionPool, "_instance"):
            DataConnectionPool._instance = DataConnectionPool()
        return DataConnectionPool._instance

    def __init__(self, connNum):
        self.connNUm = connNum
        self.active_conn_queue = collections.deque()
        self.idle_conn_queue = collections.deque()
        self.lock = threading.Lock()
        for i in range(connNum):
            conn = MySQLdb.connect( host=host,
                                    user=user,
                                    passwd=passwd,
                                    db=db,
                                    port=3306)
            self.idle_conn_queue.append(conn)

    def getConn(self):
        with self.lock:
            conn = self.idle_conn_queue.popleft()
            if conn is None:
                print("there si no conn available")
                return None
            self.active_conn_queue.append(conn)
            return conn

    def release(self, conn):
        with self.lock:
            self.active_conn_queue.remove(conn)
            self.idle_conn_queue.append(conn)

    def close(self):
        pass

    def current_active_connections(self):
        return self.active_conn_queue.__len__()

    def current_idle_connections(self):
        return self.idle_conn_queue.__len__()


dataConnectionPool = DataConnectionPool(20)