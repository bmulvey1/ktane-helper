from tkinter import *
import sys
import os.path

master = Tk()

box_size = 80

# all coords are row, column
maze_circles = [[21, 36], [42, 25], [44, 46], [11, 41], [64, 35], [53, 15], [12, 62], [14, 43], [51, 23]]
if hasattr(sys, '_MEIPASS'):
    maze1 = PhotoImage(file=os.path.join(sys._MEIPASS, './images/maze1.png'))
    maze2 = PhotoImage(file=os.path.join(sys._MEIPASS, './images/maze2.png'))
    maze3 = PhotoImage(file=os.path.join(sys._MEIPASS, './images/maze3.png'))
    maze4 = PhotoImage(file=os.path.join(sys._MEIPASS, './images/maze4.png'))
    maze5 = PhotoImage(file=os.path.join(sys._MEIPASS, './images/maze5.png'))
    maze6 = PhotoImage(file=os.path.join(sys._MEIPASS, './images/maze6.png'))
    maze7 = PhotoImage(file=os.path.join(sys._MEIPASS, './images/maze7.png'))
    maze8 = PhotoImage(file=os.path.join(sys._MEIPASS, './images/maze8.png'))
    maze9 = PhotoImage(file=os.path.join(sys._MEIPASS, './images/maze9.png'))
else:
    maze1 = PhotoImage(file='./images/maze1.png')
    maze2 = PhotoImage(file='./images/maze2.png')
    maze3 = PhotoImage(file='./images/maze3.png')
    maze4 = PhotoImage(file='./images/maze4.png')
    maze5 = PhotoImage(file='./images/maze5.png')
    maze6 = PhotoImage(file='./images/maze6.png')
    maze7 = PhotoImage(file='./images/maze7.png')
    maze8 = PhotoImage(file='./images/maze8.png')
    maze9 = PhotoImage(file='./images/maze9.png')

input_frame = Frame(master, width=90, height=480)
input_frame.grid(row=0, column=0)

circle1_temp = StringVar()
circle1_input = Entry(input_frame, textvariable=circle1_temp)
circle1_input.grid(row=0, column=1)
circle1_label = Label(input_frame, text='Circle 1')
circle1_label.grid(row=0, column=0)

goal_temp = StringVar()
goal_input = Entry(input_frame, textvariable=goal_temp)
goal_input.grid(row=2, column=1)
goal_label = Label(input_frame, text='Goal')
goal_label.grid(row=2, column=0)

location_temp = StringVar()
location_input = Entry(input_frame, textvariable=location_temp)
location_input.grid(row=3, column=1)
location_label = Label(input_frame, text='Location')
location_label.grid(row=3, column=0)

status = Label(input_frame, text='...')
status.grid(row=4, column=1)

maze_display = Canvas(master, width=480, height=480)
maze_display.grid(row=0, column=1)


def getmaze():
    location = int(circle1_temp.get())
    for i in maze_circles:
        if location in i:
            maze = maze_circles.index(i) + 1
            drawmaze(maze)
            status.config(text='Maze %s' % str(maze))
            break
        else:
            status.config(text='Invalid circle location')


def drawmaze(maze):
    exec(f'maze_display.create_image(240, 240, image=maze{maze})')
    goal = goal_temp.get()
    goal_y1 = int(goal[0]) * box_size
    goal_x1 = int(goal[1]) * box_size
    goal_y2 = int(goal[0]) * box_size - box_size
    goal_x2 = int(goal[1]) * box_size - box_size
    goal_loc = maze_display.create_rectangle(goal_x1, goal_y1, goal_x2, goal_y2, width='2')
    loc = location_temp.get()
    loc_y1 = int(loc[0]) * box_size
    loc_x1 = int(loc[1]) * box_size
    loc_y2 = int(loc[0]) * box_size - box_size
    loc_x2 = int(loc[1]) * box_size - box_size
    loc_loc = maze_display.create_oval(loc_x1, loc_y1, loc_x2, loc_y2, width='2')


submit_button = Button(input_frame, text='Submit', command=getmaze)
submit_button.grid(row=5, column=1)


def reset():
    circle1_temp.set('')
    goal_temp.set('')
    location_temp.set('')
    maze_display.delete("all")
    status.config(text='...')



reset_button = Button(input_frame, text='Reset all', command=reset)
reset_button.grid(row=6, column=1)
master.mainloop()
