import Tkinter, tkFont
root = Tkinter.Tk()
root.title = ("Joei")

canvas = Tkinter.Canvas(root, height = 500, width = 800, relief = Tkinter.RAISED, bg='beige')
canvas.grid()
checkbox = canvas.create_rectangle(100,200, 200, 300, dash = [1,4])
check = canvas.create_line(100,250,150,300,220,150, fill='black', width= 10)
message = canvas.create_text(500, 400, text= 'It\'s Wednesday my dudes.', font=('Verdana Bold', -20))
box = Tkinter.Checkbutton(root, text='This is a checkbox.')
box.grid(row= 1, column = 5)

#______________________________________________________________
times_pressed = 0
def pressed():
    try:
        del editor
    except:
        pass
    global times_pressed
    times_pressed += 1
    customFont = tkFont.Font(family='Georgia', size=10)     
    editor = Tkinter.Text(width =50, height=10, borderwidth= 100, font=customFont)
    editor.grid(row=0, column=0, columnspan=200)
    editor.insert(Tkinter.END, "The number of souls Madrid has crushed:")
    editor.insert(Tkinter.END, data.get())
    editor.see(Tkinter.END)   
#____________________________________________________________
def newWindow():
    root2 = Tkinter.Tk()
    editor2 = Tkinter.Text(master = root2, width = 45, height = 0)
    editor2.grid(row = 0, column = 0, columnspan = 20, sticky=(Tkinter.N, Tkinter.E, Tkinter.S, Tkinter.W))
    editor2.insert(Tkinter.END, "Hello.")
    editor2.see(Tkinter.END)
        
    button = Tkinter.Button(root2, text='Quit', width=10, height=1, bg='#C7ADDC', command = root2.destroy)
    button.grid(row=1, column=0, )

    button2 = Tkinter.Button(root2, text='New Window', width=10, height=1, bg='#C7ADDC', command = newWindow)
    button2.grid(row=1, column=1, )
#disablebackspacekey_________________________________________
    editor.config(state=Tkinter.DISABLED)
#disablebackspacekey_________________________________________   
def chipsdemo():
    import random
    random_number = random.randint(1,3)
    tries = 0
    tries_remaining = 2
    while tries < 2:
        guess = input('Pretzels, Lay\'s, or soda?')
        tries += 1
        tries_remaining -= 1
    
        try:
            guess_num = int(guess)
        except:
            print("That's not a whole number! You suck!! ")
            break
        
        if not guess_num > 0 or not guess_num < 11:
            print("That number is not between 1 and 3. ")
            break
        
        
        elif guess_num == random_number:
            print("You\'re right!")
            print("It took you {} tries. ".format(tries))
            break
        
        
        elif guess_num < random_number:
            if tries_remaining > 0:
                print("That number is low. You have {} tries..".format(int(tries_remaining)))
                continue
            else:
                print("I feel more like a {}".format(random_number))
                print("I\'m leaving.")
                break
        
        
        
        elif guess_num > random_number:
            if tries_remaining > 0:
                print("That number is too high. You have {} more tries.".format(int(tries_remaining)))
                continue
            else:
                print("My number was {}".format(random_number))
                print("Bye.")
                break
    
#_____________________________________________________
  
  
button = Tkinter.Button(root, text='Quit', width=5, height=1, bg='#C7ADDC', command = root.destroy)
button.grid(row=1, column=1, )

button1 = Tkinter.Button(root, text='New Window', width=10, height=1, bg='#C7ADDC', command = newWindow)
button1.grid(row=1, column=2, )

button2 = Tkinter.Button(root, text='Empty', width=10, height=1, bg='#C7ADDC', command = chipsdemo )
button2.grid(row=1, column=3, )

button3 = Tkinter.Button(root, text='New Window', width=10, height=1, bg='#C7ADDC', command = newWindow)
button3.grid(row=1, column=4, )

scrollbar = Tkinter.Scrollbar(root)
scrollbar.grid(row= 0, column =0)

#quitroot________________________________________________________
def quit():
    root.destroy()
#___________________________________________________________________________
root.mainloop()  
