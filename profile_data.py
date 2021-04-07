import mysql.connector
import csv


def usertable():
    try:
        e = "create table user (Name varchar(35),Phone bigint(15) UNIQUE,state varchar(40),pincode int(7))"
        cur.execute(e)
    except mysql.connector.errors.ProgrammingError:
        pass
    e = "select phone from user"
    cur.execute(e)
    a = cur.fetchall()
    for i in a:
        users.append(i[0])


def user():
    e = "select * from user"
    cur.execute(e)
    a = cur.fetchall()
    if len(a) == 0:
        print("No user registered")
        insertuser()
    else:
        print("Registered users are :")
        for i in a:
            print("\t", i)
        c = input("  1.Select from registered user \n  2. Add new user \n  3.Edit details \
        \n  4. Delete user \n  Any key to go back \n Enter : ")
        if c == "1":
            phin = int(input(" \t Enter phone number : "))
            e = "select * from user where phone='"+str(phin)+"'"
            cur.execute(e)
            a = cur.fetchall()
            if len(a) != 0:
                userlist(phin)
                print("Welcome", a[0][0], "!")
            else:
                print("Phone number does not exist")
                ch = input("\t1.Select from registered user \n\t2. Add new user \n\t\tAny key to go back \n Enter : ")
                if ch == "1":
                    user()
                elif ch == "2":
                    insertuser()
        elif c == "2":
            insertuser()
        elif c == "3":
            update()
        elif c == "4":
            delete()
        else:
            pass


def update():
    phone = input("Enter phone number : ")
    e = "select * from user where phone = '"+phone+"'"
    cur.execute(e)
    a = cur.fetchall()
    if len(a) == 0:
        print("Phone Number not registered")
    else:
        print("Details are : ")
        for i in a[0]:
            print(i, end=" ")
        pname = input("\n Enter new name, * to continue : ")
        if pname != "*":
            e = "Update user set name='" + pname + "' where phone=' " + phone + "'"
            cur.execute(e)
        state = input(" Enter new state, * to continue : ")
        if state != "*":
            e = "Update user set state='" + state + "' where phone=' " + phone + "'"
            cur.execute(e)
        pin = input(" Enter new pin, * to continue : ")
        if pin != "*":
            e = "Update user set pincode='" + pin + "' where phone=' " + phone + "'"
            cur.execute(e)
        db.commit()
        print("Data successfully edited! ")


def delete():
    phone = input("Enter phone number : ")
    e = "delete from user where phone='" + phone + "'"
    cur.execute(e)
    print("\n\t User deleted!")


def insertuser():
    name = input("Enter name : ")
    name = name.strip()
    phone = int(input("Enter Phone number : "))
    address = input("Enter address : ")
    address = address.strip()
    address = address.title()
    pin = input("Enter Pincode :")
    try:
        e = "insert into  user (name,phone,state,pincode) values ('{}',{},'{}',{})".format(name, phone, address, pin)
        cur.execute(e)
        db.commit()
        userlist(phone)
    except mysql.connector.errors.IntegrityError:
        e = "select name from user where phone='"+str(phone)+"'"
        cur.execute(e)
        a = cur.fetchall()
        name = a[0][0]
        print("Phone already registered by ", name)
        pass
    print("Welcome", name, "!")


def selecteduser():
    a = len(users)
    x = users[a-1]
    return x


def userlist(phone):
    for i in range(len(users)):
        if users[i] == phone:
            users.pop(i)
            break
    users.append(phone)


def check(state):
    with open("distances.csv", "r") as file:
        data = csv.reader(file)
        for i in data:
            if i[0] == state:
                break
        else:
            print("Sorry we do not deliver in entered location!")
            return False


db = mysql.connector.connect(user="root", passwd="area51", host="localhost", database="shop")
cur = db.cursor()
users = []
