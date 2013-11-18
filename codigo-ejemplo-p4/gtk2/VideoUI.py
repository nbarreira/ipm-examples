#!/usr/bin/env python

import pygtk
import gtk, gobject, webkit


class VideoUI():

  def __init__(self, controller):
    
    # Widgets    
    self.win = gtk.Window()
    self.win.set_title("Lazy video player")
    self.win.resize(800,400)
    
    hbox = gtk.HBox()
    self.win.add(hbox)
    self.webcam_display = gtk.Image()
    hbox.pack_start(self.webcam_display, False, False, 0)
    scrolledWin = gtk.ScrolledWindow()
    self.webview = webkit.WebView()
    scrolledWin.add(self.webview)
    hbox.pack_start(scrolledWin, True, True, 0)

    # Signals
    self.win.connect("delete-event", controller.quit)
    
    
  def display_frame(self, img):
    # Convert an OpenCV image to a Gtk Image
    pixbuf = gtk.gdk.pixbuf_new_from_array(img, gtk.gdk.COLORSPACE_RGB, 8)
    self.webcam_display.set_from_pixbuf(pixbuf)


  def clicked_button(self, index, count):
    # IMPORTANT: ANY CALL TO A WEBKIT FUNCTION SHOULD BE MADE INSIDE THE
    # GOBJECT.IDLE_ADD FUNCTION. OTHERWISE, IT WILL NOT WORK!!!
    gobject.idle_add(self.webview.load_html_string,
        "<h1>Pulsado boton virtual {i} en {n} ocasiones</h1>".format(i=index, n=count), 
        "file:///")
    
  def start(self):
    self.win.show_all()
    gtk.main()
    
    
  def quit(self):
    gtk.main_quit()


