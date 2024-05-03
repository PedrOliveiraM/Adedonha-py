import socket
import threading

def receive_messages(s):
        data, _ = s.recvfrom(1024)  # Buffer size is 1024 bytes
        print(f"Mensagem recebida: {data.decode()}")

def send_messages(s, server_host, server_port):
    message = input("Digite seu nome: ")
    s.sendto(message.encode(), (server_host, server_port))
    # Aguarde a resposta do servidor antes de continuar
    data, _ = s.recvfrom(1024)
    print(f"Resposta do servidor: {data.decode()}")

def send_messagesGame(s, server_host, server_port):        
    nome = input("Nome: ")
    cidade = input("Cidade: ")
    pais = input("País: ")
    animal = input("Animal: ")
    objeto = input("Objeto: ")
    message = f"{nome};{cidade};{pais};{animal};{objeto}"
    message = message.upper()
    s.sendto(message.encode(), (server_host, server_port))
    # Aguarde a resposta do servidor antes de continuar
    data, _ = s.recvfrom(1024)
    print(f"Resposta do servidor: {data.decode()}")

def udp_client(server_host='127.0.0.1', server_port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        threading.Thread(target=receive_messages, args=(s,)).start()
        send_messages(s, server_host, server_port) 
        send_messagesGame(s, server_host, server_port)
        
if __name__ == "__main__":
    udp_client()
