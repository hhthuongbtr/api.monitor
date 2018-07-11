import json
import logging
import requests # pip install requests
from setting.settings import SCC_URL
from requests.exceptions import ConnectionError

class ApiRequest:
    def __init__(self):
        self.logger = logging.getLogger("scc")
        self.url = SCC_URL
        self.headers = {
            'Accept': 'application/json',
            'Authorization': 'Basic aXB0djppcHR2QDEyMzs7',
            'Cache-Control': 'no-cache',
            'Content-Type': 'application/json'
        }

    def get(self):
        self.logger.warning("Get %s"%(self.url))
        try:
            rsp = requests.get(self.url, headers=self.headers, timeout=5)
            self.logger.critical("status: %d, message: %s"%(0, str(rsp.json())))
        except ConnectionError as e:
            self.logger.error("status: %d, message: %s"%(1, str(e)))
            return None
        return rsp 

    def put(self, data):
        self.logger.warning("message: Data post contain: %s"%(str(data)))
        try:
            rsp = requests.put(self.url, data=data, headers=self.headers, timeout=5)
            self.logger.critical("status: %d, message: %s"%(0, str(rsp.json())))
        except ConnectionError as e:
            self.logger.error("status: %d, message: %s"%(1, str(e)))
            return None
        return rsp  

    def post(self, data):
        try:
            rsp = requests.post(self.url, data=data, headers=self.headers, timeout=5)
            self.logger.critical("status: %d, message: %s"%(0, str(rsp.json())))
            # print rsp.text
        except ConnectionError as e:
            self.logger.error("status: %d, message: %s"%(1, str(e)))
            return None
        return rsp
