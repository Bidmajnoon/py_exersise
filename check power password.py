
def password():
    while True:
        psw = input('enter your password:')
        if any (i.isdigit() for i in psw) and any (i.isupper() for i in psw) and len(psw) >5:
           print('pasword fine')
           break
        else:
           print('password not powwerfull')
password()