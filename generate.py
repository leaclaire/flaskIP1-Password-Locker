import string    
import random # define the random module  
S = 10  # number of characters in the string.  
# call random.choices() string module to find the string in Uppercase + numeric data.  
ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
# print("The randomly generated string is : " + str(ran)) # print the random data  

def getPassLength():
    '''
    retrive the length of a password
    '''
    length = input("Length of your password: ")
    return int(length)

def passwordGenerator(length = 8):
    '''
    generates a random password having the specified length
    '''
    password = list(string.ascii_letters + string.punctuation + string.digits)
    random.shuffle(password)
    random_password = ''.join(random.choices(password, k=length))

    return random_password