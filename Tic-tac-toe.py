#Tic-Tac-Toe

"""
    _! _| _
    _| _| _
    _| _|_

"""
theboard = {
    'Top-Left':'','Top-mid':'','Top-right':'',
    'Mid-Left':'','Mid-mid':'','Mid-right':'',
    'Bottom-Left':'','Bottom-mid':'','Bottom-right':''
}
def ActualBoard(Board):
    print(Board['Top-Left'] + ' | ' + Board['Top-mid'] + ' | ' + Board['Top-right'] )
    print('-- -- --')
    print(Board['Mid-Left'] + ' | ' + Board['Mid-mid'] + ' | ' + Board['Mid-right'])
    print('-- -- --')
    print(Board['Bottom-Left'] + ' | ' + Board['Bottom-mid'] + ' | ' + Board['Bottom-right'])

#checking for win
def TestforWin(Board):
    won = False

    if (Board['Top-Left'] == Board['Top-mid'] == Board['Top-right'] and Board['Top-Left']!=''):
        #print(1)
        won = True
    elif(Board['Mid-Left'] == Board['Mid-mid']  == Board['Top-right'] and Board['Mid-Left'] !=''):
        #print(2)
        won = True
    elif (Board['Bottom-Left'] == Board['Bottom-mid']  == Board['Bottom-right'] and Board['Bottom-Left']!=''):
        #print(3)
        won = True
    elif (Board['Bottom-Left'] == Board['Mid-Left']  == Board['Top-Left'] and Board['Bottom-Left']!=''):
        #print(4)
        won = True
    elif (Board['Bottom-mid'] == Board['Mid-mid']  == Board['Top-mid'] and Board['Bottom-mid']!=''):
        #print(5)
        won = True
    elif (Board['Bottom-right'] == Board['Mid-right']  == Board['Top-right'] and Board['Bottom-right'] !=''):
        #print(6)
        won = True
    elif (Board['Bottom-right'] == Board['Mid-mid']  == Board['Top-Left'] and Board['Bottom-right'] !=''):
        won = True

    elif (Board['Bottom-Left'] == Board['Mid-mid']  == Board['Top-right'] and Board['Bottom-Left'] !=''):
        won = True

    return won

#lets say choose your first turn x or 0

print("choose X or 0")
turn = input()

#start from here...........////////////
for i in range(9):
    ActualBoard(theboard)
    print("Turn for "+turn)
    print("call your postion from board")
    move = input()

    while theboard[move] !='':
        print("change your move .it's already taken")
        move = input()

    theboard[move] = turn
    won = TestforWin(theboard)

    if won == True:
        print('Game over')
        ActualBoard(theboard)
        break
    elif turn == 'X':
        turn = '0'
    else:
        turn = 'X'



