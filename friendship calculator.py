#simple friendship calculator - by prs

import random
from tkinter import *

expression = ""

def press(): 
		global expression
		list = [00,55,100,95,98,80,15,40,75,65,25,20,35,85,72,64,88]
		total = random.choice(list)
		expression = expression + str(total)+"%"
		equation.set(expression)
		# initialze the expression variable by empty string 
		expression = ""
    
if __name__ == "__main__": 
	# create a GUI window 
	gui = Tk() 

	# set the background colour of GUI window 
	gui.configure(background="black") 

	# set the title of GUI window 
	gui.title("friendship  calculator") 

	# set the configuration of GUI window 
	gui.geometry("260x330")

	equation = StringVar()

	label11 = Label(gui ,text = "FRIENDSHIP CALCULATOR",font = "95",bg="khaki",fg ="red",justify = "center")
	label11.grid(row = 0,columnspan = 4)

	label1 = Label(gui ,text = "enter the first name",font = "35",bg = "black",fg ="white",justify = "left")
	label1.grid(row = 1,columnspan = 4)

	entry1 = Entry(gui,bg = "white",fg ="blue",text = "",font ="30",justify = "center")
	entry1.grid( row = 2,columnspan=4 )

	label2 = Label(gui ,font = "30",bg = "black",)
	label2.grid(row = 3)	

	label3 = Label(gui ,text = "enter the second name",font = "35",fg = "white",bg="black",justify = "center")
	label3.grid(row = 4,columnspan = 4)

	entry2 = Entry(gui,bg = "white",fg ="blue",text = "",font ="30",justify = "center")
	entry2.grid( row = 5,columnspan=4)

	label4 = Label(gui ,font = "40",bg = "black")
	label4.grid(row = 6)

	button1 =Button(gui, bg ="red",text = "press me  ",font ="30",fg ="yellow" ,height ="1",width ="10",justify = "center",command=lambda:press())
	button1.grid(row=8,columnspan = 4)

	label6 =Label(gui, bg ="black",text = " ",font ="40" ,justify = "center")
	label6.grid(row=9)
	entry3 = Entry(gui,bg = "midnight blue",fg = "white",font ="50",textvariable = equation,justify = "center")
	entry3.grid( row = 10,columnspan=4)
	equation.set('')

	label7 =Label(gui,bg ="black", fg ="red",text = "friendship calculator - by prs",font ="46" ,justify = "center")
	label7.grid(row=11)


	

gui.mainloop()
