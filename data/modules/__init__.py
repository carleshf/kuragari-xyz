#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf-8

import os
import json
from datetime import datetime

__modules_file__ = 'data.json'

def _create_full_module_( module ):
    rst = [ ]
    for opt in module[ 'lang_options' ]:
        rst.append( {
                  'global_slug': module[ 'global_slug' ],
            'global_collection': module[ 'global_collection' ],
                         'type': module[ 'type' ],
                       'system': module[ 'system' ],
                         'year': module[ 'year' ],
                     'nplayers': module[ 'nplayers' ],
                        'etime': module[ 'etime' ],
                    'available': opt[ 'available' ],
                        'title': opt[ 'title' ],
                     'subtitle': opt[ 'subtitle' ],
                      'summary': opt[ 'summary' ],
                         'link': opt[ 'link' ],
                    'lang_slug': opt[ 'lang_slug' ],
              'lang_collection': opt[ 'lang_collection' ],
                         'lang': opt[ 'lang' ]
        } )
    return rst

def _create_display_module_( modules, module ):
    coll = [ x for x in modules if module[ 'global_collection' ] is not None and x[ 'global_collection' ] == module[ 'global_collection' ] and x[ 'lang' ] == module[ 'lang' ] ]
    rst = { 
        'module': module,
        'lang': [ { 'lang': x[ 'lang' ], 'lang_slug': x[ 'lang_slug' ], 'available': x[ 'available' ] } for x in modules if x[ 'global_slug' ] == module[ 'global_slug' ] ], # and x[ 'lang' ] != module[ 'lang' ] ],
        'collection': [ { 'title': x[ 'title' ], 'year': x[ 'year' ], 'lang_slug': x[ 'lang_slug' ] } for x in coll if x [ 'lang_slug' ] != module[ 'lang_slug' ] ]
    }
    rst[ 'lang' ].sort( key = lambda x: x[ 'lang' ] )
    return rst

def load( data_path ):
    with open( os.path.join( data_path, 'modules', __modules_file__ ), 'r', encoding = 'utf-8' ) as fr:
        cnt = json.load( fr )
    rst = [ ]
    for x in cnt:
        rst += _create_full_module_( x )
    rst = sorted( rst, key = lambda x: int( x[ 'year' ] ) )[ ::-1 ]
    return rst


def display_modules_in_rows( modules, n, lang ):
    rst = [ [ ] ]
    ii, jj = 0, 0
    for mod in modules:
        if mod[ 'lang' ] == lang:
            rst[ jj ].append( mod )
            ii += 1
            if ii % n == 0:
                jj += 1
                ii = 0
                rst.append( [] )
    return rst


def get_module( modules, lang_slug ):
    rst = None
    for mod in modules:
        if mod[ 'lang_slug' ] == lang_slug:
            rst = mod
            break
    if rst is not None:
        x = _create_display_module_( modules, rst )
        return x
    else:
        return { }