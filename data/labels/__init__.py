#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf-8

import os
import json

__labels_file__ = 'data.json'

def load( data_path ):
    with open( os.path.join( data_path, 'labels', __labels_file__ ), 'r', encoding = 'utf-8' ) as fr:
        cnt = json.load( fr )
    return cnt

def labels_lang( labels, lang ):
    rst = {}
    for key, value in labels.items():
        rst[ key ] = value[ lang ]
    return rst