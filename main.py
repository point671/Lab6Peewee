# Import from peewee

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
    Baza = Baza.get(Baza.Group == 'IVTACbd-21')
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
        # list.append("/n")

   #StrA = " ".join(list)
    html = getIndexPage()


    for i in range(len(list)):
        html = replace(html, str(i), list[i])
    return html


class demoExample:
    def index(self):
        return selection(Baza)

    index.exposed = True





# Удаление сторк
def delete(Baza):
    flag = "tom22"
    One = Baza.get(Baza.FIO == flag)  # выбираем всех с именем том
    One.delete_instance()  # и удаляем


def create(Baza):
    Tom = Baza.create(Number='6', FIO='tofm', Email="sabakass33@mail.ru", Group='IVTACbd-22')  # создоние записи

    #Tom2 = Baza.create(Number='11', FIO='tom22', Email="sabakass33@mail.ru", Group='IVTACbd-21')
    #Tom3 = Baza.create(Number='11', FIO='tom22', Email="sabakass33@mail.ru", Group='IVTACbd-21')


#create(Baza)
#Tom2 = Baza.create(Number='11', FIO='tom22', Email="sabakass33@mail.ru", Group='IVTACbd-21')

#delete(Baza)
selection(Baza)

# Repeat with the SAT scores
# for Baza in Baza.select():
#    Baza.delete().where(Baza.FIO == "tom2")
cherrypy.quickstart(demoExample())