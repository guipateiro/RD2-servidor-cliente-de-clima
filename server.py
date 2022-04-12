import sys
import socket
import random

# Classe responsavel por implementar o servidor
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
        while True:
            self.socket.listen(1)
            # Indica que o socket esta aceitando conexoes
            client, addr = self.socket.accept()
            print(f"Connected by {addr}")
            option = client.recv(1024)
            temperature = random.randint(int(sys.argv[4]),int(sys.argv[5]))
            exit = str(temperature)
            client.sendall(exit.encode())

            client.close()

if __name__ == '__main__':

    if len(sys.argv) != 6:
        print (f'Uso correto: {sys.argv[0]} <nome servidor> <host> <porta> <temperatura1> <temperatura2>')
        sys.exit(1)

    server_name = sys.argv[1]
    host = sys.argv[2]
    port = int(sys.argv[3])
    server = Server(server_name, host, port)
    #server.temperature_server()
    server.wait_request()