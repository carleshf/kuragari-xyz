#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf-8

import os
import json
from datetime import datetime

__events_file__ = 'data.json'

def load( data_path ):
    with open( os.path.join( data_path, 'events', __events_file__ ), 'r', encoding = 'utf-8' ) as fr:
        cnt = json.load( fr )
    cnt = sorted( cnt, key = lambda x: x[ 'order_date' ] )[ ::-1 ]
    for ii in range( len( cnt ) ):
        cnt[ ii ][ 'event' ][ 'slug' ] = 's' + '-'.join( cnt[ ii ][ 'event' ][ 'title' ].strip().split() )
        for jj in range( len( cnt[ ii ][ 'content' ] ) ):
            cnt[ ii ][ 'content' ][ jj ][ 'date' ] = datetime.strptime( cnt[ ii ][ 'content' ][ jj ][ 'date' ], '%Y-%m-%dT%H:%M' )
        cnt[ ii ][ 'content' ] = sorted( cnt[ ii ][ 'content' ], key = lambda x: x[ 'date' ] )[ ::-1 ]
        for jj in range( len( cnt[ ii ][ 'content' ] ) ):
            if cnt[ ii ][ 'content' ][ jj ][ 'date' ].strftime( '%H:%M' ) == '00:00':
                cnt[ ii ][ 'content' ][ jj ][ 'date' ] = cnt[ ii ][ 'content' ][ jj ][ 'date' ].strftime( "%Y-%m-%d" )
            else:
                cnt[ ii ][ 'content' ][ jj ][ 'date' ] = cnt[ ii ][ 'content' ][ jj ][ 'date' ].strftime( "%Y-%m-%d, %H:%M" )
    return cnt