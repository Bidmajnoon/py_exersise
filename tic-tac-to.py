
bord = [' ' for _ in range(9)]
def display_board():
    row1 = "{}|{}|{}".format(bord[0],bord[1],bord[2])
    row2 ="{}|{}|{}".format(bord[3],bord[4],bord[5])
    row3 = "{}|{}|{}".format(bord[6],bord[7],bord[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()
player = 'x'
def make_move(position):
    global player
    if bord[position] == ' ':
        bord[position] = player
        if player =='x':
            player = 'o'
        else: 
            player = 'x'
    else :
        print("awrong ")
def winner():
    rows = [[bord[0], bord[1], bord[2]], 
            [bord[3], bord[4], bord[5]], 
            [bord[6], bord[7], bord[8]]]
    columns = [[bord[0], bord[3], bord[6]], 
               [bord[1], bord[4], bord[7]], 
               [bord[2], bord[5], bord[8]]]
    diagonals = [[bord[0], bord[4], bord[8]], 
                 [bord[2], bord[4], bord[6]]]
    
    all_lines = rows + columns + diagonals
    
    for line in all_lines:
        if line.count('X') == 3 or line.count('O') == 3:
            return True
    
    return False
def play_game():
    display_board()
    while not winner():
        position = int(input("enter betwin 1 -  9 :"))-1
        make_move(position)
        display_board()
play_game()







