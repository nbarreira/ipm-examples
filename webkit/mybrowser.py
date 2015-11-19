#!/usr/bin/env python
# --*-- coding: utf-8 --*--

from gi.repository import Gtk, WebKit

# TO DO: 
#  - Historial
#  - Bookmarks
#  - Descargas
#  - Atras/adelante
#  - ...

class MyBrowser(Gtk.Window):

  def __init__(self):
    Gtk.Window.__init__(self, title="MyBrowser")
    self.resize(800,600)
    
    self.create_widgets()  
    self.connect_signals()
    
    
    self.show_all()
    

  def create_widgets(self):
    # Layout vertical para navegador: barra url + navegador + barra progreso
    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
    self.add(vbox)

    # Layout horizontal para caja texto + botones
    hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
    vbox.pack_start(hbox, False, False, 0)
    
    self.uri_entry = Gtk.Entry()
    hbox.pack_start(self.uri_entry, True, True, 10)
    
    self.go_button = Gtk.Button(stock=Gtk.STOCK_OK)    
    hbox.pack_start(self.go_button, False, False, 0)
    self.refresh_button = Gtk.Button(stock=Gtk.STOCK_REFRESH)
    hbox.pack_start(self.refresh_button, False, False, 0)
           
    self.webview = WebKit.WebView()
    scrolled_window = Gtk.ScrolledWindow()
    scrolled_window.add(self.webview)   
    vbox.pack_start(scrolled_window, True, True, 0)
    
    self.progressbar = Gtk.ProgressBar()
    vbox.pack_start(self.progressbar, False, False, 0)
    self.progressbar.set_visible(False)
    
    
  def connect_signals(self):      
    self.connect("delete-event", Gtk.main_quit)

    self.go_button.connect("clicked", self.on_go_button_clicked)
    self.uri_entry.connect("activate", self.on_go_button_clicked)
    self.refresh_button.connect("clicked", self.on_refresh_button_clicked) 
    self.webview.connect("title-changed", self.on_webview_title_changed)
    self.webview.connect("load-started", self.on_webview_load_started)
    self.webview.connect("load-progress-changed", self.on_webview_load_progress_changed)
    self.webview.connect("load-finished", self.on_webview_load_finished)
    
    
    
  def on_go_button_clicked(self, arg):  
    url = self.uri_entry.get_text()
    
    if not url.startswith("http://") and not url.startswith("https://") and not url.startswith("file://"):
      url = "http://" + url
      self.uri_entry.set_text(url)
      
    self.webview.open(url)
    
    
  def on_refresh_button_clicked(self, arg):
    self.webview.reload()
        
  def on_webview_title_changed(self, webview, frame, title):
    self.set_title("MyBrowser: " + title)
    
  def on_webview_load_started(self, webview, frame):
    self.progressbar.set_visible(True)
    
  def on_webview_load_finished(self, webview, frame):
    self.uri_entry.set_text(self.webview.get_uri())
    self.progressbar.set_visible(False)
    
  def on_webview_load_progress_changed(self, webview, amount):
    self.progressbar.set_fraction(amount / 100.0)
 
if __name__ == '__main__':
  browser = MyBrowser()
  Gtk.main()
