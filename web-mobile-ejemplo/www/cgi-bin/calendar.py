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


def get_subject():
    form = cgi.FieldStorage()
    subject="todas"
    if form.has_key("subject"):  
        subject = form["subject"].value
    return subject


def isSubjectSelected(currentSubject, selectedSubject):
    if selectedSubject == currentSubject:
        return 'class="selected"'
    else:
        return ''
        
def get_menu_items(dao, selectedSubject):
    subjects = dao.findSubjects()
    result ="""
            <li {selected}>
                <a href="calendar.py">
                   Todas
                </a>
            </li>""".format(selected = isSubjectSelected("todas", selectedSubject))
    for s in subjects:
        name = s.decode('utf8')[1:]
        result = result + """
            <li {selected}>
                <a href="calendar.py?subject={subject}">
                   {subject}
                </a>
            </li>""".format(subject=name, selected = isSubjectSelected(name, selectedSubject))
    return result
    

def list_to_string(l):
    string = ""
    for item in l:
        string = string + item.encode('utf-8') + " "
    return string

def get_events(dao, subject):
    if subject == "todas":
        key = None
    else:
        key = "#" + subject        
    events = dao.findBySubject(key)
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
    selectedSubject = get_subject()
    
    print """<!doctype html>
        <html>
         <head>
            <title>Calendario de Eventos</title>
            <meta http-equiv="Content-Type" content="text/html;charset=utf-8" >
            <meta name="viewport" content="width=device-width, initial-scale=0.5, maximum-scale=1" />
            <link rel="stylesheet" type="text/css" href="/css/calendar.css" />
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
                <h1> Lista de eventos de {subject}</h1>
    """.format(menu=get_menu_items(dao, selectedSubject), subject=selectedSubject)
                
    get_events(dao, selectedSubject)

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
    print "Content-Type: text/html\n\n"
    main()
    
except:
    cgi.print_exception()
    

