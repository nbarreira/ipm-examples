#!/usr/bin/env python
# --*-- coding: utf-8 --*--

import feedparser
from gi.repository import Gtk, WebKit

def create_articles(entries):
  article='''
    <article>
      <h2>{title}</h2>
      <p class="date">Published on {published}</p>
      <div class="content">
        {content}
      </div>
    </article>'''
  articles = ""
  for e in entries:
    articles = articles + article.format(title=e.title.encode('utf8'), 
             published=e.published.encode('utf8'),
             content=e.description.encode('utf8'))

  return articles

# Crear ventana + widgets

w = Gtk.Window()
scrolledWindow = Gtk.ScrolledWindow()
webview = WebKit.WebView()

scrolledWindow.add(webview)
w.add(scrolledWindow)
w.resize(800,600)

# Cargar feed
feed = feedparser.parse("http://xkcd.com/rss.xml")

# Crear página y rellenar con feed
page = '''
<html>
  <head>
    <style type="text/css">
      h1 {{ background-color: #036; color: white; padding: 15px}}
      h2 {{ color: #036; border-bottom: solid 2px #036;}}
      .content{{ text-align:  center; }}
      .date {{ font-style: italic; }}
    </style>
  </head>
  <body>
    <h1>{rss_title}</h1>
    {articles}
  </body>
</html>
'''.format(rss_title=feed.feed.title, articles=create_articles(feed.entries))

#Cargar página con webkit
webview.load_html_string(page, 'file:///')

w.show_all()
w.connect("delete-event", Gtk.main_quit)
Gtk.main()    


