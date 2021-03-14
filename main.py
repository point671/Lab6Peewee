# Import from peewee
import random
import string
from peewee import *
import cherrypy

# Подкючаемся к базе SQLite
db = SqliteDatabase('schools.db')


def replace(html, key, value):
    return html.replace(key, value)


def getIndexPage():
    f = open('Main.html', "r", encoding="utf-8")
    res = f.read()
    f.close()
    return res


class Baza(Model):
    Number = PrimaryKeyField(unique=True)  # Ключ Id
    FIO = CharField()
    Email = CharField()
    Group = IntegerField()

    class Meta:
        database = db  # какая база данных используется
        db_table = 'schools'  # название таблицы этой базы данных


# Выборка
def selection(Baza):
    Baza = Baza.get(Baza.Group == 'IVTACbd')
    list = []
    if Baza == True:
        print(Baza.FIO)
    else:
        print("Запрос не найден")
    for Baza in Baza.select():
        print(Baza.Number, Baza.FIO, Baza.Email, Baza.Group)
        list.append(str(Baza.Number))
        list.append(Baza.FIO)
        list.append(Baza.Email)
        list.append(Baza.Group)
        # list_baze.append("/n")

    html = getIndexPage()
    key = 10

    for i in range(len(list)):
        html = replace(html, str(key), list[i])
        key += 1

    return html


class demoExample:
    @cherrypy.expose
    def index(self):
        return selection(Baza)

    index.exposed = True

    @cherrypy.expose
    def generate(self, DeleteName):
        delete(Baza, DeleteName)

        return selection(Baza)

    @cherrypy.expose
    def generateCreate(self, CreateName):
        CreateZapic(Baza, CreateName)
        return selection(Baza)


# Удаление сторк
def delete(Baza, DeleteName):
    One = Baza.get(Baza.FIO == DeleteName)  # выбираем всех с именем
    One.delete_instance()  # и удаляем


def CreateZapic(Baza, CreateName):
    Number, FIO, Email, Group = CreateName.split(",")
    Tom1 = Baza.create(Number=Number, FIO=FIO, Email=Email, Group=Group)


def create(Baza):
    Tom1 = Baza.create(Number='1', FIO='Andrey', Email="sabakass@mail.ru", Group='IVTACbd')
    Tom2 = Baza.create(Number='2', FIO='Anton', Email="sabakass@mail.ru", Group='IVTACbd')
    # Tom3 = Baza.create(Number='3', FIO='Misha', Email="sabakass33@mail.ru", Group='IVTACbd-22')
    Tom4 = Baza.create(Number='4', FIO='Dima', Email="sabakass@mail.ru", Group='IVTACbd')
    Tom5 = Baza.create(Number='5', FIO='Rusel', Email="sabakass@mail.ru", Group='IVTACbd')
    Tom6 = Baza.create(Number='6', FIO='Grisha', Email="sabakass@mail.ru", Group='IVTACbd')
    # создоние записи

    # Tom2 = Baza.create(Number='11', FIO='tom22', Email="sabakass33@mail.ru", Group='IVTACbd-21')
    # Tom3 = Baza.create(Number='11', FIO='tom22', Email="sabakass33@mail.ru", Group='IVTACbd-21')


#create(Baza)

# delete(Baza,nameFlag)
# selection(Baza)

# Repeat with the SAT scores
# for Baza in Baza.select():
#    Baza.delete().where(Baza.FIO == "tom2")
cherrypy.quickstart(demoExample())
