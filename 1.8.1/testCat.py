from cat import Cat
cat1 = Cat('Барон', 'мальчик', '2 года')
cat2 = Cat('Сэм', 'мальчик', '2 года')

print('Первый питомец:')
print('Имя:', cat1.getName())
print('Пол:', cat1.getGender())
print('Возраст:', cat1.getAge(), '\n')
print('Второй питомец:')
print('Имя:', cat2.getName())
print('Пол:', cat2.getGender())
print('Возраст:', cat2.getAge())