from tkinter import *

master = Tk()

batteries = BooleanVar()  # 2 or more batteries
batteries.set(FALSE)
serial = BooleanVar()  # last digit even
serial.set(FALSE)
ports = BooleanVar()  # has a parallel port
ports.set(FALSE)


def setbatteries():
    batteries.set(TRUE)


def setserial():
    serial.set(TRUE)


def setports():
    ports.set(TRUE)


serialbutton = Button(master, text='Serial ends with even mumber', command=setserial)
serialbutton.grid(row=0, column=0)
portbutton = Button(master, text='Has a parallel port', command=setports)
portbutton.grid(row=0, column=1)
batterybutton = Button(master, text='Has two or more buttons', command=setbatteries)
batterybutton.grid(row=0, column=2)

wires = []
temp_wirestar = BooleanVar()
temp_wirered = BooleanVar()
temp_wireblue = BooleanVar()
temp_wireled = BooleanVar()


def addwire():
    global wires
    wire = {'star': temp_wirestar.get(), 'red': temp_wirered.get(), 'blue': temp_wireblue.get(), 'led': temp_wireled.get()}
    print(wire)
    wires.append(wire)
    print(wires)
    print(serial.get())
    temp_wirestar.set(FALSE); temp_wirered.set(FALSE); temp_wireblue.set(FALSE); temp_wireled.set(FALSE)


wire_star = Checkbutton(master, text='Has star', variable=temp_wirestar)
wire_star.grid(row=1, column=0)
wire_red = Checkbutton(master, text='Has red color', variable=temp_wirered)
wire_red.grid(row=1, column=1)
wire_blue = Checkbutton(master, text='Has blue color', variable=temp_wireblue)
wire_blue.grid(row=1, column=2)
wire_led = Checkbutton(master, text='Has lit LED', variable=temp_wireled)
wire_led.grid(row=1, column=3)

new_wire = Button(master, text='Add wire', command=addwire)
new_wire.grid(row=2, column=1)

results = []
resultlist = Listbox(master)
resultlist.grid(row=4, column=1)


def getresults():
    global wires
    for wire in wires:
        if not wire['star'] and not wire['red'] and not wire['blue'] and not wire['led']:
            results.append('C')
        elif wire['star'] and not wire['red'] and not wire['blue'] and not wire['led']:
            results.append('C')
        elif wire['star'] and wire['red'] and not wire['blue'] and not wire['led']:
            results.append('C')
        elif not wire['star'] and wire['red'] and not wire['blue'] and not wire['led']:
            if serial.get():
                results.append('C')
            else:
                results.append('D')
        elif not wire['star'] and not wire['red'] and wire['blue'] and not wire['led']:
            if serial.get():
                results.append('C')
            else:
                results.append('D')
        elif not wire['star'] and wire['red'] and wire['blue'] and not wire['led']:
            if serial.get():
                results.append('C')
            else:
                results.append('D')
        elif not wire['star'] and wire['red'] and wire['blue'] and wire['led']:
            if serial.get():
                results.append('C')
            else:
                results.append('D')
        elif not wire['star'] and not wire['red'] and wire['blue'] and wire['led']:
            if ports.get():
                results.append('C')
            else:
                results.append('D')
        elif wire['star'] and not wire['red'] and wire['blue'] and wire['led']:
            if ports.get():
                results.append('C')
            else:
                results.append('D')
        elif wire['star'] and wire['red'] and wire['blue'] and not wire['led']:
            if ports.get():
                results.append('C')
            else:
                results.append('D')
        elif not wire['star'] and wire['red'] and not wire['blue'] and wire['led']:
            if batteries.get():
                results.append('C')
            else:
                results.append('D')
        elif wire['star'] and not wire['red'] and not wire['blue'] and wire['led']:
            if batteries.get():
                results.append('C')
            else:
                results.append('D')
        elif wire['star'] and wire['red'] and not wire['blue'] and wire['led']:
            if batteries.get():
                results.append('C')
            else:
                results.append('D')
        elif wire['star'] and not wire['red'] and wire['blue'] and not wire['led']:
            results.append('D')
        elif wire['star'] and wire['red'] and wire['blue'] and wire['led']:
            results.append('D')
        elif not wire['star'] and not wire['red'] and not wire['blue'] and wire['led']:
            results.append('D')
    print(results)
    for result in results:
        resultlist.insert(END, result)


def reset():
    global wires
    global results
    results = []
    wires = []
    resultlist.delete(0, END)


calcresults = Button(master, text='Get results', command=getresults)
calcresults.grid(row=3, column=1)

resetbutton = Button(master, text='Reset wires', command=reset)
resetbutton.grid(row=5, column=1)


def resetall():
    reset()
    serial.set(FALSE)
    ports.set(FALSE)
    batteries.set(FALSE)


fullreset = Button(master, text='Reset all', command=resetall)
fullreset.grid(row=5, column=2)

master.mainloop()
