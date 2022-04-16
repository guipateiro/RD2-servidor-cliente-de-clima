import sys
import socket
import random
import requests
from bs4 import BeautifulSoup

# Classe responsavel por implementar o servidor
class Server():
    def __init__(self, server, host, port):
        self.server = server
        # Cria socket TCP/IP
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((host, port))

    # def temperature_server(self):
        
    # Metodo responsavel por aguardar a requisicao de um cliente
    def wait_request(self,local):
        print(self.server)
        # Indica ao SO que eh o servidor
        while True:
            self.socket.listen(1)
            # Indica que o socket esta aceitando conexoes
            client, addr = self.socket.accept()
            print(f"Connected by {addr}")
            option = client.recv(1024)
            temperature = self.pegadados(local)
            #self.pegadados()
            exit = str(temperature)
            client.sendall(exit.encode())
            client.close()

    def fechar(self):
        self.socket.shutdown(socket.SHUT_RDWR)
        self.socket.close()
        print ("finalizado com sucesso")    

    def pegadados(self,local):
        # Make a request to https://codedamn-classrooms.github.io/webscraper-python-codedamn-classroom-website/
        if (local == "antartida"):
            url = "https://www.tempo.com/estacao-polo-sul-amundsen-scott.htm"
        elif (local == "dubai"):
            url = "https://www.tempo.com/dubai.htm"
        elif (local == "groelandia"):
            url = "https://www.tempo.com/godthaab-nuuk.htm"  
        else:
            return "erro"
        page = requests.get(url)#, headers=agent)
        soup = BeautifulSoup(page.content, 'html.parser')
        # Extract title of page
        temperatura = soup.find('span', class_ = "dato-temperatura changeUnitT")
        print(temperatura.text + "C" )
        return str(temperatura.text + "C")      

class Dns():
    def name_to_port(name):
        if(name == "groelandia"):
            return 34565
        elif(name == "dubai"):
            return 34566
        elif(name == "antartida"):
            return 34567
        else:
            return -1            

if __name__ == '__main__':
    try:
        if len(sys.argv) != 3:
            print (f'Uso correto: {sys.argv[0]} <nome servidor> <host>')
            sys.exit(1)

        server_name = sys.argv[1]
        host = sys.argv[2]
        port = Dns.name_to_port(sys.argv[1])
        if( port == -1):
            print("nome do servidor invalido")
            print("nomes validos: groelandia, dubai, antartida")
            sys.exit(1)
        server = Server(server_name, host, port)
        server.wait_request(sys.argv[1])
    except KeyboardInterrupt:
        server.fechar()    