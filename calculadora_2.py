class Calculadora:
    
    def soma(self, a, b):
        return a + b

    def subtracao(self, a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def divisao(self, a, b):
        return a / b

if __name__ == '__main__':
    calculadora = Calculadora()
    print(calculadora.soma(2,5))
    print(calculadora.subtracao(7,2))
    print(calculadora.mult(2,5))
    print(calculadora.divisao(20,5))