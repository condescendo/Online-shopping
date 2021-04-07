import mysql.connector
import datetime
import csv
import cart_data as cdata


def time(state):
    with open("distances.csv","r") as file:
        data = csv.reader(file)
        for row in data:
            if row[0] == state:
                time = row[1]
                break
        else:
            time = 0
        time = float(time)//105+2
        if time > 10:
            time = time-10
    return time

def payment(total,user,ad,state):
    try :
        x = cdata.cart[user]
        user = str(user)
        try :
            e = "create table "+"a"+user+"(item varchar(35),category varchar(40),price int(4),quantity int(4),do \
             date,dd date,state varchar(30),address varchar(100))"

            cur.execute(e)
        except mysql.connector.errors.ProgrammingError:
            pass
        db.commit()
        do = datetime.date.today()
        t = cdata.time(state)
        dd = do + datetime.timedelta(days = t)
        for i in x:  # list
            y = []
            e = "select * from " + str(i[0]) + " where item ='" + str(i[1]) + "'"
            cur.execute(e)
            a = cur.fetchall()
            item = a[0][0]
            catgry = a[0][1][:2:]
            hp = a[0][2]
            discount = a[0][3]
            qty = i[2]
            if discount == 0:
                fp = hp * qty
            else:
                fp =( hp - hp * discount  / 100) * qty + 10 + 5*t
        cur.execute("insert into "+ "a"+user + "(item,category,price,quantity,do,dd,state,address) values \
        (%s,%s,%s,%s,%s,%s,%s,%s )",(item,catgry,fp,qty,do,dd,state,str(ad)))
        print("\nOrder placed on ", do,"\n\tDelivery by ",dd)
        cdata.cart.pop(int(user))
        print("\tPayment of Rs.",total," done ! \n\t\tThank you for shopping with us")
        db.commit()
    except KeyError:
        pass


categories = ["Men's Fashion", "Women's Fashion","Kid's Fashion"]
ctg = ["mf", "wf","kf"]
db = mysql.connector.connect(user="root", passwd="area51", host="localhost", database="shop")
cur = db.cursor()
final = {}
