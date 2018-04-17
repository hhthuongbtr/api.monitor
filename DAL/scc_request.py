import json
import logging
import requests # pip install requests
from setting.settings import SCC_URL
from requests.exceptions import ConnectionError

class ApiRequest:
    def __init__(self):
        self.logger = logging.getLogger("scc")
        self.url = SCC_URL
        self.headers =  {
            'content-type': 'application/json'
        }

    def get(self):
        try:
            rsp = requests.get(self.url, data=data, headers=self.headers, timeout=5)
            self.logger.debug("status: %d, message: %s"%(0, str(json())))
        except ConnectionError as e:
            self.logger.error("status: %d, message: %s"%(1, str(e)))
            return None
        return rsp 

    def put(self, data):
        try:
            rsp = requests.put(self.url, data=data, headers=self.headers, timeout=5)
            self.logger.debug("status: %d, message: %s"%(0, str(json())))
        except ConnectionError as e:
            self.logger.error("status: %d, message: %s"%(1, str(e)))
            return None
        return rsp  

    def post(self, data):
        try:
            rsp = requests.post(self.url, data=data, headers=self.headers, timeout=5)
            self.logger.debug("status: %d, message: %s"%(0, str(json())))
        except ConnectionError as e:
            self.logger.error("status: %d, message: %s"%(1, str(e)))
            return None
        return rsp  
