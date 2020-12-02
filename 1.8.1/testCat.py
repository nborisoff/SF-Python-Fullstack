from cat import Cat
cat1 = Cat('Барон', 'мальчик', '2 года')
cat2 = Cat('Сэм', 'мальчик', '2 года')

print('Первый питомец:')
print('Имя:', cat1.get_name())
print('Пол:', cat1.get_gender())
print('Возраст:', cat1.get_age(), '\n')
print('Второй питомец:')
print('Имя:', cat2.get_name())
print('Пол:', cat2.get_gender())
print('Возраст:', cat2.get_age())