import Tkinter, tkFont 
root = Tkinter.Tk()

#canvas = Tkinter.Canvas(root, height = 500, width = 800, relief = Tkinter.RAISED, bg='beige')
#canvas.grid()
#checkbox = canvas.create_rectangle(100,200, 200, 300, dash = [1,4])
#check = canvas.create_line(100,250,150,300,220,150, fill='black', width= 10)
#message = canvas.create_text(500, 400, text= 'It\'s Wednesday my dudes.', font=('Verdana Bold', -20))
#box = Tkinter.Checkbutton(root, text='This is a checkbox.')
#box.grid(row= 1, column = 1)
#______________________________________________________________
times_pressed = 0
def pressed():
    try:
        del editor
    except:
        pass
    global times_pressed
    times_pressed += 1
    customFont = tkFont.Font(family='Georgia', size=20)     
    editor = Tkinter.Text(width =50, height=10, font=customFont)
    editor.grid(row=0, column =0)
    editor.insert(Tkinter.END, "The number of souls Madrid has crushed:")
    editor.insert(Tkinter.END, data.get())
    editor.see(Tkinter.END)

    
#disablebackspacekey_________________________________________
    editor.config(state=Tkinter.DISABLED)
#____________________________________________________________
def newWindow():
    root2 = Tkinter.Tk()
    editor2 = Tkinter.Text(master = root2, width = 45, height = 0)
    editor2.grid(row = 0, column = 0, columnspan = 2, sticky=(Tkinter.N, Tkinter.E, Tkinter.S, Tkinter.W))
    editor2.insert(Tkinter.END, "Hello.")
    editor2.see(Tkinter.END)
        
    button = Tkinter.Button(root2, text='Quit', width=10, height=5, command = root2.destroy)
    button.grid(row=1, column=0, )

    button2 = Tkinter.Button(root2, text='New Window', width=10, height=5, command = newWindow)
    button2.grid(row=1, column=1, )

#_____________________________________________________
  
  
button = Tkinter.Button(root, text='Quit', width=5, height=5, command = root.destroy)
button.grid(row=1, column=4, )

button1 = Tkinter.Button(root, text='New Window', width=10, height=5, command = newWindow)
button1.grid(row=1, column=5, )


#quitroot________________________________________________________
def quit():
    root.destroy()
#_______________________________________________________________________________    
radio = [0]*4 #createlist
data = Tkinter.IntVar()
for i in range(4):
    radio[i] = Tkinter.Radiobutton(root, text= str(i),
                        variable=data, value=i, indicatoron=0, command = pressed)
    radio[i].grid(row=1, column=i)
    
data.set(3)
#___________________________________________________________________________
root.mainloop()  
