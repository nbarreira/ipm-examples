# /usr/bin/env python
# --*-- coding: utf-8 --*--

from gi.repository import Gtk, GLib, GObject, WebKit
import datetime

import couchdb
import CouchDBDAO
import threading
import calendar
import random


database = 'calendar'


class CalendarWin(Gtk.Window):

  def __init__(self, db):
    Gtk.Window.__init__(self, title="Calendar-Webkit")
    self.resize(640, 340);

    self.create_widgets()
    self.connect_signals()
    self.dao = CouchDBDAO.CouchDBDAO(db)
    
    self.events = []
    self.on_calendar_month_changed(None)

    self.show_all()  
    
  
  
  
  def create_widgets(self):
    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, homogeneous=False)
    
    buttonbox = Gtk.ButtonBox(layout_style= Gtk.ButtonBoxStyle.END)
    self.button = Gtk.Button(stock=Gtk.STOCK_INFO)
    buttonbox.pack_start(self.button, False, False, 10)
    vbox.pack_start(buttonbox, False, False, 10) 

    self.calendar = Gtk.Calendar()    
    vbox.pack_start(self.calendar, False, False, 10)

    hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, homogeneous=False)
    hbox.pack_start(vbox, False, False, 0)

    
    self.webview = WebKit.WebView()
    scrolledWindow = Gtk.ScrolledWindow()
    scrolledWindow.add(self.webview)
    hbox.pack_start(scrolledWindow, True, True, 10)
    self.add(hbox)
           

  def connect_signals(self):      
    self.connect("delete-event", Gtk.main_quit)
    self.calendar.connect("month-changed",self.on_calendar_month_changed)
    self.calendar.connect("day-selected-double-click", self.on_calendar_day_selected_double_click)
    self.button.connect("clicked", self.on_button_clicked)
    
    
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
    self.events = events
    for date in events:
        d = datetime.datetime.strptime(date,'%Y-%m-%d')
        self.calendar.mark_day(d.day)
        

  def findEventsByDate(self, date):
      d = date.strftime('%Y-%m-%d')
      events = self.dao.findEventsByDate(d)
      GObject.idle_add(self.show_events, d, events)
      
      
  def show_events(self, date, events):
    event_page = '''<html>
                <head>
                  <style type="text/css">
                    h1 {{ font-size: 1.2em; }}
                    dl {{ width: 100%; padding-bottom: 0.5em; overflow:hidden; }}
                    dt {{ 
                      font-weight: bold; 
                      width: 48%; 
                      float: left; 
                      text-align: right;
                      padding-right: 2%;
                      }}
                    dd {{ 
                      overflow: hidden;
                      float: left;
                      width: 50%; 
                      padding: 0;
                      margin: 0;
                      }}
                  </style>
                </head>
                <body>
                  <h1>Eventos {current_date}</h1>
                  {events}
                </body>
              </html>'''.format(current_date=date, events=self.get_events(events));
  

    self.webview.load_html_string(event_page, "file:///")   
    
  def get_events(self, events):
      s = ''
      for e in events:
        s = s + '<dl><dt>Descripción</dt><dd>{desc}</dd><dt>Creador</dt><dd>{creator}</dd><dt>Etiquetas</dt><dd>{tags}</dd></dl>'.format(desc=e['description'].encode('utf8'),
                creator=e['creator'].encode('utf8'),
                tags=', '.join(map(lambda tag: tag.encode('utf8'), e['tags'])))
      return s


  def on_button_clicked(self, arg):
    stats_page = '''<html>
<head>
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      google.load("visualization", "1", {{packages:["linechart"]}});
      google.setOnLoadCallback(drawChart);
      function drawChart() {{
        var data = google.visualization.arrayToDataTable([
          ['Día', 'Número de Eventos'],
          {numeventos}
        ]);

        var options = {{
          title: 'Número de eventos por día',
          legend: 'bottom',
          hAxis: {{title: 'Día', titleTextStyle: {{color: 'red'}}}}
        }};

        var chart = new google.visualization.LineChart(document.getElementById('chart_div'));
        chart.draw(data, options);
      }}
    </script>
  </head>
  <body>
    <div id="chart_div" style="width: 340px; height: 300px;"></div>
  </body>
</html>'''.format(numeventos=self.get_num_eventos())
    self.webview.load_html_string(stats_page, "file:///")   

  def get_num_eventos(self):
      s = ''
      [yy,mm,dd] =  self.calendar.get_date()      
      for i in range(calendar.monthrange(yy, mm+1)[1]):
        s = s + "[ '{index}', {value} ], ".format(index=i+1, value=self.get_events_in_date(yy, mm, i))
      return s
      
  def get_events_in_date(self,yy, mm, dd):
    date = datetime.datetime(yy,mm+1,dd+1)    
    datestr = date.strftime('%Y-%m-%d')
    return self.events.count(datestr)

      
if __name__ == '__main__':
  GLib.threads_init()  
  s = couchdb.Server()
  db = s[database]
  calendarWin = CalendarWin(db)
  Gtk.main()
  
