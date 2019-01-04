#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import get_linkstate
import parse_linkstate
import linkstate_sockcli


def main():
    '''Send Linkstate to PCE'''

    while True:
        raw_ls = get_linkstate.get_ls()
        parsed_ls = parse_linkstate.parse_ls(raw_ls)
        linkstate_sockcli.lsocket(parsed_ls)
        time.sleep(1)

    return 0


if __name__ == '__main__':
    main()
