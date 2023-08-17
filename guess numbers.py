import random
number = int(input('enter a number betwi 1- 50 :  '))
def random_number(number):
    num = random.randint(1,51)
    if 0>number or number>51:
        print('enter corrct number')
        return
    count = 0
    while number != num:
        print('incorevt try again ')
        number = int(input('enter a number betwi 1- 50 :  '))
        count +=1
    return f'num {num},count{count}'
   
print(random_number(number))