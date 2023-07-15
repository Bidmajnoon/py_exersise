import re
def extract_email_addresses(path_file):
    emai_addres = []
    patern =r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    with open(path_file, 'r')as file:
        for line in file :
            matches = re.findall(patern ,line)
            emai_addres.extend(matches)
    return emai_addres
path_file ='C:/Users/bidmajnoon/Downloads/Ali.txt'
print(extract_email_addresses(path_file))
