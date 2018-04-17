import logging
import MySQLdb as mdb
from django.conf import settings

class Database:
    def connect(self):
        self.logger = logging.getLogger("dal")
        db = settings.DATABASES['default']['NAME']
        user = settings.DATABASES['default']['USER']
        password = settings.DATABASES['default']['PASSWORD']
        host = settings.DATABASES['default']['HOST']
        port = int(settings.DATABASES['default']['PORT'])
        """
        db = "monitor"
        user = "root"
        password = "root"
        host = "localhost"
        port = 3306
        """
        con = None
        try:
            con = mdb.connect(host=host, port=port, user=user, passwd=password, db=db, charset='utf8')
        except Exception as e:
            self.logger.error("error: %d, message: %s"%(1, str(e)))
        return con

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
            self.logger.warning("ststus: %d, message: %s"%(status, message))
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
            self.logger.warning("ststus: %d, message: %s"%(status, message))
            return status, message, data
        except Exception as e:
            status = 1
            message = str(e)
            data = None
            self.logger.error("ststus: %d, message: %s"%(status, message))
            return status, message, data

    '''SELECT'''
    def execute_query(self, query):
        if not query:
            status = 1
            message = "No query"
            data = None
            self.logger.warning("ststus: %d, message: %s"%(status, message))
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
            self.logger.warning("ststus: %d, message: %s total %d"%(status, message, len(data_table)))
            return status, message, data
        except Exception as e:
            status = 1
            message = str(e)
            data = None
            self.logger.error("ststus: %d, message: %s"%(status, message))
            return status, message, data
