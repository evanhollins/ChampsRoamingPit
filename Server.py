import waitress
from Application import app
from tkinter import *

start = Tk()
Label(start, text="Which port should the server run on?").grid(row = 0, column = 0)
e1 = Entry(start)
e1.grid(row = 1, column = 0)
e1.insert(0, "8080")
Button(start, text='Enter', command=start.quit()).grid(row = 2, column=0)
start.mainloop()

# top = Tk()
# w = Label(top, text="Champs Inspection Software", font="Arial 18 bold")
# w.pack()
#
# top.mainloop()

# waitress.serve(app, listen="*:8080")