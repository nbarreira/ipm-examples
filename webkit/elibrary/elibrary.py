#!/usr/bin/python

from gi.repository import Gtk, WebKit
import json
import os
import templates

DIR = os.path.abspath(__file__)

class Library(object):
    
    def __init__(self):        
        self.filename = "database.json"
        
    def find_books(self):
        books = []
        with open(self.filename) as f:
            books = json.load(f)
        return books
        
class UIView(object):
    
    def __init__(self):
        
        builder = Gtk.Builder()
        builder.add_from_file("elibrary.glade")
        self.window = builder.get_object("window1")
        scrolledWindow = builder.get_object("scrolledwindow1")
        self.webview = WebKit.WebView()
        scrolledWindow.add(self.webview)
        self.books = []
        builder.connect_signals(self)
        self.webview.connect("navigation-requested", self.on_click_link)
        


    def run(self):
        self.load_books()
        self.window.show_all()
        Gtk.main()
        
        
    def gtk_main_quit(self, arg1,arg2):
        Gtk.main_quit()
        
        
    def load_books(self):            
        page = templates.page["table"].format(
                library = "\n".join( 
                    [ templates.item["table"].format(
                        bookId=b['id'],
                        image=b['cover'],
                        title=b['title'],
                        author=b['author'],
                        editorial=b['editorial'],
                        year=b['year'],
                        synopsis=b['synopsis']) for b in self.books ] )
                )
        self.webview.load_html_string(page, 'file://' + DIR)
            
    def set_books(self, books):
        self.books = books
        
    def on_checkmenuitem1_toggled(self, view):
        self.webview.execute_script("toggle_images();");

    def on_click_link(self, webview, frame, request):
        uri = request.get_uri()
        if uri.find('#') > 0:
            bookId = uri[uri.find('#')+1:]
            if len(bookId) == 0:
                self.load_books()
            else:
                book = [b for b in self.books if str(b['id']) == bookId]
                if len(book) == 1:
                    page = templates.page["book"].format(
                        bookId=book[0]['id'],
                        image=book[0]['cover'],
                        title=book[0]['title'],
                        author=book[0]['author'],
                        editorial=book[0]['editorial'],
                        year=book[0]['year'],
                        synopsis=book[0]['synopsis'])
                    self.webview.load_html_string(page, 'file://' + DIR)
        return 0
        

class UIController(object):
    
    def __init__(self, library, ui):
        self.library = library
        self.ui = ui
        
        
    def run(self):
        books = self.library.find_books()
        self.ui.set_books(books)
        self.ui.run()


library = Library()
ui = UIView()
controller = UIController(library, ui)
controller.run()
