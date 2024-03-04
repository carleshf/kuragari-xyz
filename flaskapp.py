#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf-8

from flask import Flask, redirect, request, render_template

from datetime import datetime

data_path = 'C:/Users/carle/Documents/GitHub/kuragari-xyz/data'

#from data import plays_loader, main_language, alternative_languages, same_colection, create_rows_plays, events_loader
from data import load_labels, load_modules, load_events, get_lang, set_lang, labels_lang

app = Flask( __name__ )

#plys = plays_loader()
#evts = events_loader()

lbls = load_labels( data_path )
mdls = load_modules( data_path )
evts = load_events( data_path )


@app.context_processor
def inject_now():
    return { 'now': datetime.utcnow() }


@app.route( '/language' )
def language():
    lang  = request.args.get( 'lang', default = get_lang(), type = str )
    set_lang( lang )
    return redirect( '/catalogue', code = 302 )


@app.route( '/' )
@app.route( '/catalogue' )
def catalogue():
    #return render_template( 'index.html', data = { 'plays': plys[ main_language ], 'collections': list( set( [ x[ 'collection' ] for x in plys[ main_language ] ] ) ) } )
    return render_template( 'index.html', labels = labels_lang( lbls, get_lang() ), mdls = [] ) # mdls = create_rows_plays( plys[ main_language ], 3 ) )
  

@app.route( '/module' )
def module():
    return "patata"
    """
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
    """

@app.route( '/events' )
def events():
    return render_template( 'events.html', labels = labels_lang( lbls, get_lang() ), events = evts )

if __name__ == '__main__':
    app.run()
