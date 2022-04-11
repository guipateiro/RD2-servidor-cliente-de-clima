import sys
import socket

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
        self.socket.sendall(b"Hello, world")
        # Aguarda recebimento dos dados
        data = self.socket.recv(1024)
        print(data)

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print (f'Uso correto: {sys.argv[0]} <host> <porta>')
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])
    client = Client(host, port)
    client.send_request()