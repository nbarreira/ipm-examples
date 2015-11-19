#!/usr/bin/env python
# --*-- coding: utf-8 --*--

from gi.repository import Gtk, WebKit

window = Gtk.Window()

window.set_title("HolaMundo con Webkit!")

window.connect("destroy", Gtk.main_quit)

webview = WebKit.WebView()

# params: html string + base URI
webview.load_html_string("<h1>Hola mundo!</h1>", "file:///")

window.add(webview)

window.show_all()

Gtk.main() 
