from tkinter import *
from math import *
window = Tk()

def calculus():
    d=float(drag.get())
    p=float(density.get())
    m=float(mass.get())
    v=float(velocity.get())

    A=(2*m*9.8)/(1.225*p*d*v**2/p)
    dm=sqrt((4*A)/pi)
    lb4 = Label(window, text="%.3f" % dm + " m", font=10)
    lb4.place(x=175, y=230)

density = Entry(window, text="", bd=1)
density.place(x=200, y=50)
lb1 = Label(window,text="Local fluid density:")
lb1.place(x=75, y=50)

velocity = Entry(window, text='', bd=1)
velocity.place(x=200, y= 80)
lb2 = Label(window, text='Terminal velocity:')
lb2.place(x=75, y=80)

mass = Entry(window, text="", bd=1)
mass.place(x=200, y=110)
lb3 = Label(window, text='Veichle mass:')
lb3.place(x=75, y=110)

drag = Entry(window, text="", bd=1)
drag.place(x=200, y=140)
lb3 = Label(window, text='Drag coefficient:')
lb3.place(x=75, y=140)


calculate = Button(window, text="CALCULATE", fg='red', command=calculus)
calculate.place(x=165, y=180)





window.title("Parachute Calculator by João Runkel")
window.geometry("400x300+800+400")
window.mainloop()