#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import json
import yaml
from collections import OrderedDict


def priprosessor(out):
    '''shaping LSDB'''

    s1 = re.sub(r'\s*OSPF Router with ID \(.*\)', '', out)
    s2 = re.sub(r'\s*Area-Local Opaque-LSA \(Area.*', '', s1)
    s3 = s2.replace('  Opaque-Type ', '\n  Opaque-Type: ')
    s4 = s3.replace('Opaque-ID  ', 'Opaque-ID:')
    s5 = s4.replace('MT-ID:', 'MT-ID: ')
    s6 = re.sub(r' : .*', '', s5)
    s7 = re.sub('\n\n', '', s6)
    s8 = re.sub('  LS age', '\n\n  LS age', s7)
    s9 = re.sub('(LS Seq Number: )', '\\1  0x', s8)
    s10 = s9.replace('  ', '')
    s11 = re.sub('\(.*?\)', '', s10)
    s12 = re.sub(': Length', ':\n\tLength:', s11)
    s13 = re.sub(',', '\n', s12)
    s14 = re.sub('\[([0246])\]', '\t\\1', s13)
    s15 = re.sub('\[([1357])\]', '\\1', s14)
    s16 = re.sub('#', 'Local Interface IP Addresses:\n\t', s15)
    s17 = re.sub(' \n', '\n', s16)
    s18 = re.sub('(Algorithm [0-9]:)', '\t\\1', s17)
    s19 = re.sub('\n(.*?) =', '\n\t\\1:', s18)
    s20 = re.sub('(Segment Routing MSD TLV)', '\n\\1', s19)
    s21 = re.sub('\n\n', '', s20, 1)
    fixed_out = '---\n' + s21

    return fixed_out


def yaml_encoder(data):
    '''encode LSDB to YAML'''

    s1 = data.replace('\n', '\n  ')
    s2 = s1.replace('  LS age', '- LS age')
    s3 = s2.replace('\t', '  - ')

    return s3


def parse(out):
    '''encode LSDB to JSON'''
    # ordered dictionary
    yaml.add_constructor(yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
                         lambda loader, node: OrderedDict(loader.construct_pairs(node)))

    fixed_out = priprosessor(out)
    yaml_data = yaml.load(yaml_encoder(fixed_out))

    return json.dumps(yaml_data, indent=2)
