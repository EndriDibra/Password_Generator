# using the required libraries
import random
import re

# Entering the desired length of password
length = int(input("Choose length for your password, it should be at least 14 \n"))

# if the length of password(string) is less than 14 then input will be requested again
while length < 14:

    print("Error! Try again.")
    length = int(input("Choose length for your password, it should be at least 14! \n"))

else:

    # list1: a list with digits 0-9
    list1 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    # list2: a list with letters A-M
    list2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']

    # list3: a list with letters N-Z
    list3 = ['N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # list4: a list with letters a-m
    list4 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'í', 'j', 'k', 'l', 'm']

    # list5: a list with letters n-z
    list5 = ['n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    # list6: a list with symbols
    list6 = ['#', '$', '!', '&', '%', '(', ')', '*', '@', '^']

    # list7 : contains random characters of the other lists
    list7 = list1 + list2 + list3 + list4 + list5 + list6

    # Creating variable for password and initializing it as null
    password = " "

    # Initializing password with a for loop
    for i in range(length):

        password += random.choice(list7)

    # Every time that password does not contain the required characters, it will be re-generated
    while not (re.search("[a-z]", password) and re.search("[A-Z]", password) and re.search("[0-9]",password) and re.search("[#$!&%()*@^]", password)):

        # Setting password to null again, to re-generated
        password = " "

        for i in range(length):
            password += random.choice(list7)

    # If password contains all the required characters, it will be printed
    else:

        # printing the final result (user's password)
        print(password)
