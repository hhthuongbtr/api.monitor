import requests # pip install requests
import json
from requests.exceptions import ConnectionError
from setting.settings import SCC_URL

class ApiRequest:
    def __init__(self):
        self.url = SCC_URL
        self.headers =  {
            'content-type': 'application/json'
        }

    def get(self):
        try:
            rsp = requests.get(self.url, data=data, headers=self.headers, timeout=5)
        except ConnectionError as e:
            return e
        if rsp.status_code == 200:
            return rsp.text
        elif rsp.status_code >= 500:
            return "Check your proxy or web services"
        else:
            return rsp.status_code 

    def put(self, data):
        try:
            rsp = requests.put(self.url, data=data, headers=self.headers, timeout=5)
        except ConnectionError as e:
            return e
        if rsp.status_code == 200:
            return rsp.text
        elif rsp.status_code >= 500:
            return "Check your proxy or web services"
        else:
            return rsp.status_code 

    def post(self, data):
        try:
            rsp = requests.put(self.url, data=data, headers=self.headers, timeout=5)
        except ConnectionError as e:
            return e
        if rsp.status_code == 200:
            return rsp.text
        elif rsp.status_code >= 500:
            return "Check your proxy or web services"
        else:
            return rsp.status_code 
