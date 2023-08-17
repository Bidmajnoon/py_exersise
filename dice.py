import random
user_input =input
while True :
    x = random.randint(1, 6)
    user_input = input('continue')
    if user_input == "exit":
        break
    print(x)

