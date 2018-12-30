#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
import json

BUFSIZE = 4096


class ServAttr:
    def __init__(self):
        self.ip = ''
        self.port = 0


def ssocket():
    '''socket of segment list'''

    serv = ServAttr()
    serv.ip = '172.16.1.1'
    serv.port = 55384

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((serv.ip, serv.port))
    s.listen(5)
    ret = ''
    while True:
        (conn, addr) = s.accept()
        while True:
            data = conn.recv(BUFSIZE)
            if not data:
    		return json.loads(ret)
                break
            ret += data
        conn.close()
    s.close()

    return json.loads(ret) 