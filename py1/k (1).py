import tkinter

def do():
                label.config(text = int(entry.get()) + int(entry1.get()))
                
def do1():
                label.config(text = int(entry.get()) - int(entry1.get()))

def do2():
                label.config(text = int(entry.get()) * int(entry1.get()))
                
def do3():
                label.config(text = int(entry.get()) / int(entry1.get()))


window = tkinter.Tk()
window.minsize(300, 300)

entry = tkinter.Entry()
entry.grid(row = 0, column = 3)

entry1 = tkinter.Entry()
entry1.grid(row = 0, column = 12)

button = tkinter.Button(text = "+", command = do)
button.grid(row = 1, column = 6)

button1 = tkinter.Button(text = "-", command = do1)
button1.grid(row = 6, column = 6)

button2 = tkinter.Button(text = "*", command = do2)
button2.grid(row = 12, column = 6)

button3 = tkinter.Button(text = "/", command = do3)
button3.grid(row = 24, column = 6)

label = tkinter.Label()
label.config(text = "?")
label.grid(row = 48, column = 6)




window.mainloop()
