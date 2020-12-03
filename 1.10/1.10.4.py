class Volunteer:
    status = 'Волонтер'
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city

    def get_status(self):
        return self.status

    def get_duties(self):
        return "Список обязанностей волонтеров"

class Mentor(Volunteer):
    status = 'Наставник'

    def get_action(self):
        return 'Обучает кураторов'

    def get_duties(self):
        return "Отвечает за организацию обучений"

class Curator(Volunteer):
    status = 'Куратор'

    def get_action(self):
        return "Ищет животных, нуждающихся в помощи"

    def get_duties(self):
        return "Отвечает за содержание и пристройку животных"


v1 = Mentor('Иван', 'Петров', 'г.Москва')
v2 = Mentor('Петр', 'Иванов', 'г.Санкт-Петербург')
v3 = Curator('Василий', 'Андреев', 'г.Новосибирск')
v4 = Curator('Андрей', 'Васильев', 'г.Казань')

volunteer_list = [v1, v2, v3, v4]


guests = input('Выберите статус гостя (наставник, куратор): ')
for volunteer in volunteer_list:
    if volunteer.status.lower() == guests.lower():
        print(('%s, %s, статус "%s". %s. %s') % (volunteer.name, volunteer.city, volunteer.get_status(), volunteer.get_duties(), volunteer.get_action()))

