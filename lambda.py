########## Forma mais simples e enxuta de fazer uma calculadora/ um contador
contadorLetras = lambda lista: [len(i) for i in lista]

listaAnimais = ['tigre', 'leão', 'papagaio']
print(contadorLetras(listaAnimais))
#################################################
soma = lambda x,y: x+y

print(soma(4,3))

############ Calculadora com Lambda #############

calculadora = {
    'soma': lambda x, y: x+y,
    'subtracao': lambda x,y: x+y,
    'multiplicacao': lambda x,y: x*y,
    'divisao':lambda x, y: x/y
}
soma = calculadora['soma']
#soma = lambda x,y: x+y ####### mesma coisa da linha 18
multiplicacao = calculadora['multiplicacao']
print('A soma é: {}'.format(soma(7, 20)))
print('A multiplicação é: {}'.format(multiplicacao(4,5)))