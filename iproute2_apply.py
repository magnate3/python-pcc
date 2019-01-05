#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import print_function
import sys
import subprocess


def ip_route(sl_info):
    '''Add static route with iproute2'''

    # Can't create policy-based path
    if sl_info['segmentlist'] == 'Unreachable':
        print('[Segment list: Error] Cannot create segmentlist from {} to {}.'.format(sl_info['src'], sl_info['dst']), file=sys.stderr)
        return -1

    delcmd = 'sudo ip route del ' + sl_info['dst']
    subprocess.call(delcmd, shell=True)
    addcmd = 'sudo ip route add ' + \
        sl_info['dst'] + ' encap mpls ' + \
        sl_info['segmentlist'] + ' via ' + sl_info['nexthop']
    subprocess.call(addcmd, shell=True)
    return
