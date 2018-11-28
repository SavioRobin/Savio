import curses
from curses import KEY_UP,KEY_DOWN,KEY_LEFT,KEY_RIGHT
from random import randint
curses.initscr()
win=curses.newwin(20,60,0,0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
key=KEY_RIGHT
key2=0
score1=0
score2=0
snake1=[[4,10],[4,9],[4,8]]
snake2=[[4,48],[4,49],[4,50]]
food=[10,20]
count=0
win.addch(food[0],food[1],"$")
h=0
s1=[]
s2=[]
winner=0
prevkey2=ord('a')
prevkey=KEY_RIGHT
key1=KEY_RIGHT
key2=ord('a')
while key!=27:
    win.addstr(0,2,'SCORE PLAYER1:'+str(score1))
    win.addstr(0,24,'SNAKE GAME')
    win.addstr(0,40,'SCORE PLAYER2:'+str(score2))
    count=len(snake1)+len(snake2)
    if len(snake1)+len(snake2)>60:
        count=60
    win.timeout(80-count)

    key=win.getch()

    if key==ord(' '):
        key=-1
        while key!=ord(' '):
            key=win.getch()
        key=prevkey
        continue

    if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:
        key1=prevkey
    elif (key==KEY_LEFT and prevkey==KEY_RIGHT) or (key==KEY_UP and prevkey==KEY_DOWN) or (key==KEY_RIGHT and prevkey==KEY_LEFT) or (key==KEY_DOWN and prevkey==KEY_UP):
        key1=prevkey
    else:
        key1=key
        prevkey=key1
    snake1.insert(0, [snake1[0][0] + (key1 == KEY_DOWN and 1) + (key1 == KEY_UP and -1), snake1[0][1] + (key1 == KEY_LEFT and -1) + (key1 == KEY_RIGHT and 1)])
    
    if key  not in [ord('w'),ord('s'),ord('d'),ord('a')]:
        key2=prevkey2
    elif (key==ord('w') and prevkey2==ord('s')) or (key==ord('s') and prevkey2==ord('w')) or (key==ord('d') and prevkey2==ord('a')) or (key==ord('a') and prevkey2==ord('d')):
        key2=prevkey2

    else:
        key2=key
        prevkey2=key2
    snake2.insert(0, [snake2[0][0] + (key2 == ord('s') and 1) + (key2 == ord('w') and -1), snake2[0][1] + (key2 == ord('a') and -1) + (key2 == ord('d') and 1)])
    
    if snake1[0][0] == 0: snake1[0][0] = 18
    if snake1[0][1] == 0: snake1[0][1] = 58
    if snake1[0][0] == 19: snake1[0][0] = 1
    if snake1[0][1] == 59: snake1[0][1] = 1
    if snake2[0][0] == 0: snake2[0][0] = 18
    if snake2[0][1] == 0: snake2[0][1] = 58
    if snake2[0][0] == 19: snake2[0][0] = 1
    if snake2[0][1] == 59: snake2[0][1] = 1

    s1=snake1
    s2=snake2
    if snake1[0]==snake2[0]:break
    if snake1[0] in snake1[1:]:
        winner=2
        break
    if snake1[0] in snake2[1:]:
        winner=2
        break
    if snake2[0] in snake2[1:]:
        winner=1
        break
    if snake2[0] in snake1[1:]:
        winner=1        
        break                  
    true=-1
    if snake1[0] == food:                                            
        food = []
        score1 += 1
        true=1
        while food == []:
            food = [randint(1, 18), randint(1, 58)]
            if food in snake1: food = []
            if food in snake2: food = []
            
        win.addch(food[0], food[1], '$')
    if snake2[0]==food:
        food=[]
        score2 +=1
        true=2
        while food == []:
            food = [randint(1, 18), randint(1, 58)]
            if food in snake1: food = []
            if food in snake2: food = []
            
        win.addch(food[0], food[1], '$')
    if true!=1:    
        last = snake1.pop()                                          
        win.addch(last[0], last[1], ' ')
    if true!=2:
        last = snake2.pop()                                          
        win.addch(last[0], last[1], ' ')
    win.addch(snake1[0][0], snake1[0][1], '#')
    win.addch(snake2[0][0], snake2[0][1], '%')
    
curses.endwin()
if winner==1:
    print("player one wins")
elif winner==2:
    print("player two wins")
else:
    print("\nScore of Player1- " +str(score1))
    print("\nScore of Player2- " + str(score2))
    if score1<score2:
        print("\nplayer 2 wins")
    elif score2<score1:
        print("\nplayer 1 wins")
    else:
        print("\nits a draw")
