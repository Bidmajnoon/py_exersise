arry = [1,3,5,4,6,9,8,7]
for i in range(1 , len(arry)):
    x = arry[i]
    j = i-1
    while j>=0 and x < arry[j]:
        
        arry[j+1] = arry[j] 
        j -= 1
    arry[j+1]= x
print(arry)
    