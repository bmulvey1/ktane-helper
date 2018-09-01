from tkinter import *

master = Tk()

red = IntVar()
red.set(value=0)
blue = IntVar()
blue.set(value=0)
black = IntVar()
black.set(value=0)


def newred(var):
    if var.get() == 0:
        pass
    elif var.get() == 1:
        instructions.set('C')
    elif var.get() == 2:
        instructions.set('B')
    elif var.get() == 3:
        instructions.set('A')
    elif var.get() == 4:
        instructions.set('AC')
    elif var.get() == 5:
        instructions.set('B')
    elif var.get() == 6:
        instructions.set('AC')
    elif var.get() == 7:
        instructions.set('ABC')
    elif var.get() == 8:
        instructions.set('AB')
    elif var.get() == 9:
        instructions.set('B')


def newblue(var):
    if var.get() == 0:
        pass
    elif var.get() == 1:
        instructions.set('B')
    elif var.get() == 2:
        instructions.set('AC')
    elif var.get() == 3:
        instructions.set('B')
    elif var.get() == 4:
        instructions.set('A')
    elif var.get() == 5:
        instructions.set('B')
    elif var.get() == 6:
        instructions.set('BC')
    elif var.get() == 7:
        instructions.set('C')
    elif var.get() == 8:
        instructions.set('AC')
    elif var.get() == 9:
        instructions.set('A')


def newblack(var):
    if var.get() == 0:
        pass
    elif var.get() == 1:
        instructions.set('ABC')
    elif var.get() == 2:
        instructions.set('AC')
    elif var.get() == 3:
        instructions.set('B')
    elif var.get() == 4:
        instructions.set('AC')
    elif var.get() == 5:
        instructions.set('B')
    elif var.get() == 6:
        instructions.set('BC')
    elif var.get() == 7:
        instructions.set('AB')
    elif var.get() == 8:
        instructions.set('C')
    elif var.get() == 9:
        instructions.set('C')


def incrementred():
    red.set(red.get()+1)
    newred(red)


def incrementblue():
    blue.set(blue.get()+1)
    newblue(blue)


def incrementblack():
    black.set(black.get()+1)
    newblack(black)


redbutton = Button(master, text='Add red wire', command=incrementred, bg='red')
redbutton.grid(row=0, column=0)
bluebutton = Button(master, text='Add blue wire', command=incrementblue, bg='blue', fg='white')
bluebutton.grid(row=0, column=1)
blackbutton = Button(master, text='Add black wire', command=incrementblack, bg='black', fg='white')
blackbutton.grid(row=0, column=2)

instructions = StringVar()
instructions.set('')

instructionlabel = Entry(master, textvariable=instructions, state=DISABLED)
instructionlabel.grid(row=1, column=1)


def reset():
    red.set(0)
    blue.set(0)
    black.set(0)
    instructions.set('')


resetbutton = Button(master, text="Reset all", command=reset)
resetbutton.grid(row=2, column=1)

master.mainloop()
