#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf-8

from flask import Flask, redirect, request, render_template

from datetime import datetime

data_path = 'C:/Users/carle/Documents/GitHub/kuragari-xyz/data'

from data import load_labels, load_modules, load_events, get_lang, set_lang, labels_lang, display_modules_in_rows, get_module

app = Flask( __name__ )


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
    return render_template( 'index.html', labels = labels_lang( lbls, get_lang() ), plys = display_modules_in_rows( mdls, 3, get_lang() ) )
  

@app.route( '/module' )
def module():
    title = request.args.get( 'title', default = '*', type = str )
    mld = get_module( mdls, title )
    return render_template( 'module.html', labels = labels_lang( lbls, get_lang() ), mld = mld )


@app.route( '/events' )
def events():
    return render_template( 'events.html', labels = labels_lang( lbls, get_lang() ), events = evts )


if __name__ == '__main__':
    app.run()
