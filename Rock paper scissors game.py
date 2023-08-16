gamer1 = str(input("gamer1 enter your select"))
gamer2 = str(input('gamer2 enter yor select '))

def game(gamer1, gamer2):
    if (gamer2 =='rock' and gamer1== 'paper') or (gamer1=='snip' and gamer2 == 'paper') or(gamer1 =='rock' and gamer2 =='snip'):
        return 'winner=gamer1'
       
    if gamer1 == gamer2:
        return'play again'     
    else:
        'winner== gamer2'

print(game(gamer1,gamer2))