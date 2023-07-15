import re
def word_count(file_patch, n):
    count = {}
    with open (file_patch, 'r') as file:
        for line in file:
            words = re.findall(r'\b\w+\b', line)
            for word in words:
                if word in count:
                    count[word] += 1
                else:
                    count[word] = 1

    sort_count = sorted(count.items(), key=lambda x:x[1] , reverse=True)
    return sort_count[:n]
file_patch ='C:/Users/bidmajnoon/Downloads/Ali.txt'
print(word_count(file_patch, 10))
