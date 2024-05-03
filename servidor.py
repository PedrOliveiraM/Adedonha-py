import socket
import threading
from functions import _letras
from functions import _verificarPontos

def receive_messages(s):
        data, _ = s.recvfrom(1024)  # Buffer size is 1024 bytes
        print(f"Mensagem recebida: {data.decode()}")

def send_messages(s, client_addr):
        message = input("Digite uma mensagem para enviar: ")
        s.sendto(message.encode(), client_addr)

def udp_server(host='127.0.0.1', port=12345):   
    listaDeJogadores = []     
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    print("Servidor UDP iniciado. Aguardando mensagem.")
    
    letraGerada = _letras.sortLetter()  #sortear letra
    
    
    #   CRIAR FUNÇÃO PARA RECEBER MENSAGEM DO CLIENTE
    
    
    
    
    #---------------------------- Recebendo a mensagem do jogador 1 ----------------------------
    data, addr = s.recvfrom(1024)  # Aguarda a primeira mensagem para obter o endereço do cliente
    jogador1 = Player(data.decode(), addr, 0 , [])
    s.sendto("Mensagem recebida com sucesso!".encode(), addr)  
    print(f"Mensagem recebida do jogador1: {data.decode()}")
    listaDeJogadores.append(jogador1) #adicionando o jogador 1 na lista de jogadores
    
    #---------------------------- Recebendo a mensagem do jogador 2 ----------------------------
    data, addr = s.recvfrom(1024)  # Aguarda a primeira mensagem para obter o endereço do cliente
    jogador2 = Player(data.decode(), addr, 0 , [])
    s.sendto("Mensagem recebida com sucesso!".encode(), addr)  
    print(f"Mensagem recebida do jogador2: {data.decode()}")
    listaDeJogadores.append(jogador2) #adicionando o jogador 1 na lista de jogadores

    #---------------------------- Enviando msg para os jogadores ----------------------------
    for jogador in listaDeJogadores:
        s.sendto((f"A letra sorteada foi:{letraGerada}").encode(), jogador.address) #envio a letra para meus jogadores
             
    #---------------------------- Recebendo a mensagem ----------------------------
    data, addr = s.recvfrom(1024)   # receber mensagem adedonha
    for jogador in listaDeJogadores:
        if (jogador.address == addr):
            jogador_nome = jogador.nome
    print(f"Mensagem recebida de {jogador_nome}: {data.decode()}-{addr}")
    msg = data.upper().decode() #transformando a mensagem em maiuscula
    listaSplit = msg.split(';') #separando a mensagem por ;
    #verificar se o jogador esta na lista com o addr
    for jogador in listaDeJogadores: 
        if jogador.address == addr:
            for palavra in listaSplit:
                jogador.lista.append(palavra)
                
                
    #---------------------------- Recebendo a mensagem ----------------------------          
    data, addr = s.recvfrom(1024)   # receber mensagem adedonha
    for jogador in listaDeJogadores:
        if (jogador.address == addr):
            jogador_nome = jogador.nome
    print(f"Mensagem recebida de {jogador_nome}: {data.decode()}-{addr}")
    msg = data.upper().decode() #transformando a mensagem em maiuscula
    listaSplit = msg.split(';') #separando a mensagem por ;
    #verificar se o jogador esta na lista com o addr
    for jogador in listaDeJogadores: 
        if jogador.address == addr:
            for palavra in listaSplit:
                jogador.lista.append(palavra)
                
                
    # Enviando a pontuação para os jogadores
    listaDeJogadores = _verificarPontos.VerificarPontuacao(listaDeJogadores, letraGerada)
    
    for jogador in listaDeJogadores:
    # Acesse o endereço e os pontos do jogador
        addr_jogador = jogador.address
        pontos_jogador = jogador.pontos
        mensagem = f"Seus pontos atuais são: {pontos_jogador}"
        s.sendto(mensagem.encode(), addr_jogador)
    
    
if __name__ == "__main__":
    class Player:
        def __init__(self, nome, address  , pontos, lista):
            self.nome = nome
            self.address = address
            self.pontos = pontos
            self.lista = lista
    udp_server()
