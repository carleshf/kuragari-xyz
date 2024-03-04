#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding: utf-8

from .events import load as load_events
from .labels import load as load_labels, labels_lang
from .modules import load as load_modules, display_modules_in_rows, get_module

__language__ = 'es'
__allowed_languages__ = [ 'cat', 'es', 'en' ]


def get_lang():
    return __language__


def set_lang( lang ):
    global __language__
    if lang in __allowed_languages__:
      __language__ = lang
