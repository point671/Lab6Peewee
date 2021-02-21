# Import from peewee

from peewee import *

# Подкючаемся к базе SQLite
db = SqliteDatabase('schools.db')



class Baza(Model):
    Number = PrimaryKeyField(unique=True)  # Ключ Id
    FIO = CharField()
    Email = CharField()
    Group = IntegerField()

    class Meta:
        database = db  # какая база данных используется
        db_table = 'schools'  # название таблицы этой базы данных

#Выборка
#Baza = Baza.get(Baza.Group == 'IVTACbd-21')
#if Baza == True:
#    print(Baza.FIO)
#else:
#    print("Запрос не найден")
#   for Baza in Baza.select():
#        print(Baza.Number, Baza.FIO, Baza.Email, Baza.Group)

#Удаление сторк
#One = Baza.get(Baza.FIO == 'tom') выбираем всех с именем том
#One.delete_instance() и удаляем

#Tom = Baza.create(Number='6', FIO='tom', Email="sabakass33@mail.ru",Group= 'IVTACbd-21')
Tom2 = Baza.create(Number='11', FIO='tom2', Email="sabakass33@mail.ru",Group= 'IVTACbd-21')

# Repeat with the SAT scores
Baza.delete().where(Baza.FIO == "tom")
