# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег

class BankAccount:
    def __init__(self):
        self.balance = 0  
        self.transactions = 0 

    def deposit(self, amount):
        if amount % 50 == 0: 
            self.balance += amount
            self.transactions += 1
            self.calculate_interest()
            self.display_balance()
        else:
            print("Сумма пополнения должна быть кратной 50 у.е.")

    def withdraw(self, amount):
        if amount % 50 == 0:  
            if amount <= self.balance:
                self.balance -= amount
                self.transactions += 1
                self.calculate_interest()
                self.display_balance()
            else:
                print("Недостаточно средств на счете")
        else:
            print("Сумма снятия должна быть кратной 50 у.е.")

    def calculate_interest(self):
        if self.transactions % 3 == 0:  
            interest = self.balance * 0.03
            self.balance += interest

        if self.balance > 5000000:  
            tax = self.balance * 0.10
            self.balance -= tax

    def display_balance(self):
        print(f"Баланс: {self.balance} у.е.")

    def run_atm(self):
        while True:
            print("\nДоступные действия:")
            print("1. Пополнить счет")
            print("2. Снять средства")
            print("3. Выйти")
            choice = input("Выберите действие (1 | 2 | 3): ")

            if choice == '1':
                amount = int(input("Введите сумму для пополнения: "))
                self.deposit(amount)
            elif choice == '2':
                amount = int(input("Введите сумму для снятия: "))
                self.withdraw(amount)
            elif choice == '3':
                print("Удачи!")
                break
            else:
                print("Неверный выбор. Пожалуйста, выберите 1, 2, 3.")


atm = BankAccount()
atm.run_atm()