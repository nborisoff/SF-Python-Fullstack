class EWallet:
    def __init__(self, name, surname, balance = 0):
        self.name = name
        self.surname = surname
        self.balance = balance

    def get_balance(self):
        return self.balance


name = input('Введите имя: ')
surname = input('Введите фамилию: ')
balance = input('Введите сумму, на которую хотите пополнить баланс: ')
while not balance.isdigit():
    balance = input('Сумма должна быть числом, повторите ввод: ')
balance = int(balance)

client = EWallet(name, surname, balance)

print(('Клиент %s %s. Баланс: %s руб.') % (client.name, client.surname, client.balance))