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

print(bynary_serch(arry,x))    
