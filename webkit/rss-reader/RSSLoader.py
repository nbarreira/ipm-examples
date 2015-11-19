#!/usr/bin/env python
# --*-- coding: utf-8 --*--

import feedparser
import os
import urllib
from threading import Thread

class RSSLoader(Thread):

    def __init__(self, listener, ignore_cache=False):
        Thread.__init__(self)
        self._listener = listener
        self._ignore_cache = ignore_cache

    def run(self):
        # Retreive and parse feed from a remote URL
        # If not in cache
        CACHE_DIR = 'cache'
        if not os.path.exists(CACHE_DIR):
            os.makedirs(CACHE_DIR)
        filename = os.path.join(CACHE_DIR, "xkcd-rss.xml")
        cached = False
        try:
            with open(filename) as f: cached = True
        except IOError as e:
            cached = False
        if self._ignore_cache or not(cached):
            (filename, headers) = urllib.urlretrieve('http://xkcd.com/rss.xml', filename)
        feed = feedparser.parse(filename)
        # Notify observer
        self._listener.update_feed(feed.feed.title, feed.entries)

