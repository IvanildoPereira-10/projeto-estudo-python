class Calculadora:
    def __init__(self, num1, num2):
         self.a = num1
         self.b = num2

    def soma(self):
        return self.a + self.b

    def subtracao(self):
        return self.a - self.b

    def mult(self):
        return self.a * self.b

    def divisao(self):
        return self.a / self.b

if __name__ == '__main__':
    calculadora = Calculadora(10, 2)
    print(calculadora.a)
    print(calculadora.soma())
    print(calculadora.subtracao())
    print(calculadora.mult())
    print(calculadora.divisao())