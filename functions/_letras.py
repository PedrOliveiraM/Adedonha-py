def sortLetter():   
    import random

    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    tamanho = len(letras) #tamanhon da string
    index = random.randint(0, tamanho - 1) #gera um numero aleatorio

    return(letras[index])
