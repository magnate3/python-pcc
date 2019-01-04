#!/usr/bin/env python
# -*- coding:utf-8 -*-

import subprocess


def ip_route(sl_info):
    '''Add static route with iproute2'''

    delcmd = 'sudo ip route del ' + sl_info['dst']
    subprocess.call(delcmd, shell=True)
    addcmd = 'sudo ip route add ' + \
        sl_info['dst'] + ' encap mpls ' + \
        sl_info['segmentlist'] + ' via ' + sl_info['nexthop']
    subprocess.call(addcmd, shell=True)
    return
