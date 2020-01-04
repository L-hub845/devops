import re
fname = input("Please write first name: ")
alpha_exp = r'[a-zA-Z]+'
while re.fullmatch(name_exp, fname) == None:
    print("Not a vailed firstname")



lname = input(" Please write last name: ")
alpha_exp = r'[a-zA-Z]+'


dob = input(" Enter your date of birth in the format DD/MM/YYYY: ")

email = input(" Enter your email: ")

zipcode = input(" Please enter zip code: ")

city = input(" Please enter city: ")

state = input(" Enter state: ")

race = input(" If you like, please enter race: ")

age = input(" Please enter age: ")

sex = input(" Please enter sex: ")
