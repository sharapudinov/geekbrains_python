class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'
    def get_total_income(self):
        return sum(self._income.values())

pos=Position('Шамиль','Шарапудинов','датасайнтист',{"wage": 300000, "bonus": 500000})

print(pos.get_full_name(),pos.get_total_income())