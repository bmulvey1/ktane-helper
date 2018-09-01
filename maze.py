from tkinter import *

master = Tk()

# all coords are row, column
maze1_circles = [21, 36]
maze2_circles = [42, 25]
maze3_circles = [44, 46]
maze4_circles = [11, 41]
maze5_circles = [64, 35]
maze6_circles = [53, 15]
maze7_circles = [12, 62]
maze8_circles = [14, 43]
maze9_circles = [51, 23]

maze1 = PhotoImage(file='images\\maze1.png')
maze2 = PhotoImage(file='images\\maze2.png')
maze3 = PhotoImage(file='images\\maze3.png')
maze4 = PhotoImage(file='images\\maze4.png')
maze5 = PhotoImage(file='images\\maze5.png')
maze6 = PhotoImage(file='images\\maze6.png')
maze7 = PhotoImage(file='images\\maze7.png')
maze8 = PhotoImage(file='images\\maze8.png')
maze9 = PhotoImage(file='images\\maze9.png')

input_frame = Frame(master, width=90, height=480)
input_frame.grid(row=0, column=0)


circle1_temp = StringVar()
circle1_input = Entry(input_frame, textvariable=circle1_temp)
circle1_input.grid(row=0, column=1)
circle1_label = Label(input_frame, text='Circle 1')
circle1_label.grid(row=0, column=0)

circle2_temp = StringVar()
circle2_input = Entry(input_frame, textvariable=circle2_temp)
circle2_input.grid(row=1, column=1)
circle2_label = Label(input_frame, text='Circle 2')
circle2_label.grid(row=1, column=0)

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

maze_display = Canvas(master, width=480, height=480)
maze_display.grid(row=0, column=1)











submit_button = Button(input_frame, text='Submit')
submit_button.grid(row=4, column=1)

master.mainloop()
