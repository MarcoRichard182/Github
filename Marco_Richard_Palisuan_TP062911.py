#Marco Richard Palisuan
#TP062911

import datetime as time
print("WELCOME TO BANK MOBILE")
print("----------------------")


def login(): #Login_Menu
    while True :
        username = input("Username:")
        password = input("Password:")
        with open("text.txt","r") as fh:
            checker = 0
            for rec in fh:
                reclist = rec.strip().split(";")
                if reclist[0] == username and reclist[1] == password:#to check if the accounts are in text.txt
                    account_type = reclist [2]
                    checker = 1
                    break
            if checker == 0:
                print("username or password invalid")
                print("Please enter the correct username or password!")
                print("")
            else:
                print("Login succesful")
                print("")
                print("Hello",reclist[3])
                account_checker(account_type, reclist) #f
                break


def account_checker(account_type,reclist): #to check the account type
    if account_type == "super":
        superaccount()
    elif account_type == "admin":
        adminaccount(reclist)
    else :
        customeraccount(reclist)


def superaccount():#super account menu
    while True :
        print("1. Create admin account: ")
        print("2. Delete Account")
        print("3. Logout")
        option = input("Choose the options: ")
        if option == "1" :
            while True:
                while True :
                    print ("Please enter the correct data")
                    print("")
                    fullname = input("Fullname:")
                    checker = validation_for_fullname(fullname)#fullname must be in alphabet
                    if checker == fullname:
                        break
                while True  :
                    telephone = input("Telephone:")
                    checker = validation_for_telephone(telephone)#telephone numbers only in digits
                    if checker == telephone:
                        break
                while True :
                    birthdate = input("Birthdate (yyyy-mm-dd) :")
                    checker = validation_for_birthdate(birthdate)
                    if checker == birthdate:
                        break
                while True :
                    gender = input ("Gender:")
                    checker = validation_for_gender(gender)
                    if checker == gender:
                        break
                print ("Fullname:", fullname)
                print ("Telephone:", telephone)
                print ("Birthdate (yyyy-mm-dd) :", birthdate)
                print ("Gender:", gender)
                correct = input("Please check if the data is correct:(Yes/No)")
                if correct == "yes":
                    admindata(fullname, telephone, birthdate, gender) #f
                    break
                else:
                    break
        elif option == "2":
            reclist = edit_customer_checker()
            deleteaccount(reclist)
        elif option == "3":
            print("account logged out")
            print("Enter your account to log in")
            print("")
            login()
            break

def deleteaccount(reclist):
    account=deletecustomeraccount(reclist)
    with open("text.txt")as deleteaccount:
        line=deleteaccount.readlines()
        line[account]=(f"")
    with open("text.txt","w")as deleteaccount:
        deleteaccount.writelines(line)

def deletecustomeraccount(reclist):
    with open("text.txt","r") as customerlist:
        account=-1
        custlist=customerlist.readlines()
        for line in custlist:
            custline=line.split(";")
            account+=1
            if custline[0]==reclist[0] :
                return account
            else:
                pass


def admindata(fullname, telephone, birthdate, gender):#to input the data in text.txt
    fh2 = open("text.txt","a")
    adminid, adminpass = admingenerator()
    fh2.write(f"{adminid};{adminpass};admin;{fullname};{telephone};{birthdate};{gender}\n")
    fh2.close()


def admingenerator():#to autogenerate id and password for admin
    fh3 = open ("text.txt", "r")
    adminidgen = fh3.readlines()
    adminid1 = adminidgen[len(adminidgen)-1]
    adminid2 = adminid1[5:9]
    adminid3 = str(int(adminid2) + 1).zfill(4)
    adminid4 = "Admin" + adminid3
    adminpass = adminid3
    fh3.close()
    return adminid4, adminpass


def adminaccount(reclist):#admin menu
    while True :
        print ("1. Create Customer Account")
        print ("2. Edit Customer Account")
        print ("3. Check History")
        print ("4. Check Customer's specific history")
        print ("5. Change password")
        print ("6. Logout")
        option1 = input("Choose the options :")
        if option1 == "1" :
            while True:
                while True :
                    print ("Please enter the customer data")
                    fullname = input("Fullname  :")
                    checker = validation_for_fullname(fullname)#fullname must be in alphabet
                    if checker == fullname:
                        break
                while True :
                    telephone = input("Telephone    :")
                    checker = validation_for_telephone(telephone)
                    if checker == telephone:
                        break
                while True :
                    birthdate = input("Birthdate (yyyy-mm-dd)    :")
                    checker = validation_for_birthdate(birthdate)
                    if checker == birthdate :
                        break
                while True :
                    gender = input ("Gender :")
                    checker = validation_for_gender(gender)
                    if checker == gender:
                        break
                while True:
                    customertype = input("Customer type:")
                    if customertype == "saving":
                        break
                    elif customertype == "current":
                        break
                    else:
                        print("customer type must be in saving or current")
                while True:
                    balance = float(input("Balance: "))
                    if customertype == "saving" and balance < 100.0:
                        print("Minimum balance is 100")
                    elif customertype == "current" and balance < 500.0:
                        print("Minimum balance is 500")
                    else:
                        break
                print ("Fullname    :", fullname)
                print ("Telephone   :", telephone)
                print ("Birthdate   :", birthdate)
                print ("Gender  :", gender)
                print ("Customertype:", customertype)
                print ("Balance :", balance)
                correct = input("Please check if the data is correct:(Yes/No)")
                if correct == "yes":
                    customerdata(fullname, telephone, birthdate, gender, customertype, balance) #f
                    break
                else:
                    pass
                break
        if option1 == "2" :
            while True:
                print ("Choose What you want to edit")
                print ("1. Edit telephone")
                print ("2. Edit Birthdate:")
                print ("3. Edit Gender:")
                option3 = input("Choose the options :")
                if option3 == "1":
                    reclist = edit_customer_checker()
                    edit_telephone(reclist) #f
                    break
                elif option3 == "2":
                    reclist = edit_customer_checker()
                    edit_birthdate(reclist) #f
                    break
                elif option3 == "3":
                    reclist = edit_customer_checker()
                    edit_gender(reclist) #f
                    break

        elif option1 == "3":
            reclist = edit_customer_checker()
            historymenu(reclist)
        elif option1 == "4":
            reclist = edit_customer_checker()
            date_validation(reclist)
        elif option1 == "5":
            changepassword_admin(reclist)

        elif option1 == "6":
            print("account logged out")
            print("Enter your account to log in")
            print("")
            login() #f



def customerdata(fullname, telephone, birthdate, gender, customertype, balance):
    fh2 = open("text.txt","a")
    customerid, customerpass = customergenerator()
    fh2.write(f"{customerid};{customerpass};customer;{fullname};{telephone};{birthdate};{gender};{customertype};{balance}\n")
    fh2.close()#to add data in text.txt


def customergenerator():
    fh3 = open ("text.txt", "r")
    customeridgen = fh3.readlines()
    customerid1 = customeridgen[len(customeridgen)-1]
    customerid2 = customerid1[5:9]
    customerid3 = str(int(customerid2) + 1).zfill(4)
    customerid4 = "Custo" + customerid3
    customerpass = customerid3
    fh3.close()
    return customerid4, customerpass#customer id and pass gen in sequence


def customeraccount(reclist):
    while True:
        with open("text.txt", "r") as fh:
            for rec in fh:
                account_checker = rec.strip().split(";")
                if reclist[0] == account_checker[0]:
                    break
        reclist = account_checker
        print ("1. Deposit")
        print ("2. Withdraw")
        print ("3. Check Balance")
        print ("4. Change Password")
        print ("5. Check History")
        print ("6. Specific History")
        print ("7. Logout")
        option2 = input("Choose the options :")
        if option2 == "3" :
            check_balance(reclist) #f

        if option2 == "1" :
            deposit(reclist) #f

        if option2 == "2":
            withdraw(reclist) #f

        if option2 == "4":
            changepassword(reclist) #f

        if option2 == "7":
            print("Your account has been logged out")
            print("")
            login() #f
        if option2 == "5":
            historymenu(reclist) #f
        if option2 == "6":
            date_validation(reclist) #customer menu

def historymenu(reclist):
    print("check history")
    print("\nThese are the User Records")
    print("--------------------------")
    with open("history.txt", "r") as fh:
        history = fh.readlines()
        for lines in history:
            line = lines.split(";")
            if line[0] == reclist[0]:
                print(line)
            else:
                pass#customer history menu


def check_balance(reclist):
    print("Your balance is:", reclist [8])
    print("")
    customeraccount(reclist) #customer check balance



def deposit(reclist):#customer deposit
    account=customer_checker(reclist)
    balance=float(reclist[8])
    while True:
        totaldeposit=input("How much you want to deposit:")
        try:
            totaldeposit=float(totaldeposit)
            break
        except:
            print("Deposit must be in number!")
            continue
        break
    currenttime=timenow()
    current_balance=balance+totaldeposit
    current_balance=int(current_balance)
    with open("text.txt")as deposit:
        line=deposit.readlines()
        line[account]=(f"{reclist[0]};{reclist[1]};{reclist[2]};{reclist[3]};{reclist[4]};{reclist[5]};{reclist[6]};{reclist[7]};{current_balance}\n")
    with open("text.txt","w")as deposit:
        deposit.writelines(line)
    with open("history.txt","a") as history_deposit:
        line_deposit=(f"{reclist[0]}; Deposit: {totaldeposit};Current Balance: {current_balance};{currenttime}\n")
        history_deposit.writelines(line_deposit)



def withdraw(reclist):#customer withdraw
    account=customer_checker(reclist)
    balance=float(reclist[8])
    while True:
        totalwithdraw=input("How much you want to withdraw:")
        try:
            totalwithdraw=float(totalwithdraw)
            break
        except:
            print("Withdraw must be in number!")
            continue
        break
    currenttime=timenow()
    current_balance=balance-totalwithdraw
    current_balance=int(current_balance)
    if reclist[7] == "saving" and current_balance < 100.0:
        print("Minimum balance is 100")
    elif reclist[7] == "current" and current_balance < 500.0:
        print("Minimum balance is 500")
    else:
        with open("text.txt")as withdraw:
            line=withdraw.readlines()
            line[account]=(f"{reclist[0]};{reclist[1]};{reclist[2]};{reclist[3]};{reclist[4]};{reclist[5]};{reclist[6]};{reclist[7]};{current_balance}\n")
        with open("text.txt","w")as withdraw:
            withdraw.writelines(line)
        with open("history.txt","a") as history_withdraw:
            line_withdraw=(f"{reclist[0]}; Withdraw: {totalwithdraw};Current Balance: {current_balance};{currenttime}\n")
            history_withdraw.writelines(line_withdraw)

def customer_checker(reclist):#to find account
    with open("text.txt","r") as customerlist:
        account=-1
        custlist=customerlist.readlines()
        for line in custlist:
            custline=line.split(";")
            account+=1
            if custline[0]==reclist[0]:
                return account
            else:
                pass


def changepassword(reclist):
    account=customer_checker(reclist)
    password=reclist[1]
    while True :
        new_password=input("Enter your new password:")
        checker = validation_for_edit_password(new_password)
        if checker == new_password:
            break
    with open("text.txt")as newpassword:
        line=newpassword.readlines()
        line[account]=(f"{reclist[0]};{new_password};{reclist[2]};{reclist[3]};{reclist[4]};{reclist[5]};{reclist[6]};{reclist[7]};{reclist[8]}\n")
    with open("text.txt","w")as newpassword:
        newpassword.writelines(line)#change password


def changepassword_admin(reclist):
    account=customer_checker(reclist)
    password=reclist[1]
    while True :
        new_password=input("Enter your new password:")
        checker = validation_for_edit_password(new_password)
        if checker == new_password:
            break
    with open("text.txt")as newpassword:
        line=newpassword.readlines()
        line[account]=(f"{reclist[0]};{new_password};{reclist[2]};{reclist[3]};{reclist[4]};{reclist[5]};{reclist[6]}\n")
    with open("text.txt","w")as newpassword:
        newpassword.writelines(line)#change admin password


def edit_customer_checker():#to find account
    while True :
        username = input("Username:")
        with open("text.txt","r") as fh:
            checker = 0
            for rec in fh:
                reclist = rec.strip().split(";")
                if reclist[0] == username:
                    checker = 1
                    break
            if checker == 0:
                print("username not found")
            else:
                return reclist

                break


def edit_customer_account(reclist):#to find account index
    with open("text.txt","r") as customerlist:
        account=-1
        custlist=customerlist.readlines()
        for line in custlist:
            custline=line.split(";")
            account+=1
            if custline[0]==reclist[0] and reclist[2]=="customer":
                return account
            else:
                pass


def edit_telephone(reclist):#edit telephone
    account=edit_customer_account(reclist)
    telephone=reclist[4]
    while True :
        new_telephone=input("Enter your new telephone number:")
        checker = validation_for_telephone(new_telephone)
        if checker == new_telephone:
            break
    with open("text.txt")as newtelephone:
        line=newtelephone.readlines()
        line[account]=(f"{reclist[0]};{reclist[1]};{reclist[2]};{reclist[3]};{new_telephone};{reclist[5]};{reclist[6]};{reclist[7]};{reclist[8]}\n")
    with open("text.txt","w")as newtelephone:
        newtelephone.writelines(line)


def timenow():#import time
     current_time = time.datetime.now()
     current_time = current_time.strftime("%Y-%m-%d; at %H:%M:%S")
     return current_time


def date_validation(reclist):#history date validation
    while True:
        startdate = input("Start date (yyyy-mm-dd): ")
        lastdate = input("Last date (yyyy-mm-dd): ")
        point = 0
        try:
            start_date = startdate.split("-")
            last_date = lastdate.split("-")
            start_year, start_month, start_day = start_date
            last_year, last_month, last_day = last_date
            start_year = int(start_year)
            start_month = int(start_month)
            start_day = int(start_day)
            last_year = int(last_year)
            last_month = int(last_month)
            last_day = int(last_day)
            months_with_30_days = [4,6,9,11]
            months_with_31_days = [1,3,5,7,8,10,12]
            if (start_month >= 1 and start_month <= 12) and len(start_date) == 3:
                if start_month in months_with_31_days and (start_day >= 1 and start_day <= 31):
                    point = 1
                elif start_month in months_with_30_days and (start_day >= 1 and start_day <= 30):
                    point = 1
                elif start_month == 2 and (start_day >= 1 and start_day <= 28):
                    point = 1
                elif start_month == 2 and (start_year % 4 == 0 and start_year % 400 == 0) and (start_day >= 1 and start_day <= 29):
                    point = 1
                elif start_month == 2 and (start_year % 4 == 0 and start_year % 100 != 0) and (start_day >= 1 and start_day <= 29):
                    point = 1
                else:
                    1/0
                if point == 1 and len(last_date) == 3 and (last_month >= 1 and last_month <= 12):
                    if last_month in months_with_31_days and (last_day >= 1 and last_day <= 31):
                        pass
                    elif last_month in months_with_30_days and (last_day >= 1 and last_day <= 30):
                        pass
                    elif last_month == 2 and (last_year % 4 == 0 and last_year % 400 == 0) and (last_day >= 1 and last_day <= 29):
                        pass
                    elif last_month == 2 and (last_year % 4 == 0 and last_year % 100 != 0) and (last_day >= 1 and last_day <= 29):
                        pass
                    else:
                        1/0
                else:
                    1/0
            else:
                1/0
        except:
            print("Invalid Date Input. Please re-write.")
            continue
        historydate = start_year, start_month, start_day, last_year, last_month, last_day
        historydate = list(historydate)
        print_specific_transaction_history(reclist, historydate) #f
        break

def print_specific_transaction_history(reclist, historydate):
    with open("history.txt", 'r') as file:
        file = file.readlines()
        start_year, start_month, start_day, last_year, last_month, last_day = historydate
        start_year = str(start_year).zfill(4)
        start_month = str(start_month).zfill(2)
        start_day = str(start_day).zfill(2)
        last_year = str(last_year).zfill(4)
        last_month = str(last_month).zfill(2)
        last_day = str(last_day).zfill(2)
        startdatehistory = f'{start_year}-{start_month}-{start_day}'
        lastdatehistory = f'{last_year}-{last_month}-{last_day}'
        print("Transaction History")
        print("\n")
        point = 0
        for line in file:
            data = line.split(";")
            if data[0] == reclist[0]:
                if startdatehistory <= data[3] <= lastdatehistory:
                    print (f"{data[1]}|{data[2]}|{data[3]}|{data[4]}")
                    point = 1
        if point == 0:
            print("No Transaction Found")#print specific history



def validation_for_fullname(fullname):
    check = 0
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ "
    for eachcharacter in fullname:
        if eachcharacter not in characters:
            check = 1
    if check == 1:
        print("Invalid name! Please use only letters")
    else:
        return fullname#validation fullname


def validation_for_telephone(telephone):
    try:
        if len(telephone) >=12 and len(telephone) <=15:
            if telephone [1:].isdigit():
                return telephone
            else:
                1/0
        else:
            1/0
    except:
        print("Only digits are allowed and must be 12-15 digit!")#validation telephone


def validation_for_birthdate(birthdate):
    try:
        start_date = birthdate.split("-")
        start_year, start_month, start_day = start_date
        start_year = int(start_year)
        start_month = int(start_month)
        start_day = int(start_day)
        months_with_30_days = [4,6,9,11]
        months_with_31_days = [1,3,5,7,8,10,12]
        if (start_month >= 1 and start_month <= 12) and len(start_date) == 3:
            if start_month in months_with_31_days and (start_day >= 1 and start_day <= 31):
                return birthdate
            elif start_month in months_with_30_days and (start_day >= 1 and start_day <= 30):
                return birthdate
            elif start_month == 2 and (start_day >= 1 and start_day <= 28):
                return birthdate
            elif start_month == 2 and (start_year % 4 == 0 and start_year % 400 == 0) and (start_day >= 1 and start_day <= 29):
                return birthdate
            elif start_month == 2 and (start_year % 4 == 0 and start_year % 100 != 0) and (start_day >= 1 and start_day <= 29):
                return birthdate
            else:
                1/0
        else:
            1/0
    except:
        print("Invalid Date Input !")#validation birthdate


def validation_for_gender(gender):
    try:
        if gender.strip().isalpha():
            return gender
        else:
            1/0
    except:
        print("Only letters are allowed")#gender validation


def edit_birthdate(reclist):
    account=edit_customer_account(reclist)
    birthdate=reclist[5]
    while True :
        new_birthdate= input("Enter your new birthdate:")
        checker = validation_for_birthdate(new_birthdate)
        if checker == new_birthdate:
            break
    with open("text.txt")as newbirthdate:
        line=newbirthdate.readlines()
        line[account]=(f"{reclist[0]};{reclist[1]};{reclist[2]};{reclist[3]};{reclist[4]};{new_birthdate};{reclist[6]};{reclist[7]};{reclist[8]}\n")
    with open("text.txt","w")as newbirthdate:
        newbirthdate.writelines(line)#edit birthdarte

def edit_gender(reclist):
    account=edit_customer_account(reclist)
    gender=reclist[6]
    while True :
        new_gender=input("Enter your new gender:")
        checker = validation_for_gender(new_gender)
        if checker == new_gender:
            break
    with open("text.txt")as newgender:
        line=newgender.readlines()
        line[account]=(f"{reclist[0]};{reclist[1]};{reclist[2]};{reclist[3]};{reclist[4]};{reclist[5]};{new_gender};{reclist[7]};{reclist[8]}\n")
    with open("text.txt","w")as newgender:
        newgender.writelines(line) #edit gender


def validation_for_edit_password(new_password):
    try:
        if len(new_password) >= 8 and len(new_password) <= 12 :
            return new_password
        else:
            1/0
    except:
        print("Password must be between 8-12") #password validation





login()
