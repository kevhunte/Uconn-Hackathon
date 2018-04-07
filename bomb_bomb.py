import Tkinter as tk, time, sys, random, math
from Tkinter import Menu
from Tkinter import *

game_desc='Welcome to bomb-bomb! This game has a grid with objects that light up.\n Your goal is to repeat the same pattern to beat the level\n in the allotted time.\n As the game progresses, the speed, block sizes, and\n sequence increase.\n When the time runs out, the game is over.'

window =tk.Tk()		#tkinter instance

#----Title of window----
window.title("Bomb-bomb!") 

window.geometry("450x600")

#------Datasets-------
widgets=[]


#-----FUNCTIONS------
def greeting():
   greets = ["Break them bombs ","What's up ","Get to work! ", "Welcome ", "Hey there "]
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
   disp.grid(column=1, row=6)                          
   disp.insert(tk.END, game_desc)

def game():
    num_squares = 16
    window.title("Go!")
    window.geometry("450x600")
    clear_widgets()
    padding = window.winfo_height()/num_squares		#spacing between squares
    make_buttons(num_squares,padding)
                                                        #store in data set? Rand and fill?
def make_buttons(num,padding):
    count=y=0
    x=4							#skip first 4 grids. Leaves room for title
    edge=math.floor(math.sqrt(num))			#keeps track of edge of grid, so it stays as a square
    size=5
    while(count<num):					#repeat until all squares are made
     button = tk.Button(fg="blue")
     button.grid(column=x, row=y, padx=padding,pady=padding)			#makes button instances
     x+=1
     if(x>=edge): 
	y+=1
	x=0
     count+=1

def clear_widgets():
  widgets = window.grid_slaves()			#makes a list of all widgets
  for w in widgets:
    w.destroy()						#destroys all the current widgets

<<<<<<< HEAD
def flash(button):
	button.config(bg = 'yellow')	#Gives the button color
    window.after(200, lambda: b.config(bg = 'lightgrey')) #Gives background of window and how quick color flashes. 

def score(score):
	window.score_label = Label(disp)
	window.score_label.grid(row = 1, column = 0)

def count_down():
	for t in range(30 -1, -1):
        # format as 2 digit integers, fills with zero to the left
        # divmod() gives minutes, seconds
        sf = "{:02d}:{:02d}".format(*divmod(t, 10))
        #print(sf)  # test
        time_str.set(sf)
        window.update()
        # delay one second
        time.sleep(1)

=======

>>>>>>> ad054daf0821b8fa85b100eccdebf4ce5c4d9653
#----LABELS-----
greet=greeting()
title = tk.Label(text=greet, font=("Times New Roman",20))
title.grid(column=1, row=0) 			#places item created on grid, the window that was made

prompt = tk.Label(text="What's your name?")	#stores name info from user
#prompt.grid(column=0, row=1)

#----ENTRIES------
#name_store = tk.Entry()
#name_store.grid(column=0, row=2)

#----BUTTONS-------
#button1 = tk.Button(text="Done", command=disp_greeting)	#bg means background. adds color
#button1.grid(column=1,row=2)

new_button = tk.Button(text="New Game", fg="blue",command=game)
new_button.grid(column=1,row=2, padx=window.winfo_width()/2)

desc_button = tk.Button(text="Description", bg="blue", command=desc)	#will run a load function for the game
desc_button.grid(column=1, row=3, padx=window.winfo_width()/2)

#opt_button = tk.Button(text="Options", bg="blue", command=not_done)	#opens another window with options
#opt_button.grid(column=1, row=4, padx=window.winfo_width()/2)


window.mainloop() #runs everything in window. keep at bottom

