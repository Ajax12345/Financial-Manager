
import random
def main(): #this is the control panel
    print("Welcome to Comrades and Associates Bank")
    customer_status = input("Are you a returning customer? (yes/no) ")
    if customer_status == "yes":
        answer = input("Do you wish to make a transaction (yes/no)? ")
        if answer == "yes":
            login()

        else:
            print("Thank you for stopping by!")

    else:
        new_answer = input("Thank you for checking out your bank. Do you want to register an account? (y/n) ")
        if new_answer == "y":
            new_costomer_setup()

        else:
            print("Thank you for stopping by!")



def login(): #this validades all user accounts and provides the desired options

    while True:
        name = input("Enter your name: ")
        user_id = int(input("Enter your costomer id: "))
        account_number = int(input("Enter your account number: "))
        valid = validation(user_id)

        if valid:
            print("Credentials authenticated")
            print("Welcome,", name)
            user_action = input("To view your account status, type 'status'. To make a transaction, type 'transaction': ")
            if user_action == "status":
                status(name, user_id, account_number) #just to find the status of the account
            else:
                transaction(name, user_id, account_number) #add or withdraw from the account
            break
        else:
            new_action = input("Your credentials have not been authenticated. Do you want to try again? (y/n)")
            if new_action == "y":
                continue
            else:
                break


def new_costomer_setup(): #this sets up a new customer

    print("Welcome to Comrades and Associates Bank.\n Here, we take customer satisfaction seriously")
    user_name = input("Please enter your name: ")
    f = open('costomers.txt').readlines()
    f = [i.strip('\n') for i in f]
    the_people = []

    for i in f:
        the_people.append(i.split(' '))

        for i in range(len(the_people)):
            the_people[i][1] = int(the_people[i][1])
            the_people[i][2] = int(the_people[i][2])

    the_ids = []
    the_account_numbers = []
    for i in range(len(the_people)):
        the_ids.append(the_people[i][1])
    for i in range(len(the_people)):
        the_ids.append(the_people[i][2])

    while True:
        new_user_id = random.randint(1, 500)
        if new_user_id not in the_ids:
            break

        else:
            continue

    while True:
        new_user_account_number = random.randint(1, 500)
        if new_user_account_number not in the_account_numbers:
            break

        else:
            continue

    print("Your new user id is", new_user_id, "and your new user account number is", new_user_account_number)
    print("Remember these numbers, otherwise, you will not be able to login to your account")
    attempts = 5
    b = open("costomers.txt", 'a')
    basic_file_info = user_name+" "+str(new_user_id)+" "+str(new_user_account_number)
    b.write(basic_file_info)
    b.write("\n")
    b.close()
    first_amount = int(input("Enter the amount of money for your initial deposite: "))
    the_first_day = int(input("Enter the first day: "))
    the_first_month = int(input("Enter the month: "))
    the_first_year = int(input("Enter the year: "))
    the_first_time = int(input("Enter the time: "))
    #there, the customer can complete his first transaction
    the_file_title = user_name+str(new_user_id)+".txt"
    new_file_for_user = open(the_file_title, 'a')
    info_to_write = user_name+" "+str(new_user_id)+" "+str(the_first_day)+"/"+str(the_first_month)+"/"+str(the_first_year)+" at "+str(the_first_time)+" $"+str(first_amount)+" $"+str(first_amount)+" "+str(the_first_month)+" "+str(attempts)
    new_file_for_user.write(info_to_write)
    new_file_for_user.write("\n")
    new_file_for_user.close()



    print("Thank you very much for registering! You can now login and continue your transactions")
    login()


def validation(customer_id): #this verifies the identity of the user
    f = open('costomers.txt').readlines()
    f = [i.strip('\n') for i in f]
    the_people = []

    for i in f:
        the_people.append(i.split(' '))

        for i in range(len(the_people)):
            the_people[i][1] = int(the_people[i][1])
            the_people[i][2] = int(the_people[i][2])

    the_ids = []
    for i in range(len(the_people)):
        the_ids.append(the_people[i][1])



    if customer_id in the_ids:


        return True


    else:
        return False



def transaction(the_name, the_id, the_account_number): #this is were the transactions, adding and withdrawing, are completed
    attempts = 5
    the_file_title = the_name+str(the_id)+".txt"
    user_file = open(the_file_title).readlines()
    user_file = [i.strip('\n') for i in user_file]
    new_user_file = []
    for i in user_file:
        new_user_file.append(i.split(' '))

    the_interest = open('interest_rate.txt').readline()



    my_new_user_file = open(the_file_title, 'a')
    if len(new_user_file) == 1:
        the_length = 0

    else:
        the_length = len(new_user_file) - 1

    print("You have", float(new_user_file[the_length][6].strip("$")), "dollars in your account") #check to be sure the total is not less than or equal to zero
    if float(new_user_file[the_length][6].strip("$")) == 0:
        print("You have zero dollars in your account. You must diposite money") #if less than or equal to zero, must make a deposite

        the_money = int(input("Enter the amount of money you would like to deposit: "))
        the_day = int(input("Enter the day of the month: "))
        the_month = int(input("Enter the month of the year:  "))
        the_year = int(input("Enter the year: "))
        the_time = int(input("Enter the time: "))
        new_total = float(new_user_file[the_length][6].strip("$"))+the_money
        info_to_write = the_name+str(the_id)+str(the_day)+"/"+str(the_month)+"/"+str(the_year)+" at "+str(the_time)+" $"+str(the_money)+" $"+str(new_total)+" "+str(the_month)+" "+str(attempts)
        my_new_user_file.write(info_to_write)
        '''
        here is how I calculated interest and reset the counter for withdrawals. The second-to-last column in the user transaction file contains the number for the month (1-12).
        As long as the user enters a month that is the same as the previous month listed in the file, the counter is decreased if the action is a withdrawal. Else, the counter remains the same. However,
        if the user enters a different month than the last one, the program resets the counter back to five and calculates the interest, because it assumes the end of the previous month occured.
        '''

    else:
        counter = int(new_user_file[the_length][8])
        the_kind = input("Do you want to add or withdraw?(add/withdraw) ")
        if the_kind == "add": #if the user wants to add to his account
            while True:
                the_money = int(input("Enter the amount of money you would like to deposit: "))
                the_day = int(input("Enter the day of the month: "))
                the_month = int(input("Enter the month of the year:  "))
                the_year = int(input("Enter the year: "))
                the_time = int(input("Enter the time: "))
                new_total = float(new_user_file[the_length][6].strip("$"))+the_money
                interest_total = round(((float(new_user_file[the_length][6].strip("$"))+the_money)*float(the_interest))/12, 2) + float(new_user_file[the_length][6].strip("$"))+float(the_money)
                if int(new_user_file[the_length][7]) == the_month:

                    info_to_write = the_name+" "+str(the_id)+" "+str(the_day)+"/"+str(the_month)+"/"+str(the_year)+" at "+str(the_time)+" $"+str(the_money)+" $"+str(new_total)+" "+str(the_month)+" "+str(counter)

                else:
                    info_to_write = the_name+" "+str(the_id)+" "+str(the_day)+"/"+str(the_month)+"/"+str(the_year)+" at "+str(the_time)+" $"+str(the_money)+" $"+str(interest_total)+" "+str(the_month)+" "+str(attempts)

                my_new_user_file.write(info_to_write)
                my_new_user_file.write('\n')
                user_new_answer = input("Do you want to make another deposit? (yes/no) ")
                if user_new_answer == "yes":
                    continue

                else:
                    print("Thank you for doing business with us")
                    break

        else:

            while True: #making a withdrawal
                the_money = int(input("Enter the amount of money you would like to withdraw: "))
                the_day = int(input("Enter the day of the month: "))
                the_month = int(input("Enter the month of the year:  "))
                the_year = int(input("Enter the year: "))
                the_time = int(input("Enter the time: "))
                if int(new_user_file[the_length][7]) != the_month:
                    counter = 5
                    if float(new_user_file[the_length][6].strip("$")) - the_money < 0:
                        print("You do not have enough money in your account. You need to go back and make a deposit.")
                        break

                    else:
                        counter -= 1

                        new_money_total = round((float(new_user_file[the_length][6].strip("$"))*float(the_interest))/12, 2) + float(new_user_file[the_length][6].strip("$")) - the_money
                        info_to_write = the_name+" "+str(the_id)+" "+str(the_month)+"/"+str(the_day)+"/"+str(the_year)+" at "+str(the_time)+" $"+str(the_money)+" $"+str(new_money_total)+" "+str(the_month)+" "+str(counter)
                        my_new_user_file.write(info_to_write)
                        my_new_user_file.write('\n')

                        the_user_answer = input("Do you want to make another withdrawal?(yes/no) ")
                        if the_user_answer == "yes":
                            continue

                        else:
                            print("Thank you for doing business with us!")
                            break

                elif counter == 0:
                    print("You have reached your maximum limit of five withdrawls this month")
                    counter = attempts
                    break

                else:
                    new_money_total = float(new_user_file[the_length][6].strip("$")) - the_money
                    counter -= 1
                    info_to_write = the_name+" "+str(the_id)+" "+str(the_month)+"/"+str(the_day)+"/"+str(the_year)+" at "+str(the_time)+" $"+str(the_money)+" $"+str(new_money_total)+" "+str(the_month)+" "+str(counter)
                    my_new_user_file.write(info_to_write)
                    my_new_user_file.write('\n')
                    the_user_answer = input("Do you want to make another withdrawal?(yes/no) ")
                    if the_user_answer == "yes":
                        continue

                    else:
                        print("Thank you for doing business with us!")
                        break

def status(the_name, the_id, the_account_number): #in case the user wants to see his previous transactions
    the_file_title = the_name+str(the_id)+".txt"
    print(the_file_title)
    my_file = open(the_file_title, 'r')
    print("Here is your entire log of your previous transactions: ")
    print(my_file.read())





main()
