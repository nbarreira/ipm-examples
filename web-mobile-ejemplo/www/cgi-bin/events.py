#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import json
import couchdb
import CouchDBDAO


def get_database_connection():
    server = couchdb.Server("http://localhost:5984/")
    db = server["calendar"]
    dao = CouchDBDAO.CouchDBDAO(db)
    return dao

def get_params():
    # Parse get data
    form = cgi.FieldStorage()
    offset=0
    n = 10
    if form.has_key("n"):
        n = form["n"].value
    if form.has_key("offset"):
        offset = form["offset"].value
    return [n, offset]
    

def main():
    [n, offset] = get_params()
    dao = get_database_connection()
    events = dao.findEvents(n, offset)
    print '{ "count": ' + str(len(events)) + ', "rows" : ' + json.dumps(events) + '}'
        
try:
    print 'Content-Type: application/json\n\n'
    main()
except:
    cgi.print_exception()
  
    

