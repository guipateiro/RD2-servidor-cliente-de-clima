import sys
import socket
import time
import json
from datetime import datetime, timedelta
from cache import Cache , Tempo
from client import Client

class Server():
    def __init__(self, server, host, port):
        self.server = server
        # Cria socket TCP/IP
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #permite que o endereço do servidor seja reusado caso ele seja fechado
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((host, port))
        
    # Metodo responsavel por aguardar a requisicao de um cliente
    def wait_request(self):
        print(self.server)
        # Indica ao SO que eh o servidor
        cache = Cache()
        cache.inicia(host)         
        while True:
            self.socket.listen(1)
            # Indica que o socket esta aceitando conexoes
            mapa, addr = self.socket.accept()
            print(f"Connected by {addr}")
            option = mapa.recv(1024)
            cache.atualiza(host) 
            data = json.dumps(cache.cache_table).encode()    
            mapa.sendall(data)
            mapa.close()

    def fechar(self):
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()
        print ("finalizado com sucesso")          
      
if __name__ == '__main__':
    try:
        if len(sys.argv) != 3:
            print (f'Uso correto: {sys.argv[0]} <host> <porta>')
            sys.exit(1)
        host = sys.argv[1]
        port = int(sys.argv[2])
        servertabela = Server("tabela",host, port)
        servertabela.wait_request() 
    except KeyboardInterrupt:
        servertabela.fechar()
             
