#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import threading
import get_linkstate
import parse_linkstate
import linkstate_sockcli
import segmentlist_socksrv


def ls_socket():
    '''socket of linkstate'''

    while True:
        raw_ls = get_linkstate.get_ls()
        parsed_ls = parse_linkstate.parse_ls(raw_ls)
        linkstate_sockcli.lsocket(parsed_ls)
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
