import queries_data2 as qdata
import profile_data as pdata
import cart_data as cdata
import check_out as cout
import Past_order as porders
pdata.usertable()

def ai(c):
    for i in categories:
        cword = list(i.split(" "))
        checkper = []
        check = 0
        for j in (list(c.split(" "))):
            for k in cword:
                inpletter = list(j)
                for ctgletter in k:
                    if ctgletter in inpletter:
                        check += 1
                    check = check*100/len(k)
        checkper.append(check)
    i = checkper.index(max(checkper))
    s = "Did you mean ?", categories[i], "(y/n)"
    x = input(s)
    if x == "y" or x == "Y":
        return i, True
    else:
        return i, False


def view(q):
    key = []
    for i in q:
        i = i.strip()
        i = i.lower()
        for j in range(len(categories)):
            if categories[j] == i:
                key.append(j)

        if i not in categories:
            print("Category ", i, "does not exist")
            j, check = ai(i)
            if check:
                key.append(j)
    return key


categories = ["men's fashion", "women's fashion","kid's fashion"]
# accessories",
print("---------------")
print("ONLINE SHOPPING")
print("---------------")
while True:
    print()
    print("---------")
    print("MAIN MENU")
    print("---------")
    print()
    print("1.Your profile\n2.View items \n3.View cart  \n4.Check out\n5.View Orders \n6.Quit ")
    choice = input("\t Enter choice (1-6) :")
    choice = choice.strip()
    if choice == "1":
        print()
        print("---------")
        print("USER DETAILS")
        print("---------")
        print()
        pdata.user()

    if choice == "2":
        print()
        print("------------")
        print("ITEM DETAILS")
        print("------------")
        print()
        main = True
        while main:
            print("Choose category:")
            c = 0
            for i in categories:
                print("\t", i.capitalize(), end="    ")
                c = c + 1
            print()
            choice1 = (input("  Press all to view all items, * to go back "))
            choice1 = choice1.lower()
            choice1 = choice1.strip()
            if choice1 == "*":
                break
            else:
                if choice1 == "all":
                    key = [x for x in range(len(categories))]
                    qdata.view(key)
                else:
                    choice1 = list(choice1.split(","))
                    key = view(choice1)
                    if len(key) != 0:
                        qdata.view(key)

                while len(key) != 0:
                    print()
                    print("1.Sort results  \n2.Add items in cart \n* To Go back")
                    corf = input(" \t Enter your choice (1-2) :")
                    corf = corf.strip()
                    if corf == "1":
                        print("Sort by final price : \n \t1.Low to high \n \t2.High to low \n\t3.Maximum Discount")
                        c = input("Enter choice (1-3): ")
                        c = c.strip()
                        if c == "1":
                            order = "asc"
                            qdata.sort(key, order, True)
                        elif c == "2":
                            order = "desc"
                            qdata.sort(key, order, True)
                        elif c == "3":
                            order = "desc"
                            qdata.sort(key, order, False)
                        else:
                            print("Wrong choice!")
                        print()
                    elif corf == "2":
                        item = input("Enter item you want : ")
                        item = item.strip()
                        item = item.title()
                        if item == "*":
                            pass
                        else:
                            itemadded, ctgofi, enter = qdata.itemcategory(item, key)
                            while enter:
                                corf2 = input(" 1. Confirm addition to cart  \n\t (* to go back) Enter :")
                                if corf2 == "1":
                                    if len(pdata.users) == 0:
                                        print("Please register ")
                                        pdata.insertuser()
                                    select = pdata.selecteduser()
                                    cdata.add(select, ctgofi, itemadded)
                                    cp = input("\t 1.View final bill \n\t * Continue shopping \nEnter:")
                                    if cp == "1":
                                        total,address,state = cdata.bill(select)
                                        finalc = input("\tProceed to pay? (y/n) ")
                                        if finalc == "y":
                                            cout.payment(total,select,address,state)
                                            ff = input("1.Continue shopping \n2. Quit")
                                            if ff == "1":
                                                choice = "3"
                                            elif ff == "2":
                                                choice = "6"
                                            else:
                                                print("Please choose from given options")
                                            key = []
                                            main = False
                                            break
                                        elif finalc == "n":
                                            pass
                                        else:
                                            print("Please choose from given options!")
                                    else:
                                        pass
                                    break
                                elif corf2 == "*":
                                    break
                                else:
                                    print("Please choose from given options.")
                    elif corf == "*":
                        break
                    else:
                        print("Wrong choice!")

    if choice == "3":
        print()
        print("------------")
        print("CART DETAILS")
        print("------------")
        print()
        if len(pdata.users) == 0:
            print("No registered Users!")
        else:
            user = pdata.selecteduser()
            cdata.view(user)
            while True:
                print("\t1.Add item\n\t2.Delete item\n\t3.Proceed to Pay \n\t4.Select another user")
                c = input(" (* to go back)  Enter(1-4) : ")
                c = c.strip()
                if c == "1":
                    item = input("\tEnter Item :")
                    item = item.strip()
                    itemadded, ctgofi, enter = qdata.itemcategory(item)
                    if enter:
                        cdata.add(user, ctgofi, itemadded)
                elif c == "2":
                    itemdel = input("\tEnter item : ")
                    itemdel = itemdel.strip()
                    itemdel = itemdel.capitalize()
                    cdata.delete(itemdel, user)
                elif c == "3":
                    if user not in cdata.cart :
                        print("Cart empty!!")
                    else:
                        total, address, state = cdata.bill(user)
                        cout.payment(total, user, address, state)
                        ff = input("1.Continue shopping \n2. Quit")
                        if ff == "1":
                            choice = "3"
                        elif ff == "2":
                            choice = "6"
                        else:
                            print("Please choose from given options")
                        break
                elif c == "4":
                    enteruser = input("Enter phone number :")
                    enteruser = enteruser.strip()
                    if int(enteruser) in pdata.users:
                        user = enteruser
                        print(user,enteruser)
                        cdata.view(enteruser)
                elif c =="*":
                    break
                else:
                    print("Choose from given options")


    if choice == "4":
        print()
        print("---------")
        print("CHECK OUT ")
        print("---------")
        print()
        if pdata.users == []:
            print("No registered users!\n Cart empty")
        else:
            user= pdata.selecteduser()
            total, address, state = cdata.bill(user)
            cout.payment(total, user, address, state)
            ff = input("1.Continue shopping \n2. Quit")
            if ff == "1":
                choice = "3"
                print(choice)
            elif ff == "2":
                choice = "6"
            else:
                print("Please choose from given options")

    if choice == "5":
        print()
        print("-------------------")
        print("PAST ORDERS DETAILS")
        print("-------------------")
        print()
        user = pdata.selecteduser()
        porders.viewpayment(user)
        while True:
            c = input("\n1.View orders by different user \n(* to continue) Enter : ")
            if c == "1":
                cdata.rtd()
            else:
                break
    if choice == "6":
        print("Thank You")
        break
    else:
        if choice not in ["1","2","3","4","5"]:
            print("Wrong Choice")
        else:
            pass
    # see how long is left for delivery, order total

    #choice 4

# and break  loop.
#.#
