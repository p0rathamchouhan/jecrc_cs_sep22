# GUI - Graphical Interface
# Libraries
############## 
# 1. Tkinter
# 2. PyQT
# 3. Turtle

import tkinter as ttk
app=ttk.Tk()

app.title('My App')
app.geometry('600x400')

ttk.Label(app,text='A Simple Text Label').place(x=250,y=180)
ttk.Label(app,text='Pratham Chouhan Yash Raj').place(x=300,y=200)
app.mainloop()