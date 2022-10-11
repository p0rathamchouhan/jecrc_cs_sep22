# GUI - Graphical Interface
# Libraries
############## 
# 1. Tkinter
# 2. PyQT
# 3. Turtle

import tkinter as ttk
app=ttk.Tk()

app.title('My App')
app.geometry('1080x1081')

msg=ttk.Variable(app)


ttk.Label(app,text='A Simple Text Label').place(x=50,y=50)
ttk.Label(app,textvariable=msg, font=('ALgerian',25)).place(x=100,y=70)
ttk.Label(app,textvariable=msg).place(x=100,y=70)

def abc():
    print('Wow')
    msg.set('Jo tera mann kare')
ttk.Button(app,text='Isko Click Kardo',command=abc).place(x=100,y=120)
ttk.Button(app,text='He wala bhi hai',command= lambda:msg.set('Pata nahi')).place(x=100,y=170)

f1=ttk.Variable(app)
f1.set('0')
f2=ttk.Variable(app)
f2.set('0')
result=ttk.Variable(app)

ttk.Entry(app,textvariable=f1,font=('Arial',22)).place(x=50,y=200)
ttk.Entry(app,textvariable=f2,font=('Arial',22)).place(x=150,y=200)
ttk.Label(app,text='Result').place(x=100,y=300)
ttk.Label(app,textvariable=result,font=('Arial',22)).place(x=100,y=330)
def calci(op):
    print('I will calculate')
    result.set(eval(f1.get()+op+f2.get()))
ttk.Button(app,text='+',command=lambda:calci('+'),font=('Arial',22)).place(x=50,y=240)
ttk.Button(app,text='-',command=lambda:calci('-'),font=('Arial',22)).place(x=100,y=240)
ttk.Button(app,text='*',command=lambda:calci('*'),font=('Arial',22)).place(x=150,y=240)
ttk.Button(app,text='/',command=lambda:calci('/'),font=('Arial',22)).place(x=200,y=240)



box=ttk.Listbox(app,height=5,fg='red',activestyle='dotbox')
box.insert(1,'Sample1')
box.insert(2,'Sample2')
box.insert(3,'Sample3')
box.place(x=350,y=40)

def show():
    print(box.get(box.curselection()))

ttk.Button(app,text='show',command=show).place(x=350,y=250)
app.mainloop()