import mysql.connector
import csv
import datetime
itemlist = []
ctglist = []
cart = {}


def add(user,ctgofitem,item):
    qty = int(input("Enter quantity : "))
    if user in cart:
        c = 0
        for i in cart[user]:
            if i[0] == ctgofitem and i[1] == item:
                qty = i[2]+1
                cart[user].pop(c)
            c = c+1
        if item in cart[user]:
            cart[user].append([ctgofitem,item,qty])
        else:
            cart[user].append([ctgofitem, item, qty])
    else:
        cart[user]=[[ctgofitem,item,qty]]
    e = "select name from user where phone ='"+str(user)+"'"
    cur.execute(e)
    a = cur.fetchall()
    name = a[0][0]
    print("\nItem Added! Items in "+name+"'s cart are :")
    x = cart[user]
    for i in x: # x- nested list i- list
        for k in range(len(ctg)):
            if ctg[k] == i[0]:
                cat = categories[k]
        print("\t",i[1], "(", cat, ")", i[2])
        print()


def view(user):
    e = "select name from user where phone ='"+str(user)+"'"
    cur.execute(e)
    a = cur.fetchall()
    name = a[0][0]
    if user in cart:
        print("Items in "+name+"'s cart are :")
        x = cart[user]
        for i in x:
            print(i[1]," (",i[2],")")
    else:
        print("Your cart is empty!")

def delete(item,user):
    if len(cart) == 0:
        print("Cart empty! No item to delete.")
    else:
        c=0
        for i in cart[user]:
            i[1] = i[1].capitalize()
            if str(i[1]) == str(item) :
                if i[2]>1:
                    c= i[2]
                    while c >= i[2]:
                        c = int(input("Quantity of items you want to reduce: "))
                    if c == i[2]:
                        cart[user].pop(c)
                        break
                    else:
                        i[2] = i[2]-c
                        break
                else:
                    cart[user].pop(c)
                    break
            c = c+1
            if cart[user] == []:
                cart.pop(user)
                break
        else:
            print("Item not in cart")
        view(user)



def bill(user):
    if user in cart:
        x = cart[user] #nested list
        data =[]
        for i in x: #list
            y=[]
            e = "select * from "+str(i[0])+" where item ='"+str(i[1])+"'"
            cur.execute(e)
            a = cur.fetchall()
            item = a[0][0]
            for k in range(len(ctg)):
                if ctg[k] == i[0]:
                    catgry = categories[k]
                    break
            hp = a[0][2]
            discount = a[0][3]
            qty = i[2]
            if discount == 0:
                fp = hp*qty
            else:
                fp = (hp-hp*discount/100) * qty
            y = [item,catgry,hp,discount,qty,fp]
            data.append(y)
        t,a,s = tableprint(data,user)
        return t,a,s
    else:
        print("Cart empty! :'(")  ## $-P $$
        return None,None,None


def tableprint(data,user):
    headers = ["Item", "Category", "Price", "Discount %", "Quantity", "Final Price"]
    total = 0
    hspaces = [8,13,9,11,9,12]
    dspaces = [12,19,9,12,10,12]
    output =""
    for i in range(len(headers)):
        output += "|"+" "*(hspaces[i]-len(headers[i])) + headers[i] + " "*(hspaces[i]-len(headers[i]))
    output += "\n"+"-"*(82)
    for i in data:
        output += "\n"
        for j in range(len(i)):
            no = (dspaces[j]-len(str(i[j])))//2+1
            output +=" "*no+ str(i[j]) + " "*no
        total += i[5]
    e = "select name from user where phone ='"+str(user)+"'"
    cur.execute(e)
    a = cur.fetchall()
    name = a[0][0]
    print("\n User : ",name)
    print(output)
    state = input("Deliver to  :  \n\tState : ")
    while check(state) == False:
        state = input("\tState : ")
    city = input("City : ")
    pin = input("Pin : ")
    t = time(state)
    print("\n Distance + handling fee = Rs.", 10 + 5*t)
    total += 10 + 5*t
    print("\n\tTotal payable amount is ",total)
    address = state + ","+ city + " "+ pin
    return(total,address,state)


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


def check(state):
    with open("distances.csv","r") as file:
        data = csv.reader(file)
        for i in data:
            if i[0] == state:
                break
        else:
            print("Sorry we do not deliver in entered location!")
            return False

def rtd():
    e = "select name, phone from user"
    cur.execute(e)
    a = cur.fetchall()
    output = " "*7 + "Name " + " "*7+"| Phone \n"
    output += "-"*(35)
    for i in a :
        output +="\n\t" +  i[0]+" "*((14-len(a[0])))+str(i[1])
    print(output)
    c = input(" \n Enter phone number :")
    viewpayment(c)


categories = ["Men's Fashion", "Women's Fashion","Kid's Fashion"]
ctg = ["mf", "wf","kf"]
db = mysql.connector.connect(user="root", passwd="area51", host="localhost", database="shop")
cur = db.cursor()
final = {}
