from pydantic import BaseModel

class Operacao(BaseModel):
    num1: float
    num2: float

    def soma(self):
        return self.num1 + self.num2

    def subt(self):
        return self.num1 - self.num2

    def mult(self):
        return self.num1 * self.num2

    def div(self):
        if self.num2 == 0:
            raise ValueError("Divisão por zero não é permitida.")
        return self.num1 / self.num2
