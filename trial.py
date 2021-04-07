# categories = ["Men's Fashion", "Women's Fashion", ]   # "Tv and Appliances","Mobiles, laptops and accessories",
# c = input("Enter : ")
# c=c.capitalize()
# for i in range(len(categories)):
#         if categories[i] == c:
#             print("Found")
#         elif categories[i] != c:
#             check = 0
#             for j in categories[i]:
#                 if j in c:
#                     check += check
#             check = check*len(categories[i])/100
#             if check >= 40 or c in categories[i]:
#                 print("Did you mean ", categories[i], end=", ")
import csv
import mysql.connector
# import datetime
# d0 = datetime.date(2009, 8, 18)
# d1 = datetime.date(2008, 9, 26)
# delta = d1 - d0
# x = (delta.days)
# print(x)
#
# db = mysql.connector.connect(user="root", passwd="area51", host="localhost", database="shop")
# cur = db.cursor()
#
# def viewpayment(user):
#     e = "select * from "+ "a"+str(user)
#     cur.execute(e)
#     a = cur.fetchall()
#     if len(a) == 0:
#         print("No orders!")
#     else:
#         data = []
#         for i in a:
#             data.append(i)
#         headers = ["Item", "Category" ,"Price", "Quantity", "Date Of Order" ,  "Date Of Delivery"]
#         hspaces = [8, 13, 6, 9, 14, 17]
#         dspaces = [15, 20, 8, 12, 15, 12]
#         output = ""
#         for i in range(len(headers)):
#             output += "|" + " " * (hspaces[i] - len(headers[i])) + headers[i] + " " * (hspaces[i] - len(headers[i]))
#         output += "\n" + "-" * (86)
#         for row in data:
#            row = list(row)
#            output += "\n"
#            for j in range(len(row)):
#                if j == 5:
#                    print(row[j])
#                if str(row[j]) in ctg:
#                    for p in range(3):
#                        if ctg[p] == str(row[j]):
#                            row[j] = categories[j]
#                output += str(row[j]) + (dspaces[j] - len(str(row[j])))*" "
#         print(output)
#
#
# categories = ["Men's Fashion", "Women's Fashion","Kid's Fashion"]
# ctg = ["mf", "wf","kf"]
#
# cart = {696969:[["ctf","ANushree",2],["cfr","Bajaj",3]], 2:[[2,"AAshna"], [3,"chd"]], 3:[[2,"ew"]]}
# viewpayment(696969)
# print(d)
# d[3].pop(0))
# print(d)
# if d[3] == []:
#     d.pop(3)
# # print(d)
# def time(state):
#     with open("distances.csv","r") as file:
#         data = csv.reader(file)
#         for row in data:
#             if row[0] == state:
#                 time = row[1]
#                 break
#         else:
#             time = 0
#         time = float(time)//105+2
#         if time > 10:
#             time = time-10
#     return time
# x= time("kerala")
# y = time("punjab")
# print(x,y)


import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
fp = open(textfile, 'rb')
# Create a text/plain message
msg = MIMEText(fp.read())
fp.close()

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'The contents of %s' % textfile
msg['From'] = me
msg['To'] = you

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP('localhost')
s.sendmail(me, [you], msg.as_string())
s.quit()
