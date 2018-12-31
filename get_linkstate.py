#!/usr/bin/env python
# -*- coding:utf-8 -*-

import subprocess

def get_ls():
    '''get Linkstate from FRRouting LSDB'''

    cmd = 'sudo vtysh -c "show ip ospf database opaque-area"'
    raw_ls = subprocess.check_output(cmd, shell=True)

    return raw_ls
