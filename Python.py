import tkinter

window = tkinter.Tk()

window.title("Vasya")
window.minsize(300, 300)
window.config(bg = "navy")

a = tkinter.Frame(window)
a.pack(pady = 150)
a.config(bg = "black")
label = tkinter.Label(a) 
label.config(text="Daniil",          
                font="Lucida  100",          
                fg="navy",
                bg = "black"
                )
label.pack(pady=1, side = "top")

label1 = tkinter.Label(a)
label1.config(text = "МВЧ О 17-2",
            font = "Lucida 100",
            fg="navy",
            bg = "black"
            )
label1.pack(pady=1, side = "top")

label2 = tkinter.Label(a)
label2.config(text = "14 years",
            font = "Lucida 100",
            fg="navy",
            bg = "black"
            )
label2.pack(pady=1, side = "top")


window.mainloop()


