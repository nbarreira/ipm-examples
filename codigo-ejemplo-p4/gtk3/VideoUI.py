#!/usr/bin/env python

#import pygtk
#import gtk, gobject

from gi.repository import Gtk, GObject, GdkPixbuf, WebKit
import StringIO, Image



class VideoUI():

  def __init__(self, controller):
    
    # Widgets    
    self.win = Gtk.Window()
    self.win.set_title("Lazy video player")
    self.win.resize(800,400)
    
    hbox = Gtk.Box()
    self.win.add(hbox)
    self.webcam_display = Gtk.Image()
    hbox.pack_start(self.webcam_display, False, False, 0)
    scrolledWin = Gtk.ScrolledWindow()
    self.webview = WebKit.WebView()
    scrolledWin.add(self.webview)
    hbox.pack_start(scrolledWin, True, True, 0)

    # Signals
    self.win.connect("delete-event", controller.quit)
    
    
  def display_frame(self, img):
    # A very-very complex way to convert an OpenCV image to a Gtk Image
    # Do not ask! 
    image = Image.fromarray(img, 'RGB')
    buff = StringIO.StringIO()
    image.save(buff, 'ppm')
    contents =  buff.getvalue()
    buff.close()
    loader = GdkPixbuf.PixbufLoader.new_with_type('pnm')
    loader.write(contents)
    pixbuf = loader.get_pixbuf()
    loader.close()
    self.webcam_display.set_from_pixbuf(pixbuf)


  def clicked_button(self, index, count):
    # IMPORTANT: ANY CALL TO A WEBKIT FUNCTION SHOULD BE MADE INSIDE THE
    # GOBJECT.IDLE_ADD FUNCTION. OTHERWISE, IT WILL NOT WORK!!!
    GObject.idle_add(self.webview.load_html_string,
        "<h1>Pulsado boton virtual {i} en {n} ocasiones</h1>".format(i=index, n=count), 
        "file:///")
    
  def start(self):
    self.win.show_all()
    Gtk.main()
    
    
  def quit(self):
    Gtk.main_quit()


