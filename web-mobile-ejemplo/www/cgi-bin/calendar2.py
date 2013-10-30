#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import couchdb
import CouchDBDAO

def get_database_connection():
    server = couchdb.Server()
    db = server["calendar"]
    dao = CouchDBDAO.CouchDBDAO(db)
    return dao

        
def get_menu_items(dao):
    subjects = dao.findSubjects()
    result ="""
            <li class="selected">
                <a href="calendar2.py">
                   Todas
                </a>
            </li>"""
    for s in subjects:
        name = s.decode('utf8')[1:]
        result = result + """
            <li>
                <a href="calendar2.py">
                   {subject}
                </a>
            </li>""".format(subject=name)
    return result
    


def list_to_string(l):
    string = ""
    for item in l:
        string = string + item.encode('utf-8') + " "
    return string


def get_events(dao):
        
    events = dao.findBySubject()
    
    for e in events:        
        print """<article>
            <time>{date}</time>
            <h1>{description}</h1>
            <p class="tags">{tags}</p>
            <p class="creator">{creator}</p>
        </article>""".format(
            description=e['description'].encode('utf-8'), 
            date=e['date'].encode('utf-8'), 
            tags=list_to_string(e['tags']), 
            creator=e['creator'].encode('utf-8'))
    


def main():
    dao = get_database_connection()
    print """<!doctype html>
    <html>
        <head>
            <title>Calendario de Eventos</title>
            <meta http-equiv="Content-Type" content="text/html;charset=utf-8" >
            <meta name="viewport" content="width=device-width, initial-scale=0.5, maximum-scale=1" />
            <link rel="stylesheet" type="text/css" href="/css/calendar.css" />
        
            <script type="text/javascript" src="/js/calendar.js"></script>
            <script type="text/javascript">
                window.onload = calendar_init;
            </script>
        </head>
    
        <body>
                
         <div id="wrapper">
            <header>
                <h1>Calendario de Eventos</h1>
            </header>
                     
            <nav>
                <ul>
                    {menu}
                </ul>
            </nav>   
            
            <section>
                <h1> Lista de eventos de Todas</h1>""".format(menu=get_menu_items(dao))
                
    get_events(dao)

    print """
            </section>
            
            <footer>            
                Interfaces Persona Máquina - Curso 2013/2014
                <br />
                Noelia Barreira Rodríguez 
            </footer>
         
         
         </div>
        
    
        </body>

    </html>"""



try:   
    print("Content-type: text/html\n\n")   
    main() 
except:
    cgi.print_exception()               
    
