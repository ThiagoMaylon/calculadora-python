class Calculadora(object):
    def __init__(self, n1: int, n2: int):
        self.n1: int = n1
        self.n2: int = n2
    
    def soma(self) -> int:
        return self.n1 + self.n2
    def multiplicacao(self) -> int:
        return self.n1 * self.n2
    def subtracao(self) -> int:
        return self.n1 - self.n2
    def divisao(self) -> float:
        return self.n1 / self.n2

    def mostra_resultado(self) -> None:
        print(f'{self.n1} + {self.n2} = {self.soma()}')
        print(f'{self.n1} * {self.n2} = {self.multiplicacao()}')
        print(f'{self.n1} - {self.n2} = {self.subtracao()}')
        print(f'{self.n1} / {self.n2} = {self.divisao()}\n')

calculadora1 = Calculadora(10, 5)
calculadora2 = Calculadora(50, 8)

calculadora1.mostra_resultado()
calculadora2.mostra_resultado()