from tkinter import *
from tkinter import ttk

root = Tk()
root.title('tabs app')
root.geometry("500x500")

my_notebook = ttk.Notebook(root)
my_notebook.pack()

def hide():
    my_notebook.hide(1)

def show():
    my_notebook.add(my_frame2, text="Tab Two")    

def select():
    my_notebook.select(1)

my_frame1 = Frame(my_notebook, width=500, height=500, bg="yellow")
my_frame2 = Frame(my_notebook, width=500, height=500, bg="blue")

my_frame1.pack(fill="both", expand=1)
my_frame2.pack(fill="both", expand=1)

my_notebook.add(my_frame1, text="Menu")
my_notebook.add(my_frame2, text="Tab Two")

my_button = Button(my_frame1, text="Hide Tab 2", command=hide).pack(pady=5, side='top', padx=5, anchor=W)
my_button2 = Button(my_frame1, text="Show Tab 2", command=show).pack(pady=5, side='top', padx=5, anchor=W)
my_button3 = Button(my_frame1, text="Navigate To Tab 2", command=select).pack(pady=5, side='top', padx=5, anchor=W)

root.mainloop()