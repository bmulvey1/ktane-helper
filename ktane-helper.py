from tkinter import *

master = Tk()

serial_label = Label(master, text='Serial number')
serial_label.grid(row=1, column=0)

strike_label = Label(master, text='Strikes')
strike_label.grid(row=0, column=0)

portadd_label = Label(master, text='Add port')
portadd_label.grid(row=2, column=0)

portlist_label = Label(master, text='Added ports')
portlist_label.grid(row=4, column=0)

indicatorlist_label = Label(master, text='Added indicators')
indicatorlist_label.grid(row=5, column=0)

indicatorinput_label = Label(master, text='Add indicator')
indicatorinput_label.grid(row=3, column=0)

temp_port = StringVar()
temp_port.set('')

serial = StringVar()
serial.set('')

temp_indicator = StringVar()
temp_indicator.set('')

temp_indicatoron = BooleanVar()
temp_indicatoron.set(FALSE)

vowel_label = Label(master, text='Vowel', bg='red')
vowel_label.grid(row=1, column=3)

even_label = Label(master, text='Even', bg='red')
even_label.grid(row=1, column=2)

port_input = Entry(master, textvariable=temp_port)
port_input.grid(row=2, column=1)

indicator_input = Entry(master, textvariable=temp_indicator)
indicator_input.grid(row=3, column=1)

indicatoron_input = Checkbutton(master, text='On', variable=temp_indicatoron)
indicatoron_input.grid(row=3, column=2)

port_list = Listbox(master)
port_list.grid(row=4, column=1)

indicator_list = Listbox(master)
indicator_list.grid(row=5, column=1)


def addport(event):
    str = event.widget.get().upper()
    port_list.insert(END, str)
    temp_port.set('')


def addindicator(event):
    str = event.widget.get().upper()
    on = temp_indicatoron.get()
    if on:
        str1 = str + ' ' + 'ON'
        indicator_list.insert(END, str1)
        temp_indicatoron.set(FALSE)
        temp_indicator.set('')
    else:
        str1 = str + ' ' + 'OFF'
        indicator_list.insert(END, str1)
        temp_indicatoron.set(FALSE)
        temp_indicator.set('')


port_input.bind('<Return>', addport)
indicator_input.bind('<Return>', addindicator)


def checkvowel(serial):
    vowels = ['A', 'E', 'I', 'O', 'U']
    sn = serial.get().upper()
    if sn == '':
        return
    for i in sn:
        if i in vowels:
            vowel_label.config(bg='green')
            break
        else:
            pass


def checkeven(serial):
    sn = serial.get()
    if sn == '':
        return
    if sn[-1].isdigit():
        if int(sn[-1]) % 2 != 0:
            even_label.config(bg='red')
        elif int(sn[-1]) == 0:
            even_label.config(bg='yellow')
        else:
            even_label.config(bg='green')
    else:
        even_label.config(bg='red')


serial.trace("w", lambda name, index, mode, serial=serial: checkvowel(serial))
serial.trace("w", lambda name, index, mode, serial=serial: checkeven(serial))

strikes = IntVar()
strikes.set(value=0)

strikecounter = Entry(master, textvariable=strikes, state=DISABLED)
strikecounter.grid(row=0, column=1)
serialdisplay = Entry(master, textvariable=serial)
serialdisplay.grid(row=1, column=1)


def reset():
    serial.set(value='')
    strikes.set(value=0)
    vowel_label.config(bg='red')
    even_label.config(bg='red')
    port_list.delete(0, END)
    indicator_list.delete(0, END)
    temp_indicatoron.set(FALSE)
    temp_indicator.set('')
    temp_port.set('')


def inc_strikes():
    strikes.set(value=strikes.get() + 1)


strikebutton = Button(master, text='Add a strike', command=inc_strikes)
strikebutton.grid(row=0, column=2)
resetbutton = Button(master, text='Reset all', command=reset)
resetbutton.grid(row=6, column=1)

master.mainloop()
