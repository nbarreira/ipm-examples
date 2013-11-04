# --*-- coding: utf-8 --*--
import couchdb

class CouchDBDAO():

    def __init__(self, database):
        self._db = database
    
    def __view_to_list(self, view_result):
        
        docs = []
        for row in view_result:
            docs.append({'id': row['id'], 'key': row['key'], 'value': row['value']})        
    
        return docs


    def findEvents(self, num, offset):
        f = '''
            function (doc) {
                if (doc.type =='Event') {
                    emit(doc.date, doc);
                }
            }'''
    
        return self.__view_to_list(self._db.query(f, limit=num, skip=offset))

    

    def findSubjects(self):
        f1='''function(doc) {
                if (doc.type == 'Subject') {
                    for(var i = 0; i < doc.tags.length; i++) {
                        emit(doc.tags[i], doc.tags[i]);
                    }
                }
            }'''
        return self.__view_to_list(self._db.query(f1))

    def findBySubject(self, subject=None):
    
        f1='''function(doc) {
                if (doc.type == 'Event') {
                    for(var i = 0; i < doc.tags.length; i++){ 
                        emit(doc.tags[i], doc);
                    }
                }
        }'''
        if subject:
            return self.__view_to_list(self._db.query(f1, key=subject))
        else:
            return self.__view_to_list(self._db.query(f1))
