import mysql.connector

def viewpayment(user):
    try:
        e = "select * from "+ "a"+str(user)
        cur.execute(e)
        a = cur.fetchall()
        if len(a) == 0:
            print("No orders!")
        else:
            data = []
            for i in a:
                data.append(i)
            headers = ["Item", "Category" ," Price ", "Quantity", "Date Of Order" ,  "Date Of Delivery","Deliver to ","Address of user"]
            hspaces = [8, 13, 6, 11, 14, 17,15,20]
            dspaces = [15, 20, 10, 10, 19, 20,20,32]
            output = ""
            for i in range(len(headers)):
                output += "|" + " " * (hspaces[i] - len(headers[i])) + headers[i] + " " * (hspaces[i] - len(headers[i]))
            output += "\n" + "-" * (130)
            for row in data:
               row = list(row)
               output += "\n"
               for j in range(len(row)):
                   if str(row[j]) in ctg:
                       for p in range(3):
                           if ctg[p] == str(row[j]):
                               row[j] = categories[j]
                   output += str(row[j]) + (dspaces[j] - len(str(row[j])))*" "
            print(output)
    except mysql.connector.errors.ProgrammingError:
        print("No orders")

categories = ["Men's Fashion", "Women's Fashion","Kid's Fashion"]
ctg = ["mf", "wf","kf"]
db = mysql.connector.connect(user="root", passwd="area51", host="localhost", database="shop")
cur = db.cursor()
final = {}
