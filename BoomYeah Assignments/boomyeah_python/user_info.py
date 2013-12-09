#Create a python program wherein the user is asked for the following information:

#First Name
#Last Name
#Birthdate
#Address
#Email address

#After the user gave the information, the program will display the following:

#First Name
#Initials
#Address
#Age
#Age status (e.g. You're too old, You're too young)
#Email address

from datetime import date

def main():
    print
    first_name = raw_input("Enter your first name:")
    last_name = raw_input("Enter your last name:")
    birthdate = raw_input("Enter your birthdate (mm/dd/yyyy):")
    addr = raw_input("Enter your address:")
    email_addr = raw_input("Enter your email address:")
    print
    print "Here are the details you entered"
    print"_______________________________"
    print "Your first name is", first_name
    print "Your Initials are", first_name[0] +'.'+last_name[0]+'.'
    print 'Your Address is', addr
    print "Your age is", age(birthdate)
    print "You are", age_status(age)+":)"
    print "Your Email Address is", email_addr


def age(birthdate):

    #Splitting the given birthdate.
    birthdate = birthdate.split('/')
    #prints the current date using date object
    current_date = date.today()
    today_date = str(current_date)
    today_date = today_date.split('-')
    #Assiging integer type date formats to a and b variables
    #since the dateformats are stored as string formats
    a = int(today_date[0])
    b = int(birthdate[2])

    result = a-b

    return result

def age_status(age):

    if age >=60:
        return "You are too old!"

    if age >=35:
        return "You are quite old"

    if age <=18:
        return "You are too young"


main()