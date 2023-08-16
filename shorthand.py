name = str(input('enter your Organization name ='))
sp = name.split(' ')
result = [word[0] for word in sp]
r2 = ''.join(result)
print(r2)

