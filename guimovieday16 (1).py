import tkinter as ttk
import pandas as pd
from unittest import result
import warnings

warnings.filterwarnings('ignore')
app=ttk.Tk()
app.geometry('600x600')
app.title('movie recommender') 
#ttk.Label(app, text='enter the movie that you have watched: ').place(x=15,y=15)
cols=['user_id','movie_id','rating','ts']
df=pd.read_csv('u.data', sep='\t', names=cols).drop('ts',axis=1)
item_cols = ['movie_id','title']+ [str(i) for i in range(22)]
df1=pd.read_csv('u.item', sep='|', encoding = "ISO-8859-1", names=item_cols)[['movie_id','title']]
#merge
movie=pd.merge(df,df1,on='movie_id')
result=ttk.Variable(app)
frame=ttk.Frame(app)
frame.place(x=10,y=10)
box=ttk.Listbox(frame,width=80 ,height=20)
box.place(x=10,y=10)
def get_movie():
    pass
for title in movie['title'].unique():
    box.insert(ttk.END, title)
#box.grid(row = , column = )
box.pack(side='left', fill='y')
#box.place(x=10,y=10)

scroll=ttk.Scrollbar(frame, orient=ttk.VERTICAL)
scroll.config(command=box.yview)
box.config(yscrollcommand=scroll.set)
scroll.pack(side='right', fill='y')
        
ttk.Button(app, text='Find recommendations', font=('Arial'),width=22 ,command=get_movie).place(x=10,y=350)
ttk.Label(app, textvariable=result,font=('Arial',22)).place(x=200,y=500)

app.mainloop()