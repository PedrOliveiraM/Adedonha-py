def VerificarPontuacao(listaDeJogadores, letra):
    for jogador in listaDeJogadores:
        for palavra in jogador.lista: # Para cada palavra na lista do jogador
            if palavra[0] == letra: # Verifica se a primeira letra da palavra é igual à letra especificada
                jogador.pontos += 10
    
    for i in range(len(listaDeJogadores)):
        for j in range(i+1, len(listaDeJogadores)):
            for k in range(len(listaDeJogadores[i].lista)):
                if listaDeJogadores[i].lista[k] == listaDeJogadores[j].lista[k]:
                    listaDeJogadores[i].pontos -= 5
                    listaDeJogadores[j].pontos -= 5
                    
    return listaDeJogadores

"""
class Player:
        def __init__(self, nome, address  , pontos, lista):
            self.nome = nome
            self.address = address
            self.pontos = pontos
            self.lista = lista
            

jogador1 = Player("ENRIQUE", "12345", 0 , ["Pedro", "sefguro", "Polonia", "aas", "Poste"])         # 10 0 10 0 5 = 25
jogador2 = Player("Luiz", "4755", 0 , ["Pietro", "Porto seguro", "Portugal", "Pato", "a"])         # 10 5 10 5 0 = 30
jogador3 = Player("sabrina", "222", 0 , ["Portuga", "Porto seguro", "Pasmania", "Pato", "Poste"])  # 10 5 10 5 5 = 35

listaDeJogadores = [jogador1, jogador2, jogador3]

VerificarPontuacao(listaDeJogadores, "P")
#imprimir os pontos de cada jogador:
for jogador in listaDeJogadores:
    print(f"O jogador {jogador.nome} tem {jogador.pontos} pontos")
    """