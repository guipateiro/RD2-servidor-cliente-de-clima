import sys
import socket
import time
import json

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
        tabela = json.loads(data)
        return tabela

    # Metodo responsavel por enviar a requisicao
    def send_request_raw(self):
        # Envia requisicao
        data = "Hello, world"
        #print (data)
        self.socket.sendall(data.encode())
        # Aguarda recebimento dos dados
        data = self.socket.recv(1024)
        return data.decode()    

    def fechar(self):
            self.socket.shutdown(socket.SHUT_RDWR)
            self.socket.close()    

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print (f'Uso correto: {sys.argv[0]} <host> <porta>')
        sys.exit(1)

    host = sys.argv[1]
    port = int(sys.argv[2])
    palavra = input('>>')
    tabela = {}
    try:
        while (palavra != "sair"):

            if (palavra == "get") or (palavra == "connect") or (palavra == "cache"):
                try:
                    client = Client(host, port)
                    tabela = client.send_request()
                    print("{:<8} {:<15} {:<10}".format('n','servidor','temperatura'))   
                    i = 1 
                    for x in tabela:
                        print("{:<8} {:<15} {:<10}".format(i,x,tabela[x]["temperatura"]))    
                        i = i + 1   
                except:
                    print("erro ao receber pacote ou se conectar com " + host + ":" + str(port))
                    sys.exit(1)

                palavra = input('>>') 

            elif (palavra == "tabela") or (palavra == "imprime") or (palavra == "print"):
                print("{:<8} {:<15} {:<10}".format('n','servidor','temperatura'))   
                i = 1 
                for x in tabela:
                    print("{:<8} {:<15} {:<10}".format(i,x,tabela[x]["temperatura"]))    
                    i = i + 1   
                palavra = input('>>') 

            elif (palavra == "info") or (palavra == "creditos"):
                print("creditos:")
                print("Cristiano C. Mendieta GRR20190394")
                print("Guilherme C. Pateiro  GRR90197152")
                palavra = input('>>') 

            elif (palavra == "ajuda") or (palavra == "help"):
                print("comandos:")
                print("----------------------------------------------------------------------------------------------")
                print("{:<30} {:<15}".format("get, connect, cache","faz um pedido para o servidor e imprime a tabela recebida"))
                print("{:<30} {:<15}".format("tabela, imprime,print","imprime a tabela LOCAL"))
                print("{:<30} {:<15}".format("info, creditos","mostra os creditos, os membros do grupo"))
                print("{:<30} {:<15}".format("help, ajuda","mostra essa tela")) 
                print("{:<30} {:<15}".format("sair","finaliza o programa"))
                print("----------------------------------------------------------------------------------------------")
                palavra = input('>>')  
            else:
                print("comando desconhecido 'ajuda' para lista de comandos")
                palavra = input('>>')
        try:        
            client.fechar()
        except: 
            sys.exit(1)    
    except KeyboardInterrupt:
        try:
            client.fechar()
        except:
            pass
        finally:       
            print ("finalizado com sucesso")                                