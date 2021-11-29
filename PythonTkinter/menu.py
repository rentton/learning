from tkinter import *

#We have to define the principal screen
root = Tk()
root.title("Using menu")

#Create
menu_bar = Menu(root)
#Add in the route
root.config(menu=menu_bar)

#Add the menu in the bar
file = Menu(menu_bar, tearoff=0)
file.add_command(label="new")
file.add_separator()
file.add_command(label="save")
#Add the submenu
#tearoff remove weird lines
edit = Menu(menu_bar, tearoff = 0)
edit.add_command(label="copy")
edit.add_command(label="cut")


menu_bar.add_cascade(label="File",menu=file)
menu_bar.add_cascade(label="Edit",menu=edit)



#Defining the principal frame in the screen
my_frame = Frame()
my_frame.pack()

option = IntVar()


result = Label(my_frame,text="")
result.pack()

root.mainloop()

