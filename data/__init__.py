#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf-8

import os
import json
import codecs

from datetime import datetime

events_file = '/home/carleshf/kuragari-xyz/data/events/events.json'
content_folder = '/home/carleshf/kuragari-xyz/data/content-lang'
main_language = 'es'


def _load_content( folder_lang ):
  rst = {}
  for lng in os.listdir( folder_lang ):
    if not lng.startswith( '_' ):
      rst[ lng ] = [ ]
      for fle in os.listdir( os.path.join( folder_lang, lng ) ):
        if not fle.startswith( '_' ):
          with open( os.path.join( folder_lang, lng, fle ), 'r' ) as fh:
          #with codecs.open( os.path.join( folder_lang, lng, fle ), encoding = 'utf-8' ) as fh:
            rst[ lng ].append( json.load( fh ) )
  rst[ lng ] = sorted( rst[ lng ], key = lambda x: int( x[ 'year' ] ) )
  return rst

def alternative_languages( slug, current_language, data ):
  rst = []
  for lng in data.keys():
    if lng != current_language:
      for ply in data[ lng ]:
        if slug == ply[ 'global_slug' ]:
          rst.append( ( lng, ply[ 'slug' ] ) )
  return list( set( rst ) )

def same_colection( slug, current_language, data ):
  rst = []
  curr = [ x[ 'collection' ] for x in data[ current_language ] if x[ 'global_slug' ] == slug ][ 0 ]
  print( curr )  
  for ply in data[ current_language ]:
    if ply[ 'collection' ] == curr and ply[ 'global_slug' ] != slug:
      rst.append( ( ply[ 'title' ], ply[ 'slug' ], ply[ 'year' ] ) )
  return rst
  
  
def plays_loader():
  return _load_content( content_folder )

def create_rows_plays( plays, n ):
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
  return rst



def events_loader():
  with open( events_file, 'r' ) as fr:
    cnt = json.load( fr )
  cnt = sorted( cnt, key = lambda x: x[ 'order_date' ] )[ ::-1 ]
  for ii in range( len( cnt ) ):
    cnt[ ii ][ 'event' ][ 'slug' ] = 's' + '-'.join( cnt[ ii ][ 'event' ][ 'title' ].strip().split() )
    for jj in range( len( cnt[ ii ][ 'content' ] ) ):
      cnt[ ii ][ 'content' ][ jj ][ 'date' ] = datetime.strptime( cnt[ ii ][ 'content' ][ jj ][ 'date' ], '%Y-%m-%dT%H:%M' )
    cnt[ ii ][ 'content' ] = sorted( cnt[ ii ][ 'content' ], key = lambda x: x[ 'date' ] )[ ::-1 ]
    for jj in range( len( cnt[ ii ][ 'content' ] ) ):
      if cnt[ ii ][ 'content' ][ jj ][ 'date' ].strftime("%H:%M") == '00:00':
        cnt[ ii ][ 'content' ][ jj ][ 'date' ] = cnt[ ii ][ 'content' ][ jj ][ 'date' ].strftime( "%Y-%m-%d" )
      else:
        cnt[ ii ][ 'content' ][ jj ][ 'date' ] = cnt[ ii ][ 'content' ][ jj ][ 'date' ].strftime( "%Y-%m-%d, %H:%M" )
  return cnt