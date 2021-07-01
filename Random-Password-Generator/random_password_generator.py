import string,random
#Generating ASCII of letters numbers and digits
Letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation
#Combining All the ASCII values
All=Letters+numbers+symbols
print("Welcome to the password Generator")
while 1:
    #Taking password Length and counts
    password_length = int(input("What would be your password Length?: "))
    password_count = int(input("How many passwords do you require?: "))
    #loop for number of passwords
    for i in range(password_count):
        password = ""
        #Loop for generating random passwords
        for j in range(0,password_length):
            password_char=random.choice(All)
            password = password + password_char
        print("The Generated Passwords are: ",password)
