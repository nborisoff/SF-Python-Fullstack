class EWallet:
    def __init__(self, name, surname, balance = 0):
        self.name = name
        self.surname = surname
        self.balance = balance

    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        if balance >= 0 and isinstance(balance, int):
            self.balance = balance


name = input('Введите имя: ')
surname = input('Введите фамилию: ')
balance = input('Введите сумму, на которую хотите пополнить баланс: ')
while not balance.isdigit():
    balance = input('Сумма должна быть числом, повторите ввод: ')
balance = int(balance)

client = EWallet(name, surname)
client.set_balance(balance)

print(('Клиент %s %s. Баланс: %s руб.') % (client.name, client.surname, client.get_balance()))