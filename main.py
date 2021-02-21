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
        database = db # какая база данных используется
        db_table = 'schools' # название таблицы этой базы данных





Baza = Baza.get(Baza.Group == 'IVTACbd-21')

if Baza ==True:
    print(Baza.FIO)
else:
    print("Запрос не найден")


    for Baza in Baza.select():
        print(Baza.Number,Baza.FIO,Baza.Email,Baza.Group)


# Repeat with the SAT scores
