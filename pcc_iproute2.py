#!/usr/bin/env python
# -*- coding:utf-8 -*-

import subprocess


def ip_route(segment_lists):
    '''add static route'''

    delcmd = 'sudo ip route del ' + segment_lists['to'] 
    subprocess.call(delcmd, shell=True) 
    addcmd = 'sudo ip route add ' + segment_lists['to'] + ' encap mpls ' + segment_lists['segment_list'] + ' via ' + segment_lists['via'] 
    subprocess.call(addcmd, shell=True) 
    return
