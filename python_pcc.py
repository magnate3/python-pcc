#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import subprocess
import threading
import frr_parser
import linkstate_sockcli
import segmentlist_socksrv


def ls_socket():
    '''socket of linkstate'''

    while True:
        cmd = 'sudo vtysh -c "show ip ospf database opaque-area"'
        opaque_area = subprocess.check_output(cmd, shell=True)

        linkstate = frr_parser.parse(opaque_area)
        linkstate_sockcli.lsocket(linkstate)
        time.sleep(1)

    return


def sl_socket():
    '''socket of segmentlist'''

    segment_lists = segmentlist_socksrv.ssocket()

    return


def main():
    '''simple pcc for FRRouting'''

    # send linkstate
    thread_ls = threading.Thread(target=ls_socket)
    # receive segment list
    thread_sl = threading.Thread(target=sl_socket)

    thread_ls.start()
    thread_sl.start()

    return 0


if __name__ == '__main__':
    main()
