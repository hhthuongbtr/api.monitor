import MySQLdb as mdb
from django.conf import settings

class Database:
    def connect(self):
        db = settings.DATABASES['default']['NAME']
        user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        host = settings.DATABASES['default']['HOST']
        port = int(settings.DATABASES['default']['PORT'])
        return mdb.connect(host=host, port=port, user=user, passwd=password, db=db, charset='utf8')

    def close_connect(self, session):
        return session.close()

    '''
    INSERT, UPDATE, DELETE, CREATE statement
    '''
    def execute_non_query(self, query):
        if not query:
            status = 1
            message = "No query"
            data = None
            return status, message, data
        try:
            session = self.connect()
            cur=session.cursor()
            cur.execute(query)
            session.commit()
            self.close_connect(session)
            status = 0
            message = "Ok"
            data = None
            return status, message, data
        except Exception as e:
            status = 1
            message = str(e)
            data = None
            return status, message, data

    '''SELECT'''
    def execute_query(self, query):
        if not query:
            status = 1
            message = "No query"
            data = None
            return status, message, data
        try:
            session = self.connect()
            cur=session.cursor()
            cur.execute(query)
            data_table = cur.fetchall()
            self.close_connect(session)
            status = 0
            message = "Ok"
            data = data_table
            return status, message, data
        except Exception as e:
            status = 1
            message = str(e)
            data = None
            return status, message, data
