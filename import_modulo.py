from televisao import Televisao
from calculadora_1 import Calculadora
from contador_letras import contadorLetras

if __name__ == '__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)
    calculadora = Calculadora(10, 3)
    print(calculadora.soma())
    lista_animais = ["gato", "cachorro", "pato"]
    totalLetras = contadorLetras(lista_animais)
    print('O total de letras na lista é: {}'.format(totalLetras))