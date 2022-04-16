from datetime import datetime, timedelta
from client import Client

class Tempo():
    def __init__(self):
        self.tempo1 = datetime.now()
        self.tempo2 = datetime.now()
        self.tempo3 = datetime.now()

class Cache():
    def __init__(self):
        self.tempo = Tempo()
        self.cache_table = {"groelandia":{}, "dubai":{}, "antartida":{}}

    def add_data_cache(self, chave, temperature):
        timeout = self.set_timeout()
        self.cache_table[chave].update({"temperatura": temperature})#, "timeout": timeout})
        return timeout

    def set_timeout(self):
        timeout = 30
        return datetime.now() + timedelta(seconds=timeout)

    def check_timeout(self, timeout):
        if timeout < datetime.now():
            return True
        else:
            return False

    def inicia(self, host):
        if self.check_timeout(self.tempo.tempo1):
            try:
                client = Client(host, 34565)
                self.tempo.tempo1 = self.add_data_cache("groelandia",client.send_request_raw())
                print(self.cache_table)
            except:
                tempo1 = self.add_data_cache("groelandia","erro de conexao")
                print(self.cache_table)    
        if self.check_timeout(self.tempo.tempo2):
            try:
                client = Client(host, 34566)
                self.tempo.tempo2 = self.add_data_cache("dubai",client.send_request_raw())
                print(self.cache_table)
            except:
                tempo2 = self.add_data_cache("dubai","erro de conexao")
                print(self.cache_table)    
        if self.check_timeout(self.tempo.tempo3):
            try:
                client = Client(host, 34567)
                self.tempo.tempo3 = self.add_data_cache("antartida",client.send_request_raw())
                print(self.cache_table)
            except:
                tempo3 = self.add_data_cache("antartida","erro de conexao")
                print(self.cache_table)

    def atualiza(self, host):
        if self.check_timeout(self.tempo.tempo1):
            try:
                client = Client(host, 34565)
                self.tempo.tempo1 = self.add_data_cache("groelandia",client.send_request_raw())
                print(self.cache_table)
            except:
                print(self.cache_table)       
        if self.check_timeout(self.tempo.tempo2):
            try:
                client = Client(host, 34566)
                self.tempo.tempo2 = self.add_data_cache("dubai",client.send_request_raw())
                print(self.cache_table) 
            except: 
                print(self.cache_table)  
        if self.check_timeout(self.tempo.tempo3):
            try:
                client = Client(host, 34567)
                self.tempo.tempo3 = self.add_data_cache("antartida",client.send_request_raw())
                print(self.cache_table)
            except:
                print(self.cache_table)