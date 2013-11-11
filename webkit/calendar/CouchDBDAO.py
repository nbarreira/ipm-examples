#!/usr/bin/env python
# --*-- coding: utf-8 --*--
import couchdb

class CouchDBDAO():

    def __init__(self, database):
        self._db = database
    
    def __view_to_list(self, view_result):
        
        docs = []
        for row in view_result:
            docs.append(row['value'])        
    
        return docs


    def findEventsByDate(self, date):
        f = '''
            function (doc) {
                if (doc.type =='Event') {
                    emit(doc.date, doc);
                }
            }'''
        return self.__view_to_list(self._db.query(f, key=date))


    def findEventsByPeriod(self, startdate, enddate):
        f = '''
            function (doc) {
                if (doc.type =='Event') {
                    emit(doc.date, doc.date);
                }
            }'''
    
        return self.__view_to_list(self._db.query(f, startkey=startdate, endkey=enddate))

    


