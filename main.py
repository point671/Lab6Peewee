# Import from peewee
from peewee import *


# Подкючаемся к базе SQLite
db = SqliteDatabase('schools.db')



class Baza(Model):

    Number = CharField(primary_key=True)  # Ключ Id
    FIO = CharField()
    Email = CharField()
    Group = IntegerField()

    class Meta:
        database = db # какая база данных используется
        db_table = 'schools' # название таблицы этой базы данных



print("Прив")

Baza = Baza.get(Baza.FIO == 'Dima')

if Baza ==True:
    print(Baza.FIO)
else:
    print("Запрос не найден")




# Repeat with the SAT scores
