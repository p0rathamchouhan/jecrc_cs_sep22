from operator import mod
import tkinter as ttk
import pandas as pd

model =pd.read_pickle('SurvivalPredictionRF.pickle')
app=ttk.Tk()
app.geometry('320x200')
app.title('Titanic Survival Prediction')

cols=['Se_male','Fare','Age']

# Gender
ttk.Label(app,text='Choose Gender',padx=20,pady=20).grid(row=0,column=0)
genders={ 'Male' : 1,
          'Female' :0}
genderVar=ttk.Variable(app)
genderVar.set(genders['Male'])
frame=ttk.Frame(app)
frame.grid(row=0,column=1)
for gender,genderValue in genders.items():
    ttk.Radiobutton(frame,text=gender,variable=genderVar,value=genderValue).pack(side=ttk.LEFT)

# Fare
ttk.Label(app,text='Enter Fair',padx=20,pady=20).grid(row=1,column=0)
fareVar=ttk.DoubleVar(app)
fareVar.set(0.0)
ttk,ttk.Spinbox(app,from_ =0, to =10000,textvariable=fareVar,width=10).grid(row=1,column=1)
#ttk.Entry(app,textvariable=fareVar).grid(row=1,column=1)

# Age
ttk.Label(app,text='Enter Fair',padx=20,pady=20).grid(row=2,column=0)
ageVar=ttk.DoubleVar(app)
ageVar.set(0.0)
ttk,ttk.Spinbox(app,from_ =0, to =150,textvariable=ageVar,width=10).grid(row=2,column=1)
#ttk.Entry(app,textvariable=fareVar).grid(row=1,column=1)

def find_survival():
    global model
    query_df=pd.DataFrame({'Sex_male':[genderVar.get()],'Fare':[fareVar.get()],'Age':[ageVar.get()]})

    pred=model.predict(query_df)
    if pred[0]==1:
        resultVar.set('Might Survive')
    else:
        resultVar.set('MIght NOT Survive!')
    return

ttk.Button(app,text='Check',command=find_survival,padx=20,pady=20).grid(row=3,column=0,columnspan=20)

# Result
resultVar=ttk.Variable(app)
ttk.Label(app,textvarible=resultVar,font=('Times New Roman',20)).grid(row=4,column=0,columnspan=2)
app.mainloop()