#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import subprocess
import threading
import frr_parser
import pcc_linkstate
import pcc_segmentlist
import pcc_iproute2


def ls_socket():
    '''socket of linkstate'''

    while True:
        cmd = 'sudo vtysh -c "show ip ospf database opaque-area"'
        opaque_area = subprocess.check_output(cmd, shell=True)

        linkstate = frr_parser.parse(opaque_area)
        pcc_linkstate.lsocket(linkstate)
        time.sleep(1)

    return


def sl_socket():
    '''socket of segmentlist'''

    segment_lists = pcc_segmentlist.ssocket()

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
