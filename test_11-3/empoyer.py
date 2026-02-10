RAISE_AMOUNT = 5000 
class Employee:
    def __init__(self, familia, salary, raise_amount):
        self.familia = familia
        self.salary = salary
        self.raise_amount = raise_amount  # сохраняем для использования

    def give_raise(self, raise_amount=None):  # опциональный параметр
        if raise_amount is None:
            raise_amount = self.raise_amount  # используем дефолтный
        self.salary += raise_amount  # короче и чище