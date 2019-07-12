import random
import time
from tkinter import Tk, Label, Button, Frame, Canvas




def create_board(width,height):
    bli = [] # final gameboard
    
    for i in range(0,height):
        dif_row = []
        
        for j in range(0,width):
            dif_row.append(None)
        bli.append(dif_row)
            
        
        
        #print(sli)
    
    return bli
def bury_mine(gboard,n):
    
    
    mines_buried = 0
    
    while mines_buried < n: 
        
        # randomly select y coordinate
        y = random.randint(0,len(gboard)-1)
        # randomly select x coordinate
        x = random.randint(0,len(gboard[0])-1)
        # check if there is already a mine in position [y][x] 
        if gboard[y][x] != -1:        
            #    if not, set that position to "*"
            gboard[y][x] = -1
            mines_buried += 1
def get_mine_count(gboard, x,y):
    width = len(gboard[0])
    height = len(gboard)
    
    mine_count = 0
    if x > 0 and gboard[y][x-1] == -1:
        mine_count +=1
    if x < width -1 and gboard [y][x+1] == -1:
        mine_count +=1 
    if y > 0 and gboard [y-1][x] == -1:
        mine_count +=1
    if y < height -1 and gboard [y+1][x] == -1:
        mine_count +=1
    if y > 0 and x> 0 and gboard [y-1][x-1] == -1:    
        mine_count += 1
    if y > 0 and x < width -1 and gboard [y-1][x+1]== -1:
        mine_count +=1
    if y < height -1 and x>0 and gboard[y+1][x-1]==-1:
        mine_count +=1
    if y < height -1 and x < width -1 and gboard [y+1][x+1] == -1:
        mine_count +=1
    return mine_count
def uncover_board(gboard, x,y):
    if gboard[y][x] != -1 and gboard[y][x] ==None:
        
        
        if get_mine_count(gboard, x,y) > 0:
            gboard[y][x] = get_mine_count(gboard, x,y)
        if get_mine_count(gboard, x,y) == 0:
            gboard[y][x] = 0
            width = len(gboard[0])
            height = len(gboard)
            
            if x > 0:
                uncover_board(gboard, x-1, y)
        
            if x < width -1:
                uncover_board(gboard, x+1, y)
       
            if y > 0:
                uncover_board(gboard, x, y-1)
       
            if y < height -1:
                uncover_board(gboard, x, y+1)
        
            if y > 0 and x> 0:
                uncover_board(gboard, x-1, y-1)
        
            if y > 0 and x < width -1:
                uncover_board(gboard, x+1, y-1)
       
            if y < height -1 and x>0:
                uncover_board(gboard, x-1, y+1)
       
            if y < height -1 and x < width -1:
                uncover_board(gboard, x+1, y+1)
                
def check_won(gboard):
    check_won_flag = True
    #if uncover_board(gboard, x,y) == -1:
    #    check_won_flag = False
    #    print("Boom! You lost!")
    #if uncover_board(gboard, x,y)!= -1:
    #    check_won_flag = False
    #    print("Continue :)")
    for col in range(0, len(gboard)):
        for row in range(0, len(gboard[0])):
            if gboard[col][row] == None:
                check_won_flag = False
                #print("You Have Won!")
    return check_won_flag

def display_board(gboard, canvas):
    
    height = (len(gboard) * 30) + len(gboard)
    width = (len(gboard[0]) * 30) + len(gboard[0])
    
    for i in range(0,width, 31):
        col = i // 31
        for j in range(0,height,31):
            row = j // 31
            if gboard[row][col] == None or gboard[row][col] == -1:
                canvas.create_rectangle(i, j,(i+30),(j+30), fill="teal")
            elif gboard[row][col] == 0:
                canvas.create_rectangle(i, j,(i+30),(j+30), fill="yellow")
                canvas.create_text(i+15,j+15,font="Times 20",text=chr(9786))
                
            elif gboard[row][col] >0:
                canvas.create_rectangle(i, j,(i+30),(j+30), fill="pink")
                canvas.create_text(i+15,j+15,font="Times 20",text=str(gboard[row][col]))
                
            elif gboard[row][col] == -2: 
                canvas.create_rectangle(i, j,(i+30),(j+30), fill="red")
                canvas.create_text(i+15,j+15,font="Times 20",text=chr(9760))
                
        
        
width = int(input("How wide do you want your game:  "))
height = int(input("How long do you want your game: "))
n = int(input("How many bombs do you want? DON'T BE A COWARD: "))   

def game(height, width, n):
    ready = input("Choose your fate! Are you ready? :< ")
    if ready == "yes":
      
        gboard = create_board(height, width)
        bury_mine(gboard,n)
        root = Tk()
        root.wm_title("Minesweeper")
        heightpxls = (len(gboard) * 30) + len(gboard)
        widthpxls = (len(gboard[0]) * 30) + len(gboard[0])
        canvas = Canvas(master=root, height=heightpxls, width=widthpxls)
        canvas.pack()
        start_time = time.time()
        display_board(gboard, canvas)
        def handle_click(event):
            frame = Frame(master=root, height=400,width=400)
            frame.pack_propagate(0) # don't shrink
            
            x = event.x // 31
            y  = event.y //31
            #print(x,y)
            if gboard[y][x] == -1:
                
                gboard [y][x] = -2
                display_board(gboard, canvas)
                canvas.unbind("<Button-1>")
                #print("You Lose")
                label = Label(master=root, text="You Lost!!\nBetter Luck Next Year! :( ", font=("Arial",40))
                label.pack(side="bottom")
                elapsed_time = int(time.time() - start_time)
                
                label2 = Label(master=root, text=(elapsed_time),font=("Arial",20))
                label2.pack(side="bottom")
                
                button = Button(master=frame, text="Cya Loser!", command=root.destroy)
                button.pack(side="bottom")
                
                frame.pack()
            else:          
                uncover_board(gboard, x,y)
                display_board(gboard,canvas)
                
                if check_won(gboard)==True:
                    canvas.unbind("<Button-1>")
                    label = Label(master=root, text="You're A Winner\n Hope You Enjoyed SHAPE 2019 :) ", font=("Arial ",40))
                    label.pack(side="top")
                    button1 = Button(master=frame, text="Bye Winner!", command=root.destroy)
                    button1.pack(side="bottom")
                    elapsed_time = int(time.time() - start_time)
                    label3 = Label(master=root, text=(elapsed_time),font=("Arial",20))
                    label3.pack(side="bottom")
                    frame.pack()
                    #print("You won!")
                    canvas.unbind("<Button-1>")
           
            
        canvas.bind("<Button-1>",handle_click)
        root.mainloop()


            

game(height,width, n)
        
        