import tkinter as ttk
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from PIL import ImageTk,Image

data = pd.read_csv(r'Training/Trademill_User/treadmil-users.csv')

app=ttk.Tk()
app.geometry('600x300')
app.title('Treadmil User Analysis')

graphs=ttk.Variable(app)
values=['Select'] + list(data.columns)
value={'Pair Plot':'sns.pairplot(data = data)',
        'Joint Plot':"sns.jointplot(data = data,x='{col1}',y='{col2}')",
        'Bar Plot':"sns.barplot(data = data,x='{col1}',y='{col2}')"
        }
graphs.set('Pair Plot')
y=10
for key,value in value.items():
    ttk.Radiobutton(app,text=key,variable=graphs,value=value).place(x=10,y=y)
    y += 20
## option menu
# option 1
col1 = ttk.Variable(app)
col1.set(values[0])
ttk.Label(app,text='Column 1').place(x=150,y=10)
ttk.OptionMenu(app,col1, *values).place(x=150,y=40)

col2 = ttk.Variable(app)
col2.set(values[0])
ttk.Label(app,text='Column 2').place(x=150,y=80)
ttk.OptionMenu(app,col2, *values).place(x=150,y=110)

col3 = ttk.Variable(app)
col3.set(values[0])
ttk.Label(app,text='Column 3').place(x=150,y=150)
ttk.OptionMenu(app,col3, *values).place(x=150,y=180)


# CANVAS
cnv=ttk.Canvas(app,width=200,height=200)
cnv.place(x=200,y=100)

# Label
result=ttk.Variable(app)
ttk.Label(app,textvariable=result).place(x=300,y=200)
def show():
    global cnv
    global img
    #print(graphs.get())
    column1=col1.get()
    column2=col2.get()
    column3=col3.get()
    
    g=graphs.get()
    if'col1' in g:
        if column1=='Select':
            result.set('Column 1 must be selected')
            return
    if'col2' in g:
        if(column2=='Select'):
            result.set('Column 2 must be selected')
            return
    if'col3' in g:
        if column3=='Select':
            result.set('Column 3 must be selected')
            return

    fig=plt.figure(figsize=(5,2))
    eval(g.format(col1=column1,col2=column2,col3=column3))
    fig.savefig('graph.png')
    img=ImageTk.PhotoImage(Image.open('graph.png').resize((250,200)))

    
    cnv.create_image(0,0,anchor=ttk.NW,image=img)

ttk.Button(app,text='Show',command=show).place(x=400,y=10)


app.mainloop()