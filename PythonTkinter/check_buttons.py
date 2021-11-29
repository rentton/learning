from tkinter import *

#We have to define the principal screen
root = Tk()
root.title("Using radio buttons")

#Defining the principal frame in the screen
my_frame = Frame()
my_frame.pack()

option = IntVar()
option2 = IntVar()


def get():
    print(option.get())
    if option.get() == 1:
        result1.config(text="hello, male")
    elif option2.get() == 1:
        result2.config(text="hello, female")
    
    
    

rb1 = Checkbutton(my_frame, text="Male", variable=option, command = get)
rb1.pack()
rb2 = Checkbutton(my_frame, text="Female", variable=option2, command = get)
rb2.pack()

result1 = Label(my_frame,text="")
result1.pack()

result2 = Label(my_frame,text="")
result2.pack()


root.mainloop()
