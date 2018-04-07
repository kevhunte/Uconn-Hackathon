import Tkinter as tk, time, sys, random, math
from Tkinter import Menu
from Tkinter import *

#prototype for the game bomb-bomb. This game will have a grid with objects that light up.
#The user must repeat the same pattern to beat the level in the allotted time.
#As they progress, the speed, block sizes, and sequence increase
#when the time runs out, the game is over 

window =tk.Tk()		#tkinter instance

#----Title of window----
window.title("Bomb-bomb!") 

window.geometry("500x500")

#------Datasets-------
widgets=[]


#-----FUNCTIONS------
def greeting():
   greets = ["Break them bombs ","What's up ","Get to work! ", "Welcome ", "Hey there "]
   #name = str(name_store.get()) 	#gets name from entry
   
   return greets[random.randint(0,len(greets)-1)] 	#picks random greeting with name

def disp_greeting():
   greet = greeting()
   disp = tk.Text(master=window, height=10, width=40)	#master makes so no specified size
   disp.grid(column=0, row=3)				#right below associated button
   disp.insert(tk.END, greet)				#insert makes the function text appear on the grid

def not_done():
   message = "This function doesn't work yet, but it will soon"
   disp = tk.Text(master=window, height=10, width=40)   
   disp.grid(column=1, row=5)                          
   disp.insert(tk.END, message)

def game():
    num_squares = 16
    window.title("Go!")
    window.geometry("450x450")
    clear_widgets()
    padding = window.winfo_height()/num_squares		#spacing between squares
    make_buttons(num_squares,padding)
                                                                #store in data set? Rand and fill?
def make_buttons(num,padding):
    count=0
    edge=math.floor(math.sqrt(num))			#keeps track of edge of grid, so it stays as a square
    x=y=0
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

load_button = tk.Button(text="Load", bg="blue", command=not_done)	#will run a load function for the game
load_button.grid(column=1, row=3, padx=window.winfo_width()/2)

opt_button = tk.Button(text="Options", bg="blue", command=not_done)	#opens another window with options
opt_button.grid(column=1, row=4, padx=window.winfo_width()/2)


window.mainloop() #runs everything in window. keep at bottom

