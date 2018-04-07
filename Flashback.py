import Tkinter as tk, time, sys, random, math
from Tkinter import *
from random import shuffle
#from PIL import ImageTk
#from PIL import ImageTk

game_desc=' Welcome to Flashback! This game has a grid with objects\n that light up. Your goal is to repeat the same pattern to \n beat the level in the allotted time.\n\n As the game progresses, the speed, block sizes, and\n sequence increases.\n\n When the time runs out, the game is over.'

window =tk.Tk()		#tkinter instance

#-----GLOBALS------
num_squares = 16					#defaults for these numbers
num_flashes = 2

#-----WINDOW-----
window.title("Flashback!") 

window.geometry("414x736")

#background_image=PIL.Image.open("FlashBack_Menu_Screen.png")			#background image for app
pic = tk.PhotoImage("FlashBack_Menu_Screen.png")
label = Label(window, image=pic)
label.image = pic
label.place(x=0,y=0, relwidth=1, relheight=1)

#------Datasets-------
widgets=[]


#-----FUNCTIONS------
def game():
    window.title("Go!")
    window.geometry("414x736")
    clear_grid()
    padding = window.winfo_height()/num_squares         #spacing between squares 
    make_buttons(num_squares,padding)
    flash_buttons(num_flashes)

def set_squares(n,string):				#sets number of squares for grid
   num_squares = n
   label = tk.Label(text=string+' mode selected!', font=("Times New Roman",14))
   label.grid(column=1, row=5)

def set_difficulty():					#sets difficulty for game
   clear_grid()
   label = tk.Label(text='Select Game difficulty', font=("Times New Roman",14))
   label.grid(column=1, row=0)
   easy = tk.Button(text='Easy', command = set_squares(9,'easy'))
   med = tk.Button(text='Medium', command = set_squares(16,'medium'))
   hard = tk.Button(text='Hard', command = set_squares(25,'hard'))
   back = tk.Button(text= 'Go Back', command = Main_Menu)
   easy.grid(column=1, row=1)
   med.grid(column=1, row=2)
   hard.grid(column=1, row=3)
   back.grid(column=1, row=4)

def greeting():
   greets = ["What's up ","Ready to play? ", "Hello there ", "Hey there! "]
   #name = str(name_store.get()) 	#gets name from entry
   
   return greets[random.randint(0,len(greets)-1)] 	#picks random greeting with name

def disp_greeting():
   greet = greeting()
   disp = tk.Text(master=window, height=7, width=40)	#master makes so no specified size
   disp.grid(column=2, row=1)				#right below associated button
   disp.insert(tk.END, greet)				#insert makes the function text appear on the grid

def desc():
   #message = "This function doesn't work yet, but it will soon"
   disp = tk.Text(master=window, height=10, width=60)   
   disp.grid(column=1, row=6, pady=0)                          
   disp.insert(tk.END, game_desc)
                                                        #store in data set? Rand and fill?
def make_buttons(num,padding):
    count=x=0
    y=1							#skip first 4 grids. Leaves room for title
    edge=math.floor(math.sqrt(num))			#keeps track of edge of grid, so it stays as a square
    size=5
    while(count<num):					#repeat until all squares are made
     button = tk.Button()
     button.config(bg='blue')
     button.grid(column=x, row=y, padx=padding,pady=padding)			#makes button instances
     x+=1
     if(x%edge==0): 
	y+=1
	x=0
     count+=1
    quit = tk.Button(text='Quit', command= Main_Menu)
    quit.grid(column=0, row=y+1 )

def clear_pack():
  widgets = window.slaves()
  for w in widgets:
   w.destroy()

def clear_grid():
  widgets = window.grid_slaves()			#makes a list of all widgets
  for w in widgets:
    w.destroy()						#destroys all the current widgets

def score(score):
	window.score_label = Label(disp)
	window.score_label.grid(row = 1, column = 0)

def count_down():
	for t in range(30, -1, -1):
        # format as 2 digit integers, fills with zero to the left
        # divmod() gives minutes, seconds
	   sf = "{:02d}:{:02d}".format(*divmod(t, 10))
        #print(sf)  # test
	   time_str.set(sf)
	   window.update()
        # delay one second
	   time.sleep(1)

def flash(button):					#flashes button widgets
   button.config(bg = 'white')
   window.after(200, lambda: button.config(bg = 'blue') )

def flash_buttons(num):
   count=num						#flashes buttons, number of buttons
   buttons = window.grid_slaves()			#makes list of all current widgets on screen
   shuffle(buttons)					#randomizes order of widgets
   for b in buttons:
    if(count<=0): break					#if count is zero, stop flashing buttons
    flash(b)
    count-=1

#----LABELS-----
greet=greeting()
title = tk.Label(text=greet, font=("Times New Roman",20))
title.grid(column=1, row=0) 			#places item created on grid, the window that was made

prompt = tk.Label(text="What's your name?")	#stores name info from user
#prompt.grid(column=0, row=1)

#----ENTRIES------
#name_store = tk.Entry()
#name_store.grid(column=0, row=2)

#-----BUTTONS-------
#button1 = tk.Button(text="Done", command=disp_greeting)	#bg means background. adds color
#button1.grid(column=1,row=2)

#-----MAIN MENU------

def Main_Menu():
  clear_grid()
  title = tk.Label(text=" ", font=("Times New Roman",20))
  title.grid(column=1, row=0, pady= 150)                     		#spacing for jpeg
  play_button = tk.Button(text="Play", fg="blue",command=game)
  play_button.grid(column=1,row=2, pady=60)
  desc()							#displays description of the game
  #desc_button = tk.Button(text=" ",) 
  #desc_button.grid(column=1, row=2)
  #opt_button = tk.Button(text="Set Difficulty", bg="blue", command=set_difficulty)	#sets game difficulty
  #opt_button.grid(column=1, row=4)

Main_Menu()
window.mainloop() #runs everything in window. keep at bottom

