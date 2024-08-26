import random
import string

def random_passwords(length=8):
    
    #define the main characters
    password_list = string.ascii_lowercase + string.ascii_uppercase + srting.digits + string.punctuation
    Password_list = []
    for _ in range(length):
        password_list.apend(random.choice(letters))
        password = ''.join(password_list)
    return password

#asking user to enter desired password
length = int(input("Please enter desired pssword length: "))

#generate password
password = generate_list(length)
print("Generate password: " +password)

  

    
    
    
