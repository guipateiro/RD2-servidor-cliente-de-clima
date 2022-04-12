import sys
import socket
import time

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

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print (f'Uso correto: {sys.argv[0]} <host> <porta>')
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])
    #descomente para fazer um cliente que manda mensagens regularmente
    #while True:
    client = Client(host, 34565)
    client.send_request()
    #time.sleep(3)