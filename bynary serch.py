arry = [1,3,5,6,7,10, 12,15]
x = int(input('enter your number?'))

def bynary_serch(arry, x):
    low = 0
    high = len(arry)-1
    
    while low <= high:
        mid = (low +high)//2
        if arry[mid] == x:
            return mid
        elif x>arry[mid]:
            low = mid+1
        else:
            high = mid - 1
    return -1

result = bynary_serch(arry,x) 
if result ==-1:
    print('the number not in list')
else:
    print(f'number in list index:{bynary_serch (arry, x)}')  
