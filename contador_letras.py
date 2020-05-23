def contadorLetras(lista_palavras):
    contador = []
    for i in lista_palavras:
        quantidade = len(i)
        contador.append(quantidade)
        return contador

if __name__ == '__main__':
    lista = ["gato", "cachorro", "galinha"]
    print(contadorLetras(lista))