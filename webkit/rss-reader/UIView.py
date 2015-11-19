#!/usr/bin/env python
# --*-- coding: utf-8 --*--

from gi.repository import Gtk, GObject, WebKit

import templates



class UIView(object):

    def __init__(self, controller):
        GObject.threads_init()
        self._controller = controller
        # Create a GTK+ window
        self._w = Gtk.Window()
        self._w.set_title("Example RSS Reader")
        # Terminate the program when the window is closed
        self._w.connect("destroy", controller.on_destroy)

        # Instantiate the WebKit renderer
        self._web_view = WebKit.WebView()
        # Create a scroll area and add the webkit item
        scroll = Gtk.ScrolledWindow()
        scroll.add(self._web_view)

        # Create the actions and the toolbar
        actions = Gtk.ActionGroup("Actions")
        actions.add_actions([
            ("FileMenu", None, "_File", None, None, None),
            ("ViewMenu", None, "_View", None, None, None),
            ("quit", Gtk.STOCK_QUIT, "_Quit", "<ctrl>Q", None, self._controller.on_quit),
            ("reload", Gtk.STOCK_REFRESH, "_Reload", "<ctrl>R", None, self._controller.on_reload)
            ])
        ui_def = """
        <menubar name="menubar_main">
          <menu action="FileMenu">
            <menuitem action="quit" />
          </menu>
          <menu action="ViewMenu">
            <menuitem action="reload" />
          </menu>
        </menubar>
        <toolbar name="toolbar_main">
          <toolitem action="reload" />
        </toolbar>
        """
        mngr = Gtk.UIManager()
        mngr.insert_action_group(actions)
        mngr.add_ui_from_string(ui_def)
        self._w.add_accel_group(mngr.get_accel_group())

        # Add the menubar, toolbar and scrolled renderer to the window
        vb = Gtk.Box(False, orientation = Gtk.Orientation.VERTICAL)
        vb.pack_start(mngr.get_widget("/menubar_main"), False, False, 0)
        vb.pack_start(mngr.get_widget("/toolbar_main"), False, False, 0)
        vb.pack_start(scroll, True, True, 0)
        self._w.add(vb)
        self._w.resize(780, 350)

    def start(self):
        # Turn over control to the GTK+ main loop
        self._w.show_all()
        Gtk.main()

    def finish(self):
        Gtk.main_quit()

    def show_loading(self):
        self._update_web_view(templates.loading_template.format())

    def show_loading2(self):
        self._web_view.execute_script("show_loading();")

    def update_feed(self, title, entries):
        self._web_view.execute_script("hide_loading();")
        self._update_web_view(templates.main_template.format(
            title = title,
            articles = "\n".join([templates.feed_template.format(
                            title = item.title,
                            description= item.description) for item in entries])))


    def _update_web_view(self, content):
        # Load html into the renderer
        self._web_view.load_html_string(content, "file:///")
