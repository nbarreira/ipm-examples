#!/usr/bin/env python
# --*-- coding: utf-8 --*--

from UIViewController import UIViewController
from RSSLoader import RSSLoader

# Workaround (https://bugzilla.gnome.org/show_bug.cgi?id=622084)
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

controller = UIViewController()
# Starts in new thread
RSSLoader(controller).start()
# Turns over control to GTK+ main loop
controller.start()
