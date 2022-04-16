#   feito por:
#   
#
#
#   data da ultima modoficação 
import sys
import socket
import random
import requests
from bs4 import BeautifulSoup

# Classe responsavel por implementar o servidor
class Server():
    def __init__(self, servidor, log, host, port):
        self.servidor = servidor
        self.log = log
        # Cria socket TCP/IP
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #permite que o endereço do servidor seja reusado caso ele seja fechado
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((host, port))
        
    # Metodo responsavel por aguardar a requisicao de um cliente
    def aguarda_requisicao(self,local):
        self.log.write(f"{self.servidor} aguardando requisicao...\n")
        # Indica ao SO que eh o servidor
        while True:
            self.socket.listen(1)
            # Indica que o socket esta aceitando conexoes
            cliente, addr = self.socket.accept()
            self.log.write(f"\nConnected by {addr}\n")
            #pega o pacote do cliente
            cliente.recv(1024)
            #pega os dados da internet do local informado
            temperatura = self.pegadados(local)
            # prepara e envia temperatura para o cliente
            cliente.sendall(temperatura.encode())
            cliente.close()

    def fechar(self):
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()
        log.write('\n----------------------------------\n\n')
        log.write(f"{nome_servidor} finalizado com sucesso\n\n")
        log.write('----------------------------------\n\n')   

    def pegadados(self,local):
        # pega o url baseado no nome do lugar que foi inserido
        if (local == "antartida"):
            url = "https://www.tempo.com/estacao-polo-sul-amundsen-scott.htm"
        elif (local == "dubai"):
            url = "https://www.tempo.com/dubai.htm"
        elif (local == "groelandia"):
            url = "https://www.tempo.com/godthaab-nuuk.htm"  
        else:
            return "erro"
        # pega a pagina da internet baseado no url    
        pagina_web = requests.get(url)
        soup = BeautifulSoup(pagina_web.content, 'html.parser')
        # extrai a classe que contem a temperatura atual do lugar
        temperatura = soup.find('span', class_ = "dato-temperatura changeUnitT")
        self.log.write(temperatura.text + "C" )
        return str(temperatura.text + "C")      

class Dns():
    def porta_por_nome(nome):
        # indica qual porta usar baseado no nome do servidor
        if(nome == "groelandia"):
            return 34565
        elif(nome == "dubai"):
            return 34566
        elif(nome == "antartida"):
            return 34567
        else:
            # retorna -1 caso o nome inserido seja invalido
            return -1            

if __name__ == '__main__':
    try:
        if len(sys.argv) != 3:
            print (f'Uso correto: {sys.argv[0]} <nome servidor> <host>')
            sys.exit(1)

        nome_servidor = sys.argv[1]
        host = sys.argv[2]
        port = Dns.porta_por_nome(nome_servidor)
        if(port == -1):
            print("nome do servidor invalido")
            print("nomes validos: groelandia, dubai, antartida")
            sys.exit(1)

        log_file = 'logs/' + nome_servidor + '_log.txt'
        log = open(log_file, 'w')
        log.write('----------------------------------\n\n')
        log.write(f"Inicio de execucao servidor {nome_servidor}\n\n")
        log.write('----------------------------------\n\n')

        server = Server(nome_servidor, log, host, port)
        server.aguarda_requisicao(nome_servidor)
    except KeyboardInterrupt:
        server.fechar()    
    