#!/usr/bin/env python
# --*-- coding: utf-8 --*--

from gi.repository import Gtk, GLib, GObject
import datetime

import couchdb
import CouchDBDAO
import threading
import calendar


database = 'calendar'


class CalendarWin(Gtk.Window):

  def __init__(self, db):
    Gtk.Window.__init__(self, title="Calendar-Gtk")
    self.resize(640, 200);

    self.create_widgets()
    self.connect_signals()
    self.dao = CouchDBDAO.CouchDBDAO(db)
    
    self.on_calendar_month_changed(None)

    self.show_all()  
    
  
  
  
  def create_widgets(self):

    hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
    self.add(hbox)

    self.calendar = Gtk.Calendar()    
    hbox.pack_start(self.calendar, False, False, 10)
    
    self.label = Gtk.Label()
    hbox.pack_start(self.label, False, False, 10)
           

  def connect_signals(self):      
    self.connect("delete-event", Gtk.main_quit)
    self.calendar.connect("month-changed",self.on_calendar_month_changed)
    self.calendar.connect("day-selected-double-click", self.on_calendar_day_selected_double_click)
    
    
    
  def on_calendar_month_changed(self, args):
      self.calendar.clear_marks()
      [yy,mm,dd] =  self.calendar.get_date()

      startdate = datetime.datetime(yy,mm+1,1)
      enddate = datetime.datetime(yy,mm+1,calendar.monthrange(yy, mm+1)[1])

      thread = threading.Thread(target=self.findEventsByMonth, args=(startdate, enddate) )
      thread.start()


  def on_calendar_day_selected_double_click(self, args):
    [yy,mm,dd] =  self.calendar.get_date()
    date = datetime.datetime(yy,mm+1,dd)  
    thread = threading.Thread(target=self.findEventsByDate, args=(date,) )
    thread.start()



  def findEventsByMonth(self, startdate, enddate):
      sd = startdate.strftime('%Y-%m-%d')
      ed = enddate.strftime('%Y-%m-%d')
      events = self.dao.findEventsByPeriod(sd, ed)
      GObject.idle_add(self.mark_events, events)


  def mark_events(self, events):
    for date in events:
        d = datetime.datetime.strptime(date,'%Y-%m-%d')
        self.calendar.mark_day(d.day)
        

  def findEventsByDate(self, date):
      d = date.strftime('%Y-%m-%d')
      events = self.dao.findEventsByDate(d)
      GObject.idle_add(self.show_events, d, events)
      
      
  def show_events(self, date, events):
    s = "<b>Eventos " + date + ": </b>\n"
    for e in events:
        s = s + '<i>Descripción</i> {desc}\n<i>Creador</i>\t{creator}\n<i>Etiquetas</i>\t{tags}\n\n'.format(desc=e['description'].encode('utf8'),
                creator=e['creator'].encode('utf8'),
                tags= ', '.join(map(lambda tag: tag.encode('utf8'), e['tags'])))
   
    self.label.set_markup(s)   
      
if __name__ == '__main__':
  GLib.threads_init()  
  s = couchdb.Server()
  db = s[database]
  calendarWin = CalendarWin(db)
  Gtk.main()
