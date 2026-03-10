# Create a class called PersonAccount. 
# It has firstname, lastname, incomes, expenses properties and it has total_income, 
    # Incomes is a set of incomes and its description. The same goes for expenses.
    # total_expense, account_info, add_income, add_expense and account_balance methods. 

class PersonAccount:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = {}    # {'Salario': 1000, 'Freelance': 500}
        self.expenses = {}   # {'Renta': 300, 'Comida': 200}

    def add_income(self, description, amount):
        self.incomes[description] = amount

    def add_expense(self, description, amount):
        self.expenses[description] = amount

    def total_income(self):
        return sum(self.incomes.values())

    def total_expense(self):
        return sum(self.expenses.values())

    def account_balance(self):
        return self.total_income() - self.total_expense()

    def account_info(self):
        print(f"Nombre: {self.firstname} {self.lastname}")
        print(f"Ingresos: {self.incomes}")
        print(f"Gastos:   {self.expenses}")
        print(f"Balance:  {self.account_balance()}")


# Prueba
P1 = PersonAccount('Fernando', 'Gómez')
P1.add_income('Salario', 1000)
P1.add_income('Freelance', 500)
P1.add_expense('Renta', 300)
P1.add_expense('Comida', 200)

P1.account_info()
print("Balance:", P1.account_balance())
