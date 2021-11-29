from tkinter import *
#pop-up windows
from tkinter import messagebox


#We have to define the principal screen
root = Tk()

#pop-up
def popup():
    print("entra")
    messagebox.showinfo("Hello World", 
                        "Hello World is a normal first program")

def _exit():
    if messagebox.askquestion("Exit","Do u want to exit?"):
        root.destroy()
        

#Create
menu_bar = Menu(root)
#Add in the route
root.config(menu=menu_bar)

#Add the menu in the bar
file = Menu(menu_bar, tearoff=0)
file.add_command(label="new", command=popup)
# file.add_separator()
file.add_command(label="exit", command = _exit)
#Add the submenu
#tearoff remove weird lines
edit = Menu(menu_bar, tearoff = 0)
edit.add_command(label="copy")
edit.add_command(label="cut")


menu_bar.add_cascade(label="File",menu=file)
menu_bar.add_cascade(label="Edit",menu=edit)


root.mainloop()

