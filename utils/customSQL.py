from django.db.models import Q
from channel.models import *
from log.models import *
from itertools import chain
from django.db import connection
import os

def my_custom_sql(cmd):
    cursor = connection.cursor()
    cursor.execute(cmd)
    row = cursor.fetchall()
    cursor.close()
    return row

#######################################################################
#                                                                     #
#-------------------------------File----------------------------------#
#                                                                     #
#######################################################################
class File:
    def __init__(self):
        self.filedir= "/tmp/log_file.sql"
        if not os.path.exists(self.filedir):
            command="echo '\n' >"+self.filedir
            os.system(command)

    def read(self):
        f = open(self.filedir, 'r')
        lines=f.read()
        f.close()
        command="cat /dev/null > "+self.filedir
        os.system(command)
        return lines

    def write(self, text):
        f = open(self.filedir, 'r')
        data_rows = f.read()
        f.close()
        if text not in data_rows:
            f = open(self.filedir, 'a')
            f.write(text+'\n')
            f.close()
        else:
            print text
            print "replicate"