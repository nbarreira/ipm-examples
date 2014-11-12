from gi.repository import Gtk, Gio, GObject, Gdk, WebKit
import requests
import threading
import os
import templates

#SERVER = "http://localhost:5000"
SERVER = "http://ipm-movie-database.herokuapp.com"

PATH=os.path.dirname(os.path.realpath(__file__))

class MovieModel(object):

	def __init__(self):		
		pass		
	def get_movies(self, page):
		try:
			data = requests.get(SERVER + "/movies/page/" + str(page))
			response = eval(data.text)
			if response['result'] == 'success':
				return response['data']
			return None	
		except requests.exceptions.ConnectionError:
			return None



class MovieWindow(Gtk.Window):

	def __init__(self, controller):
		self.controller = controller
		Gtk.Window.__init__(self, title="ipm-mdb-webkit")
		self.resize(300,470)
		self.current_page = 1	
		self.create_widgets()  
		self.connect_signals()
		self.show_all()
				
	def create_widgets(self):
		vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		self.add(vbox)

		self.webview = WebKit.WebView()
		scrolled_window = Gtk.ScrolledWindow()
		scrolled_window.add(self.webview)   
		vbox.pack_start(scrolled_window, True, True, 10)
		
		hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
		self.previous = Gtk.Button(stock=Gtk.STOCK_GO_BACK)
		self.next = Gtk.Button(stock=Gtk.STOCK_GO_FORWARD)
		self.execute = Gtk.Button(stock=Gtk.STOCK_EXECUTE)
		self.entry = Gtk.Entry()
		self.entry.set_text(str(self.current_page))
		hbox.pack_start(self.previous, True, False, 0)
		hbox.pack_start(self.entry, True, False, 0)
		hbox.pack_start(self.next, True, False, 0)				
		hbox.pack_start(self.execute, True, False, 0)				
		vbox.pack_start(hbox, False, True, 10)				
		self.statusbar = Gtk.Statusbar()
		vbox.pack_start(self.statusbar, False, False, 0)
		
		
		
	def connect_signals(self):
		self.connect("delete-event", Gtk.main_quit)
		self.next.connect("clicked", self.on_next_button_clicked)
		self.previous.connect("clicked", self.on_previous_button_clicked)
		self.execute.connect("clicked", self.on_execute_button_clicked)
		self.webview.connect("navigation-policy-decision-requested", self.on_navigation_policy_decision_requested)
		

			
	def on_previous_button_clicked(self, arg): # Previous page 
		if self.current_page > 1:
			self.statusbar.push(1, "Loading movies...")
			self.controller.get_movies(self.current_page - 1)
		else:
			self.show_error("Incorrect page")
		
		
	def on_next_button_clicked(self, arg): # Next page
		self.statusbar.push(1, "Loading movies...")
		self.controller.get_movies(self.current_page + 1)

	def on_execute_button_clicked(self, arg): # Execute a script in the webview
		self.webview.execute_script("test()")
		
	def on_navigation_policy_decision_requested(self, webview, frame, request, nav_action, pol_decision):
		print "[PYTHON] Requesting url =>" + nav_action.get_original_uri()
		

	def show_movies(self, movies, page):
		self.current_page = page
		self.entry.set_text(str(self.current_page))
		self.statusbar.pop(1)
		content = templates.page_template.format(
			movies = "\n".join([templates.movie_template.format(
				title = movie['title'],
				year = movie['year'],
				url_image= movie['url_image']) for movie in movies]))		
		self.webview.load_html_string(content, "file://" + PATH + "/")				
		
                
	def show_error(self, msg):
		self.statusbar.pop(1)
		dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR, 	
			Gtk.ButtonsType.CANCEL, "Error")
		dialog.format_secondary_text(msg)
		dialog.run()
		dialog.destroy()		



class MovieController(object):
	def __init__(self):
		self.model = MovieModel()
		self.view = MovieWindow(self)
		self.get_movies(1)

	def get_movies(self, page):
		threading.Thread(target=self._retrieve_movies, args=(page, )).start()
	
	def _retrieve_movies(self, page):
		movies = self.model.get_movies(page)
		if movies:
			GObject.idle_add(self.view.show_movies, movies, page)
		else:
			GObject.idle_add(self.view.show_error, "No more movies")


if __name__ == '__main__':
	GObject.threads_init()
	controller = MovieController()
	Gtk.main()
