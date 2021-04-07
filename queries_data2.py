import mysql.connector
import data1


def strike(text):
    s = ""
    for c in text:
        a = u'\u0336' + c
        s += a
    return s


def view(tkey):
    c = 1
    for i in tkey:
        print()
        print(" Items in", categories[i], " are:")
        print()
        tname = ctg[i]
        e = "select item,price,discount from " + tname
        cur.execute(e)
        a = (cur.fetchall())
        for x in a:
            item = x[0].capitalize()
            price = x[1]
            discount = x[2]
            if str(discount) != "0":
                op = strike(str(price))
                statement = str(item + "Rs." + op + "(-" + str(discount) + "%)  Rs.") + str(int(price) + int(price)-int(price) * int(discount) / 100)
                print("\t",item, "Rs.", op, "(-", discount, "%)  Rs.", int(price) - int(price) * int(discount) / 100, "  "*(38-len(str(statement))),end="")
            else:
                statement = item + ": Rs"+ str(price)
                #print(str(statement),len(statement),len(str(statement)))

                print( "\t", item, ": Rs", price, " "*(38 - len(str(statement))), end = "  ")
            if c%2 == 0:
                print()
            c=c+1
        print()

def sort(tkey, order, check):
    for i in tkey:
        tname = ctg[i]
        print()
        print("Item's in ",categories[i],"are:")
        print()
        if check:
            e = "select item,price - price*discount/100 from " + tname + " order by price-price*discount/100 " + order
            cur.execute(e)
            a = (cur.fetchall())
            c = 1
            for x in a:
                print("\t\t", x[0], ": Rs.", x[1], end="")
                if c%3 ==0:
                    print()
                c=c+1
            print()

        else:
            e = "select item,price,discount from " + tname + " order by discount " + order
            cur.execute(e)
            a = (cur.fetchall())
            c=1
            for x in a:
                if x[2] != 0:
                    statement = str( x[0]+ " "+ str(x[2])+ "%off"+ " :Rs")+str(int(x[1])*int(x[2])/100)
                    print("\t\t",  x[0], " ", x[2], "%off", " :Rs",int(x[1])- int(x[1])*int(x[2])/100, " "*(25-len(statement)), end="")
                else:
                    statement = str(x[0]+ " :Rs")+str(int(x[1]))
                    print("\t\t",  x[0], " :Rs", int(x[1])," "*(25-len(statement)), end="")
                if c%2 == 0:
                    print()
                c = c+1
            print()


def itemcategory(item, tkey = [0,1,2]):
    category = []
    pcategory = []
    for i in tkey:
        tname = ctg[i]
        printname = categories[i]
        e = "select * from " + tname + " where item='" + item + "'"
        cur.execute(e)
        a = cur.fetchall()
        if len(a) != 0:
            category.append(tname)
            pcategory.append(printname)

    if len(category) > 1:
        print("Choose category:")
        print("\t", pcategory)
        cat = input(" \t Enter : ")
        cat = cat.strip()
        cat = cat.lower()
        while cat not in pcategory:
            print(cat, pcategory)
            print("Item does not exist.")
            return None, None, False

        else:
            for i in range(len(pcategory)):
                if cat == pcategory[i]:
                    cat = category[i]
                    break
    elif len(category) == 0:
        print("Item does not exist")
        return None, None, False
    else:
        cat = category[0]
    itemdetail(item, cat)
    return item, cat, True


def itemdetail(item, cat):
    e = "select * from " + cat + " where item='" + item+"'"
    cur.execute(e)
    a = cur.fetchall()
    for i in a:
        for j in range(len(ctg)):
            if ctg[j] == i[1][:2]:
                j = categories[j]
                break
        if i[3] != 0:
            print(i[0], " (", j, ") ", " - Rs ", i[2]- i[2] * i[3] / 100)
        else:
            print(i[0], " (", j, ") ", " - Rs ", i[2])


data1.createdb()
data1.insertvalues()


ctg = ["mf", "wf", "kf"]
db = mysql.connector.connect(user="root", passwd="area51", host="localhost", database="shop")
cur = db.cursor()
categories = ["men's fashion", "women's fashion", "kid's fashion"]
