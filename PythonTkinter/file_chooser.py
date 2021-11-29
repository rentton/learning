from tkinter import *
#pop-up windows
from tkinter import filedialog


#We have to define the principal screen
root = Tk()

#pop-up
def file():
    f = filedialog.askopenfile(title="Open", initialdir="C:", 
                               filetypes =(("texto files","*.txt"),("python files","*.py")))
    print(f)    

Button(root,text="Push",command=file).pack()

root.mainloop()

