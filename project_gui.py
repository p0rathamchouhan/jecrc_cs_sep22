import tkinter as ttk
import pandas as pd

app = ttk.Tk()
model = pd.read_pickle('laptop.pickle')

app.geometry('400x500')
app.title('Laptop resell price prediction')

ram = ttk.Variable(app)
ram.set('0')
ttk.Label(app, text="RAM",padx=10,pady=10).place(x=20,y=30)
ttk.Spinbox(app, from_=0,to=10000 ,textvariable=ram, width='20',).place(x=20,y=70)

rom = ttk.Variable(app)
rom.set('0')
ttk.Label(app, text="Total Memory (ROM) ",padx=10,pady=10).place(x=200,y=30)
ttk.Spinbox(app, from_=0,to=10000 ,textvariable=rom, width='20',).place(x=200,y=70)

value={'Workstation':[1],
        'other':[0],
        }

y=140
Tn= ttk.Variable(app)
ttk.Label(app, text="Type Name",padx=10,pady=10).place(x=20,y=100)
for key,value in value.items():
    ttk.Radiobutton(app, text=key ,variable=Tn,value=value).place(x=20,y=y)
    y=y+20

val=['Intel',
     'Samsung',
     'AMD'
    
]

ttk.Label(app, text="CPU",padx=10,pady=10).place(x=20,y=200)
frame=ttk.Frame(app)
frame.place(x=20,y=250)
box=ttk.Listbox(frame,width=20 ,height=3)
box.place(x=10,y=10)
for type in val:
    box.insert(ttk.END, type)
box.pack(side='left', fill='y')

result = ttk.Variable(app)

def pred():
    global model
    x=box.get(box.curselection())
    if x=='Intel':
        a=1
    else:
        a=0
    
    if x=='Samsung':
        b=1
    else:
        b=0
    
    if x=='AMD':
        c=1
    else:
        c=0
    query_data={'Ram':[eval(ram.get())],
                'Memory':[eval(rom.get())],
                'TypeName_Workstation':[Tn.get()],
                'Cpu_Intel':[a],
                'Cpu_AMD':[c],
                'Cpu_Samsung':[b]
                }
    prediction = model.predict(pd.DataFrame(query_data))
    result.set(round(prediction[0],2))

ttk.Button(app, text="Predict", command=pred, font=('Times New Roman',20)).place(x=120,y=370)
ttk.Label(app, text="Amount is in euros", font=('Times New Roman',12)).place(x=100,y=430)

ttk.Label(app, textvariable=result, font=(22)).pack(side=ttk.BOTTOM)

app.mainloop()