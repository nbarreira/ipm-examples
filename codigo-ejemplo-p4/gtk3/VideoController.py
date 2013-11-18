#!/usr/bin/env python

from VideoCapture import VideoCapture
from VideoUI import VideoUI

from datetime import datetime

from gi.repository import GObject
GObject.threads_init()

class VideoController():

  def __init__(self):

    # roi = region of interest: array with the coordinates of the virtual buttons on the image
    # TODO: Add new virtual bottoms by selecting new regions on the frame! 
    roi = [ (0,0, 50, 50)]
    
    self._capture_from_webcam = True

    self._view = VideoUI(self)
    self._capture = VideoCapture(self, roi)

    # Store the time where the last click was performed in each virtual button
    self.last_click = [0]
    
    # EXAMPLE
    # Store the number of clicks performed in each virtual button
    self.click_counter = [0]
    
  
  def start(self):
    self._capture.start()    
    self._view.start()
      
  
  def is_capture_enabled(self):
    return self._capture_from_webcam
    
    
  def display_frame(self, frame):
    GObject.idle_add(self._view.display_frame, frame)
    
       
  def on_click_virtual_button(self, index):    

    now = datetime.now()
    if self.last_click[index] == 0 or self._is_a_new_click(self.last_click[index], now):       
       self.last_click[index] = now
       
       # TODO: manage the click!
  
       # EXAMPLE: display the number of clicks in the View    
       self.click_counter[index] = self.click_counter[index] + 1
       self._view.clicked_button(index, self.click_counter[index])
    else:
      print "Click virtual button {i} discarded".format(i=index)
      pass

  
  def quit(self, arg1, arg2):  
    print "exit!"
    self._capture_from_webcam = False
    GObject.idle_add(self._view.quit)
    
    
  def _is_a_new_click(self, t1, t2):
    # Discard clicks very close in time (< 2 seconds)
    # TODO: Adjust this function as you wish
    c = t2 - t1
    if c.seconds > 1:
      return True
    else:
      return False
  
