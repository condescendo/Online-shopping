import mysql.connector
import csv


def category():
    ctg = ["mf", "wf","kf"]
    return ctg


def createdb():
    try:
        cur.execute("create database shop")
        cur.execute("use shop")
    except mysql.connector.errors.DatabaseError:
        cur.execute("use shop")


def createtable(c):
    try:
        e = "create table " + c + "(Item varchar(35),code varchar(10) UNIQUE,Price int(10)," \
                                    "discount int(15))"
        cur.execute(e)
    except mysql.connector.errors.ProgrammingError:
        pass


def takedata(c):
    d = []
    name = c + ".csv"
    with open(name, 'r') as file:
        data = csv.reader(file)
        for row in data:
            d.append(row)
            item = row[0]
            code = row[1]
            price = row[2]
            discount = row[3]
            try:
                e = "insert into " + c + "(Item,code,price,discount) " \
                                         "values ('{}','{}',{},{})".format(item, code, price, discount)
                cur.execute(e)
                db.commit()
            except mysql.connector.errors.IntegrityError:
                pass


def insertvalues():
    ctg = category()
    for c in ctg:
        createtable(c)
        takedata(c)


db = mysql.connector.connect(user="root",  passwd="area51", host="localhost")
cur = db.cursor()
