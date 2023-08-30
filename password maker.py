import random 
import string
def make_pass(lenth):
    char = string.ascii_letters + string.digits + string.punctuation
    pas =''.join(random.choice(char) for i in range(lenth)) 
    return pas
print(make_pass(7))