#!/usr/bin/env python
# -*- coding:utf-8 -*-

import socket
import json
import iproute2_apply

BUFSIZE = 4096


class ServAttr:
    def __init__(self):
        self.ip = ''
        self.port = 0


def ssocket(request):
    '''Socket of segment list'''

    serv = ServAttr()
    serv.ip = '172.16.1.254'
    serv.port = 55384

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((serv.ip, serv.port))
    # Send request (Source and Destination Address set)
    s.send(json.dumps(request))

    # Receive sl_info (Source and Destination, Nexthop Address, Segment list)
    sl_info = ''
    while True:
        data = s.recv(BUFSIZE)
        if not data:
            iproute2_apply.ip_route(json.loads(sl_info))
            break
        sl_info += data
    s.close()

    return
