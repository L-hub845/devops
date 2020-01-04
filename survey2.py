
print("The survey about you")
# this is the regular expression that checks for a-z A-Z characters only
alpha_exp = r'[a-zA-Z]+'
# this is the input line that ask for firstname
firstname = str(input(" What is your first name? "))

# this is the while loop that runs the vailidation checks
while re.fullmatch(name_exp, fname) == None:
    print("Not a vailed firstname" )
    firstname = str(input("Please enter your first name"))

lastname = str(input(" What is your last name? "))
# this is a while loop that runs the vailidation checks 
while re.fullmatch(name_exp, fname) == None:
    print("Not a vailed lastname") 
    lastname = str(input(please enter your last name"))
    
# this is the loop that runs the validation check for the 2
# and day along with the 4 digit year 
dob = input("Enter you date of birth in the format DD/MM/yyyy")
while re.fullmatch(r'\d{2}\/\d{2}\/\d{4}', dob) == None:
    print("The Date of birth you provided is correct")
    dob = input("Enter your date of birth in format DD/MM/YYYY")

# this is the input line that ask for the email
email = str(input(" Enter your email "))
# this is the while loop that runs the vailidation checks
    

) 

