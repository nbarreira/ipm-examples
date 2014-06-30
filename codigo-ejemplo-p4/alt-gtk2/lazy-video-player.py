#!/usr/bin/env python

import sys
from VideoController import VideoController


if len(sys.argv) > 1:
  vc = VideoController(sys.argv[1])
  vc.start() 
else:
  print "Usage: lazy-video-player.py filename"

