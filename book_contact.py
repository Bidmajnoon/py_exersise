
book_contact = {}

def add_contact():
    name = str(input('enter your name'))
    address = str(input('enter addres'))
    phone =  str(input('enter your phone number'))
    book_contact[name] ={'addres:':address,'phone' :phone}

def serch():
    serch = input('enter your name')
    if serch in book_contact:
        print(book_contact[serch])
    else:
        print('the contact not in book_contact')

def delet_contact():
    delet = input('enter contact')
    if delet in book_contact:
        del book_contact[delet]
        print('the contact deleta sucessful')
    else:
        print('contact not in book_contact')
def detail():
    if not book_contact:
        print('no contact in book_contact ')
    else:
        for name, contact in book_contact.items():
            print('name:', name)
            print('detail', contact)
            
            print('---------------')

def main ():
    while True:

        do = int(input('enter what do 1:ad  2:serch  3 :del 4:show contact 5: exit' ))
        if do == 1:
            print(add_contact())
        elif do == 2:
            print(serch())
        elif do == 3:
            print(delet_contact())
        elif do == 4:
            print(detail())
        elif do == 5:
           break
        else:
            print('enter a correct number ')

main()