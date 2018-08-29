from tkinter import *

master = Tk()

passwords = [['about', 'after', 'again', 'below', 'could'],
             ['every', 'first', 'found', 'great', 'house'],
             ['large', 'learn', 'never', 'other', 'place'],
             ['plant', 'point', 'right', 'small', 'sound'],
             ['spell', 'still', 'study', 'their', 'there'],
             ['these', 'thing', 'think', 'three', 'water'],
             ['where', 'which', 'world', 'would', 'write']]

col1 = StringVar()
col1.set('')
col2 = StringVar()
col2.set('')
col3 = StringVar()
col3.set('')

entries = []
for i in range(0, 3):
    exec(f'entry{i} = Entry(master, textvariable=col{i+1})')
    exec(f'entry{i}.grid(row=7, column={i})')

allwords = []
words = [[0 for x in range(5)] for x in range(7)]
for col in range(0, 5):
    for row in range(0, 7):
        words[row][col] = Label(master, text=passwords[row][col])
        words[row][col].grid(row=row, column=col)
        allwords.append(words[row][col])




def checkwords_1(col):
    letters = col.get()
    if letters == '':
        for column in range(5):
            for row in range(7):
                words[row][column].config(bg='red')
        return
    else:
        for i in letters:
            for column in range(0, 5):
                for row in range(0, 7):
                    if i in passwords[row][column][0]:
                        word = words[row][column]
                        if str(word.cget('background')).lower() == 'systembuttonface':
                            word.config(bg='green')
                        elif str(word.cget('background')).lower() == 'red':
                            word.config(bg='green')
                    else:
                        word = words[row][column]
                        if str(word.cget('background')).lower() == 'green':
                            pass
                        else:
                            word.config(bg='red')


checkedprevious2 = False
current_true2 = []
previous_true2 = []


def checkwords_2(col):
    global checkedprevious2
    letters = col.get()
    global current_true2
    global previous_true2
    if letters == '':
        current_true2 = []
        previous_true2 = []
        return
    else:
        if checkedprevious2:
            for i in letters:
                for column in range(0, 5):
                    for row in range(0, 7):
                        word = words[row][column]
                        if i in passwords[row][column][1]:
                            if word.cget('text') not in current_true2:
                                current_true2.append(word)
            print(current_true2)
            common = set(current_true2) & set(previous_true2)
            false = set(allwords) - set(common)
            for word in list(common):
                word.config(bg='green')
                print(word.cget('text'))
            for word in list(false):
                word.config(bg='red')
                print(word.cget('text') + ' false')

        else:
            for column in range(5):
                for row in range(7):
                    word = words[row][column]
                    if word.cget('background') == 'green':
                        previous_true2.append(word)
            print(previous_true2)
            checkedprevious2 = True
            for i in letters:
                for column in range(0, 5):
                    for row in range(0, 7):
                        word = words[row][column]
                        if i in passwords[row][column][1]:
                                current_true2.append(word)
            print(current_true2)
            common = set(current_true2) & set(previous_true2)
            false = set(allwords) - set(common)
            print(list(common))
            print(list(false))
            for word in list(common):
                word.config(bg='green')
            for word in list(false):
                word.config(bg='red')


checkedprevious3 = False
current_true3 = []
previous_true3 = []


def checkwords_3(col):
    global checkedprevious3
    global current_true3
    global previous_true3
    letters = col.get()
    if letters == '':
        current_true3 = []
        previous_true3 = []
        return
    else:
        if checkedprevious3:
            for i in letters:
                for column in range(0, 5):
                    for row in range(0, 7):
                        word = words[row][column]
                        if i in passwords[row][column][2]:
                            if word.cget('text') not in current_true3:
                                current_true3.append(word)
            common = set(current_true3) & set(previous_true3)
            false = set(allwords) - set(common)
            for word in list(common):
                word.config(bg='green')
            for word in list(false):
                word.config(bg='red')

        else:
            for column in range(5):
                for row in range(7):
                    word = words[row][column]
                    if word.cget('background') == 'green':
                        previous_true3.append(word)
            checkedprevious3 = True
            for i in letters:
                for column in range(0, 5):
                    for row in range(0, 7):
                        word = words[row][column]
                        if i in passwords[row][column][2]:
                                current_true3.append(word)
            common = set(current_true3) & set(previous_true3)
            false = set(allwords) - set(common)
            for word in list(common):
                word.config(bg='green')
            for word in list(false):
                word.config(bg='red')


col1.trace("w", lambda name, index, mode, col1=col1: checkwords_1(col1))
col2.trace("w", lambda name, index, mode, col2=col2: checkwords_2(col2))
col3.trace("w", lambda name, index, mode, col3=col3: checkwords_3(col3))
master.mainloop()
