"""
    Autores: Cristiano C. Mendieta e Guilherme Pateiro
    Última modificação: 16/04/2022
"""

import sys
import socket
import json
from cache import Cache

class ServerCache():
    def __init__(self, servidor, log, host, port):
        self.servidor = servidor
        self.log = log
        # Cria socket TCP/IP
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Permite que o endereco do servidor seja reusado caso ele seja fechado
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((host, port))
         
    # Metodo responsavel por aguardar a requisicao de um cliente
    def aguarda_requisicao(self):
        self.log.write(f"{self.servidor} aguardando requisicao\n\n")
        # Indica ao SO que eh o servidor
        cache = Cache(self.log)
        cache.inicia(host)         
        while True:
            self.socket.listen(1)
            # Indica que o socket esta aceitando conexoes
            localizacao, endereco = self.socket.accept()
            self.log.write(f"Conectado por {endereco}\n\n")
            cache.atualiza(host) 
            data = json.dumps(cache.cache_table).encode()    
            localizacao.sendall(data)
            localizacao.close()

    # Metodo responsavel por fechar a conexao do socket
    def fechar(self):
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()
        log.write('----------------------------------\n\n')
        log.write(f"{self.servidor} finalizado com sucesso\n\n")
        log.write('----------------------------------\n\n')        
      
if __name__ == '__main__':
    try:
        if len(sys.argv) != 3:
            print (f'Uso correto: {sys.argv[0]} <host> <porta>')
            sys.exit(1)
        host = sys.argv[1]
        port = int(sys.argv[2])

        log_file = 'logs/cache_log.txt'
        log = open(log_file, 'w')
        log.write('----------------------------------\n\n')
        log.write('Inicio de execucao servidor cache\n\n')
        log.write('----------------------------------\n\n')

        servidor_tabela = ServerCache("tabela_cache", log, host, port)
        servidor_tabela.aguarda_requisicao()
    except KeyboardInterrupt:
        servidor_tabela.fechar()
             
