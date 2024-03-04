#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf-8

import os
import json
from datetime import datetime

__events_file__ = 'data.json'

def load( data_path ):
    return []



""" def create_rows_plays( plays, n ):
  plays = sorted( plays, key = lambda x: int( x[ 'year' ] ) )[ ::-1 ]
  rst = [ [] ]
  ii, jj = 0, 0
  for ply in plays:
    rst[ jj ].append( ply )
    ii += 1
    if ii % n == 0:
      jj += 1
      ii = 0
      rst.append( [] )
  return rst """