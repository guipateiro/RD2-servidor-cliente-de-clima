from datetime import datetime, timedelta
from client import Client
from server import Dns

class Tempo():
    def __init__(self):
        self.tempo1 = datetime.now()
        self.tempo2 = datetime.now()
        self.tempo3 = datetime.now()

class Cache():
    def __init__(self,log):
        self.log = log
        self.tempo = Tempo()
        self.cache_table = {"groelandia":{}, "dubai":{}, "antartida":{}}

    def add_data_cache(self, chave, temperature):
        timeout = self.set_timeout()
        self.cache_table[chave].update({"temperatura": temperature})
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
                self.log.write(f"tempo de 'groelandia' vencido, iniciando requisicao de novos dados com o servidor:\n")
                client = Client(self.log, host, Dns.porta_por_nome("groelandia"))
                self.tempo.tempo1 = self.add_data_cache("groelandia",client.send_request_raw())
                print(self.cache_table)
            except:
                tempo1 = self.add_data_cache("groelandia","erro de conexao")
                self.log.write(f"erro no recebimento da requisicao\n\n")
                print(self.cache_table)    
        if self.check_timeout(self.tempo.tempo2):
            try:
                self.log.write(f"tempo de 'dubai' vencido, iniciando requisicao de novos dados com o servidor:\n")
                client = Client(self.log, host, Dns.porta_por_nome("dubai"))
                self.tempo.tempo2 = self.add_data_cache("dubai",client.send_request_raw())
                print(self.cache_table)
            except:
                tempo2 = self.add_data_cache("dubai","erro de conexao")
                self.log.write(f"erro no recebimento da requisicao\n\n")
                print(self.cache_table)    
        if self.check_timeout(self.tempo.tempo3):
            try:
                self.log.write(f"tempo de 'antartida' vencido, iniciando requisicao de novos dados com o servidor:\n")
                client = Client(self.log, host, Dns.porta_por_nome("antartida"))
                self.tempo.tempo3 = self.add_data_cache("antartida",client.send_request_raw())
                print(self.cache_table)
            except:
                tempo3 = self.add_data_cache("antartida","erro de conexao")
                self.log.write(f"erro no recebimento da requisicao\n\n")
                print(self.cache_table)

    def atualiza(self, host):
        if self.check_timeout(self.tempo.tempo1):
            try:
                self.log.write(f"tempo de 'groelandia' vencido, iniciando requisicao de novos dados com o servidor:\n")
                client = Client(self.log, host, Dns.porta_por_nome("groelandia"))
                self.tempo.tempo1 = self.add_data_cache("groelandia",client.send_request_raw())
                print(self.cache_table)
            except:
                self.log.write(f"erro no recebimento da requisicao\n\n")
                print(self.cache_table)       
        if self.check_timeout(self.tempo.tempo2):
            try:
                self.log.write(f"tempo de 'dubai' vencido, iniciando requisicao de novos dados com o servidor:\n")
                client = Client(self.log, host, Dns.porta_por_nome("dubai"))
                self.tempo.tempo2 = self.add_data_cache("dubai",client.send_request_raw())
                print(self.cache_table) 
            except: 
                self.log.write(f"erro no recebimento da requisicao\n\n")
                print(self.cache_table)  
        if self.check_timeout(self.tempo.tempo3):
            try:
                self.log.write(f"tempo de 'antartida' vencido, iniciando requisicao de novos dados com o servidor:\n")
                client = Client(self.log, host, Dns.porta_por_nome("antartida"))
                self.tempo.tempo3 = self.add_data_cache("antartida",client.send_request_raw())
                print(self.cache_table)
            except:
                self.log.write(f"erro no recebimento da requisicao\n\n")
                print(self.cache_table)