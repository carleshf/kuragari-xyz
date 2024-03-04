#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf-8

from flask import Flask 
from flask import request
from flask import render_template

from datetime import datetime

from data import plays_loader, main_language, alternative_languages, same_colection, create_rows_plays, events_loader

app = Flask( __name__ )
plys = plays_loader()
evts = events_loader()




@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

@app.route( '/' )
@app.route( '/modules' )
def hello():
  #return render_template( 'index.html', data = { 'plays': plys[ main_language ], 'collections': list( set( [ x[ 'collection' ] for x in plys[ main_language ] ] ) ) } )
  return render_template( 'index.html', plays =  create_rows_plays( plys[ main_language ], 3 ) )

@app.route( '/module' )
def module():
  lang  = request.args.get( 'lang', default = main_language, type = str )
  lang  = lang if lang in plys.keys() else None
  if lang is not None:
    slug = list( set( [ x[ 'slug' ] for x in plys[ lang ] ] ) )
  else:
    slug = list( set( [ x[ 'slug' ] for x in plys[ main_language ] ] ) )
  title = request.args.get( 'title', default = '*', type = str )
  title = title if title in slug else None
  if lang is not None and title is not None:
    ply = [ x for x in plys[ lang ] if x[ 'slug' ] == title ][ 0 ]
    alt_lang = alternative_languages( ply[ 'global_slug' ], lang, plys )
    same_col = same_colection( ply[ 'global_slug' ], lang, plys )
    return render_template( 'module.html', is_error = False, ply = ply, alternative_languages = alt_lang, are_other = len( same_col ) != 0, same_collection = same_col )
  else:
    return render_template( 'module.html', is_error = True,  ply = {},  alternative_languages = [],       are_other = 0,                    same_collection = [] )


@app.route( '/events' )
def events():
  return render_template( 'events.html', events = evts )

if __name__ == '__main__':
    app.run()
