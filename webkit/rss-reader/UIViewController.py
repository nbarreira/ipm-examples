#!/usr/bin/env python
# --*-- coding: utf-8 --*--

from gi.repository import GObject
from RSSLoader import RSSLoader
from UIView import UIView

class UIViewController(object):

    def __init__(self):
        self._view = UIView(self)

    def start(self):
        GObject.idle_add(self._view.show_loading)
        self._view.start()

    def update_feed(self, title, entries):
        GObject.idle_add(self._view.update_feed, title, entries)

    def on_reload(self, action):
        GObject.idle_add(self._view.show_loading2)
        RSSLoader(self,ignore_cache=True).start()

    def on_quit(self, action):
        self._quit()

    def on_destroy(self, w):
        self._quit()


    def _quit(self):
        GObject.idle_add(self._view.finish)
