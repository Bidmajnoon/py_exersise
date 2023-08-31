import random 
import string
def make_pass(lenth):
    char = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for i in range(lenth):
        password += random.choice(char)
        
    return password
print(make_pass(7))
