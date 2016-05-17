import Tkinter, tkFont

root = Tkinter.Tk()
#frame = Tkinter.Frame(root,height=500, width=200, bg='blue', cursor="circle")
#frame.pack()
root.title('Doofenshmirtz Evil Incorporated')

scrollbar = Tkinter.Scrollbar(root)
scrollbar.grid(row=0, column=6, sticky = Tkinter.N + Tkinter.S)

#def add():
 #   global talk
  #  talk += 1
    
   # editor.insert(Tkinter.END, "Hello",+str(talk))
    #editor.insert(Tkinter.END, "\n")
    #editor.see(Tkinter.END)
    
    #scrollbar.config(command=editor.yview)


#editor = Tkinter.Text(width=50, height=4, bg='#799cbe', yscrollcommand = scrollbar.set)
#editor.grid(row=0, column=0)













def pressed():
    #Deletes the text box if it is there
    try:
        del editor
    except:
        pass
    #recreates the textbox
    global times_pressed
    frame = Tkinter.Frame(root, height=300, width=200, bg='blue', cursor="pirate")
    customFont = tkFont.Font(family='Comic Sans MS',weight='bold', size=25)
    editor = Tkinter.Text(frame, width=50, height=4, font=customFont, bg='#799cbe')
    editor.grid(row=0, column=0)
    
    
    #Adds text to the box
    editor.insert(Tkinter.END, "The number of times Stanford Pines corrected Stanley Pines\' grammer: ")
    editor.insert(Tkinter.END)
    editor.see(Tkinter.END)
    
    #disable chnging the text box
    editor.config(state=Tkinter.DISABLED)
    #editor.config(state=Tkinter.NORMAL)

talk = 0

def talk():

    talkText = Tkinter.Text(master = root, width=100, height=20, bg='pink')
    talkText.grid(row=0, column=0, columnspan = 500)

def quit():
    root.destroy() 
    
def newWindow():
    root2 = Tkinter.Tk()
    editor2 = Tkinter.Text(master = root2, width = 40, height=0 )
    editor2.grid(row = 0, column = 0, columnspan = 2, sticky=(Tkinter.N, Tkinter.W, Tkinter.E))
    editor2.insert(Tkinter.END, "Doofenshmirtz Evil Incorporated")
    editor2.see(Tkinter.END)
    
    button = Tkinter.Button(root2, text='Quit', width=10, height= 5, command = root2.destroy)
    button.grid(row=1, column=0)

    button2 = Tkinter.Button(root2, text='New Window', width=10, height= 5, command = newWindow)
    button2.grid(row=2, column=0)
    
    button3 = Tkinter.Button(root2, text='List Box', width=10, height= 5, command = listBox)
    button3.grid(row=3, column=0)


def listBox():
    root3 = Tkinter.Tk()
    lbox = Tkinter.Listbox(master = root3, bg='#C7ADDC', height=100, width=100, cursor='circle', borderwidth=20)
    lbox.grid(row=0, column=0, columnspan=100, sticky=(Tkinter.N, Tkinter.W, Tkinter.E))
    lbox.see(Tkinter.END)


button = Tkinter.Button(root, text='QUIT', width=10, height= 5, command = quit)
button.grid(row=3,column=1)

button2 = Tkinter.Button(root, text='New Window', width=10, height= 5, command = newWindow)
button2.grid(row=3, column=2)

button3 = Tkinter.Button(root, text='Talk', width=10, height= 5, command = talk)
button3.grid(row=3, column=3)


#redbutton = Tkinter.Button(frame, text="Red", fg="red")


#greenbutton = Tkinter.Button(frame, text="Brown", fg="brown")
#greenbutton.grid(row=3,column=0) 

#bluebutton = Tkinter.Button(frame, text="Blue", fg="blue")
#bluebutton.pack( side = LEFT )


root.mainloop()