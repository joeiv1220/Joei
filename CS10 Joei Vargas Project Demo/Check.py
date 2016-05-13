import Tkinter, tkFont

root = Tkinter.Tk()

#canvas = Tkinter.Canvas(root, height = 500, width = 800, relief = Tkinter.RAISED, bg='beige')
#canvas.grid()

#checkbox = canvas.create_rectangle(100,200, 200, 300, dash = [1,4])

#check = canvas.create_line(100,250,150,300,220,150, fill='black', width= 10)

#message = canvas.create_text(500, 400, text= 'It\'s Wednesday my dudes.', font=('Verdana Bold', -20))

'''box = Tkinter.Checkbutton(root, text='This is a checkbox.')
box.grid(row= 1, column = 1)'''
  
times_pressed = 0
def pressed(x):
    try:
        del editor
    except:
        pass
    global times_pressed
    times_pressed+= x
    customFont = tkFont.Font(family='Georgia', size=20)     
    editor = Tkinter.Text(width =50, height=10, font=customFont)
    editor.grid(row=0, column =0)
    #____________________________
    editor.insert(Tkinter.END, "The number of souls Madrid has crushed:")
    editor.insert(Tkinter.END, times_pressed)
    editor.see(Tkinter.END)
    
    #disablebackspacekey
    editor.config(state=Tkinter.DISABLED)
    
button = Tkinter.Button(root, text='Add 1', width=10, height=5, command = lambda : pressed(1))
button.grid(row=1, column=0, pady = 100)

button2 = Tkinter.Button(root, text='Add 2', width=10, height=5, command = lambda : pressed(2))
button2.grid(row=1, column=1, pady = 100)

button3 = Tkinter.Button(root, text='Add 4', width=10, height=5, command = lambda : pressed(4))
button3.grid(row=1, column=2, pady = 100)

button4 = Tkinter.Button(root, text='Add 8', width=10, height=5, command = lambda : pressed(8))
button4.grid(row=1, column=3, pady = 100)

button5 = Tkinter.Button(root, text='Add 10', width=10, height=5, command = lambda : pressed(10))
button5.grid(row=1, column=4, pady = 100)

root.mainloop()








'''radio = [0]*4 #createlist
data = Tkinter.IntVar()
for i in range(4):
    radio[i] = Tkinter.Radiobutton(root, text= str(i), variable=data, value=i)
    radio[i].grid(row=3, column=i)
    
data.set(3)'''

  