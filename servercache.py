import sys
import socket
import time
import json
from datetime import datetime, timedelta

# Classe responsavel por implementar o cliente
class Client():
    def __init__(self, host, port):
        # Cria um socket TCP/IP
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Estabelece conexao
        self.connection = self.socket.connect((host, port))

    # Metodo responsavel por enviar a requisicao
    def send_request(self):
        # Envia requisicao
        data = "Hello, world"
        #print (data)
        self.socket.sendall(data.encode())
        # Aguarda recebimento dos dados
        data = self.socket.recv(1024)
        print(data.decode())
        return data.decode()

class Cache():
    def __init__(self):
        self.cache_table = {"alaska":{}, "saara":{}, "antartida":{}}

    def add_data_cache(self, chave, temperature):
        timeout = self.set_timeout()
        self.cache_table[chave].update({"temperature": temperature})#, "timeout": timeout})
        return timeout

    def set_timeout(self):
        timeout = 30
        return datetime.now() + timedelta(seconds=timeout)

    def check_timeout(self, timeout):
        if timeout < datetime.now():
            return True
        else:
            return False

class Server():
    def __init__(self, server, host, port):
        self.server = server
        # Cria socket TCP/IP
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))

    # def temperature_server(self):
        
    # Metodo responsavel por aguardar a requisicao de um cliente
    def wait_request(self):
        print(self.server)
        # Indica ao SO que eh o servidor
        tempo1 = datetime.now()
        tempo2 = datetime.now()
        tempo3 = datetime.now()
        cache = Cache()
        if cache.check_timeout(tempo1):
            try:
                client = Client(host, 34565)
                tempo1 = cache.add_data_cache("alaska",client.send_request())
                print(cache.cache_table)
            except:
                tempo1 = cache.add_data_cache("alaska","erro de conexao")
                print(cache.cache_table)    
        if cache.check_timeout(tempo2):
            try:
                client = Client(host, 34566)
                tempo2 = cache.add_data_cache("saara",client.send_request())
                print(cache.cache_table)
            except:
                tempo2 = cache.add_data_cache("saara","erro de conexao")
                print(cache.cache_table)    
        if cache.check_timeout(tempo3):
            try:
                client = Client(host, 34567)
                tempo3 = cache.add_data_cache("antartida",client.send_request())
                print(cache.cache_table)
            except:
                tempo3 = cache.add_data_cache("antartida","erro de conexao")
                print(cache.cache_table)
        while True:
            self.socket.listen(1)
            # Indica que o socket esta aceitando conexoes
            mapa, addr = self.socket.accept()
            print(f"Connected by {addr}")
            option = mapa.recv(1024)
            if cache.check_timeout(tempo1):
                try:
                    client = Client(host, 34565)
                    tempo1 = cache.add_data_cache("alaska",client.send_request())
                print(cache.cache_table)   
            if cache.check_timeout(tempo2):
                try:
                    client = Client(host, 34566)
                    tempo2 = cache.add_data_cache("saara",client.send_request())
                print(cache.cache_table)    
            if cache.check_timeout(tempo3):
                try:
                    client = Client(host, 34567)
                    tempo3 = cache.add_data_cache("antartida",client.send_request())
                print(cache.cache_table) 
            data = json.dumps(cache.cache_table).encode()    
            mapa.sendall(data)

            mapa.close()


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print (f'Uso correto: {sys.argv[0]} <host> <porta>')
        sys.exit(1)
    host = sys.argv[1]
    port = int(sys.argv[2])
    servertabela = Server("tabela",host, port)
    servertabela.wait_request()   