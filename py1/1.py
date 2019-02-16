import tkinter

operator = ""

def do(b):
    z = len(entry.get())
    entry.insert(z, b)

def do1():
    z = len(entry.get())
    entry.delete(0, z)

def do2():
    global operator
    do("+")
    operator = "+"

def do3():
    global operator
    do("-")
    operator = "-"

def do4():
    global operator
    do("*")
    operator = "*"

def do5():
    global operator
    do("/")
    operator = "/"

def do6():
    x = (entry.get()).split(operator)
    do1()
    if operator == "+":
        entry.insert(0, (int(x[0]) + int(x[1])))
    if operator == "-":
        entry.insert(0, (int(x[0]) - int(x[1])))
    if operator == "*":
        entry.insert(0, (int(x[0]) * int(x[1])))
    if operator == "/":
        entry.insert(0, (int(x[0]) / int(x[1])))
        
    


window = tkinter.Tk()
window.title("Daniil")
window.minsize(300, 300)

a = tkinter.Frame(window)
a.grid(row = 2)

entry = tkinter.Entry()
entry.config(fg = "navy")
entry.grid(row = 1, column = 0)

button = tkinter.Button(a, text = "1", command = lambda: do(1))
button.grid(row = 2, column = 2)

button1 = tkinter.Button(a, text = "2", command = lambda: do(2))
button1.grid(row = 2, column = 4)

button2 = tkinter.Button(a, text = "3",  command = lambda: do(3))
button2.grid(row = 2, column = 6)

button3 = tkinter.Button(a, text = "+", command = do2)
button3.grid(row = 2, column = 8)

button4 = tkinter.Button(a, text = "4", command = lambda: do(4))
button4.grid(row = 6, column = 2)

button5 = tkinter.Button(a, text = "5", command = lambda: do(5))
button5.grid(row = 6, column = 4)

button6 = tkinter.Button(a, text = "6", command = lambda: do(6))
button6.grid(row = 6, column = 6)

button7 = tkinter.Button(a, text = "-" , command = do3)
button7.grid(row = 6, column = 8)

button8 = tkinter.Button(a, text = "7", command = lambda: do(7))
button8.grid(row = 9, column = 2)

button9 = tkinter.Button(a, text = "8", command = lambda: do(8))
button9.grid(row = 9, column = 4)

button10 = tkinter.Button(a, text = "9", command = lambda: do(9))
button10.grid(row = 9, column = 6)

button11 = tkinter.Button(a, text = "*", command = do4)
button11.grid(row = 9, column = 8)

button12 = tkinter.Button(a, text = "CE", command = do1)
button12.grid(row = 12, column = 2)

button13 = tkinter.Button(a, text = "0", command = lambda: do(0))
button13.grid(row = 12, column = 4)

button14 = tkinter.Button(a, text = "=", command = do6)
button14.grid(row = 12, column = 6)

button15 = tkinter.Button(a, text = "/", command = do5)
button15.grid(row = 12, column = 8)







window.mainloop()