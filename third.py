from Tkinter import *

window = Tk()

window.title("Third Example")
window.state('zoomed')

combo = Combobox(window)
combo['values'] = (1,2,3,4,5,"Text")
combo.current(1)#set the selected item
combo.grid(column=0,row=0)
window.mainloop()