from tkinter import *
from datetime import date
from tkinter.ttk import Combobox
import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from matplotlib.figure import Figure
import numpy as np 
import matplotlib.pyplot as plt 
from backend import *

background = "#f0ddd5"
framebg = "#62a7ff"
framefg = "#fefbfb"

root = Tk()
root.title ("Heart Disease  Prediction System")
root.geometry ("1450x730+60+80")
root.resizable(False,False)
root.config(bg = background)

count = 0

def increment_and_analyze():
    global count
    count += 1
    analysis(count)


#Analysis 
def analysis(count):
    name = Name.get()
    D1 = Date.get()
    today = datetime.date.today()
    A= today.year-DOB.get()

    try:
        B= selection()
    except:
        messagebox.showerror("missing", "Please select gender!")
        return
    
    try:
        F = selection2()
    except:
        messagebox.showerror("missing", "Please select fbs!")
        return
    
    try:
        I = selection3()
    except:
        messagebox.showerror("missing", "Please select exang!")
        return
        
    try:
        C = int(selection4())
    except:
        messagebox.showerror("missing", "Please select cp!")
        return
    
    try:
        G = int(restecg_combobox.get())
    except:
        messagebox.showerror("missing", "Please select restcg!")
        return

    try:
        K = int(selection5())
    except:
        messagebox.showerror("missing", "Please select slope!")
        return

    try:
        L = int(ca_combobox.get())
    except:
        messagebox.showerror("missing", "Please select ca!")
        return

    try:
        M = int(thal_combobox.get())
    except:
        messagebox.showerror("missing", "Please select thal!")
        return

    try:
        D = int(trestbps.get())
        E = int(chol.get())
        H = int(thalach.get())
        J = float(oldpeak.get())
    except:
        messagebox.showerror("missing data", "Data entries missing!")
        return

    #graph 1
    f = Figure(figsize=(5,5),dpi=100)
    a = f.add_subplot(111)
    a.plot(["Sex","fbs","exang"],[B,F,I])
    canvas = FigureCanvasTkAgg(f)
    canvas.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
    canvas._tkcanvas.place(width=250,height=250,x=600,y=240)

    #graph 2
    f2 = Figure(figsize=(5,5),dpi=100)
    a2 = f2.add_subplot(111)
    a2.plot(["age","trestbps","chol","thalach"],[A,D,E,H])
    canvas2 = FigureCanvasTkAgg(f2)
    canvas2.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
    canvas2._tkcanvas.place(width=250,height=250,x=860,y=240)

    #graph 3
    f3 = Figure(figsize=(5,5),dpi=100)
    a3 = f3.add_subplot(111)
    a3.plot(["oldpeak","resticg","cp"],[J,G,C])
    canvas3 = FigureCanvasTkAgg(f3)
    canvas3.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
    canvas3._tkcanvas.place(width=250,height=250,x=600,y=470)

    #graph 4
    f4 = Figure(figsize=(5,5),dpi=100)
    a4 = f4.add_subplot(111)
    a4.plot(["slope","ca","thal"],[K,L,M])
    canvas4 = FigureCanvasTkAgg(f4)
    canvas4.get_tk_widget().pack(side=tk.BOTTOM,fill=tk.BOTH,expand=True)
    canvas4._tkcanvas.place(width=250,height=250,x=860,y=470)

    #input data
    input_data = (A,B,C,D,E,F,G,H,I,J,K,L,M)

    input_data_as_numpy_array=np.asanyarray(input_data)

    input_data_reshape = input_data_as_numpy_array.reshape(1, -1)
    prediction = model.predict(input_data_reshape)
    print(prediction[0])

    if (prediction[0] == 0):
        print("This individual is not at risk for Heart Disease")
        report.config(text=f"Report:{count}",fg="#8dc63f")
        report1.config(text=f"{name}is not at risk for heart disease")
    
    else:
        print("The Individual is at risk for Heart Disease")
        report.config(text=f"Report:{count}",fg="#ed1c24")
        report1.config(text=f"{name} is at risk for heart disease")

#info window 
def Info():
    Icon_window=Toplevel(root)
    Icon_window.title("Info")
    Icon_window.geometry("700x600+300+100")

    #icon
    icon_image=PhotoImage(file="Images/info.png")
    Icon_window.iconphoto(False,icon_image)

    Label(Icon_window,text="Information Related to dataset",font="robot 17 bold").pack(padx=20,pady=20)

    #info
    Label(Icon_window,text="age - age in years",font="arial 11").place(x=20,y=100)
    Label(Icon_window,text="sex - sex (1- male; 0 - female)",font="arial 11").place(x=20,y=130)
    Label(Icon_window,text="cp - chest pain type (0 - typical angina; 1 - atypical angina; 2 - non-anginal pain; 3 - asymptomatic)",font="arial 11").place(x=20,y=160)
    Label(Icon_window,text="trestbps - resting blood pressure (in mm Hg on admission to the hospital)",font="arial 11").place(x=20,y=190)
    Label(Icon_window,text="chol - serum cholestroal in mg/dl",font="arial 11").place(x=20,y=220)
    Label(Icon_window,text="fbs - fasting blood sugar > 120mg/dl (1 - True; 0 - False)",font="arial 11").place(x=20,y=250)
    Label(Icon_window,text="resteg resting electrocardiographic results (0 - normal 1 - having ST-T; 2 - hypertrophy)",font="arial 11").place(x=20,y=280)
    Label(Icon_window,text="thalach - maximum heart rate achieved",font="arial 11").place(x=20,y=310)
    Label(Icon_window,text="exang - exercise induced angina ( 1- yes; 0 - no)",font="arial 11").place(x=20,y=340)
    Label(Icon_window,text="oldpeak - ST depression induced by exercise relative to rest",font="arial 11").place(x=20,y=370)
    Label(Icon_window,text="slope - the slope of the peak exercise ST segment (0 - upsloping; 1 - flat; 2- downsloping)",font="arial 11").place(x=20,y=400)
    Label(Icon_window,text="ca - number of major vessels (0-3) colored by flourosopy",font="arial 11").place(x=20,y=430)
    Label(Icon_window,text="thal - 0 = normal; 1 = fixed defect; 2 = reversable defect",font="arial 11").place(x=20,y=460)



    Icon_window.mainloop()

def logout():
    root.destroy()


def Clear():
    Name.get('')
    DOB.get('')
    trestbps.get('')
    chol.get('')
    thalach.set('')
    oldpeak.set('')


#icon 1
image_icon = PhotoImage(file="Images/icon.png")
root.iconphoto(False,image_icon)

#Header Section 
logo = PhotoImage(file = "Images/header.png")
myimage=Label (image = logo,bg=background)
myimage.place(x=0,y=0)

Heading_entry=Frame(root,width=800,height = 190,bg="#df2d4b")
Heading_entry.place(x=600,y=20)

Label(Heading_entry,text = "Registration No.",font = "arial 13",bg = "#df2d4b",fg=framefg).place(x=30,y=0)
Label(Heading_entry,text = "Date",font = "arial 13",bg = "#df2d4b",fg=framefg).place(x=430,y=0)

Label(Heading_entry,text = "Patiant Name",font = "arial 13",bg = "#df2d4b",fg=framefg).place(x=30,y=90)
Label(Heading_entry,text = "Birth Year",font = "arial 13",bg = "#df2d4b",fg=framefg).place(x=430,y=90)

Entry_Image=PhotoImage(file="Images/Rounded Rectangle 1.png")
Entry_Image2 = PhotoImage(file="Images/Rounded Rectangle 2.png")
Label(Heading_entry,image=Entry_Image,bg="#df2d4b").place(x=20,y=30)
Label(Heading_entry,image=Entry_Image,bg="#df2d4b").place(x=430,y=30)

Label(Heading_entry,image=Entry_Image2,bg="#df2d4b").place(x=20,y=120)
Label(Heading_entry,image=Entry_Image2,bg="#df2d4b").place(x=430,y=120)

Registration = IntVar()
reg_entry = Entry(Heading_entry,textvariable = Registration,width = 30,font = "arial 15",bg = "#0e5363",fg="white",bd=0)
reg_entry.place(x=30,y=45)

Date = StringVar()
today = date.today()
d1 = today.strftime("%d/%m/%Y")
date_entry = Entry(Heading_entry,textvariable=Date,width=15,font='aria; 15',bg="#0e5363",fg="white",bd=0)
date_entry.place(x=500,y=45)
Date.set(d1)

Name = StringVar()
name_entry = Entry(Heading_entry,textvariable = Name,width = 20,font = "arial 20",bg = "#ededed",fg="#222222",bd=0)
name_entry.place(x=30,y=130)

DOB = IntVar()
dob_entry = Entry(Heading_entry,textvariable = DOB,width = 20,font = "arial 20",bg = "#ededed",fg="#222222",bd=0)
dob_entry.place(x=450,y=130)

#Body
Detail_entry=Frame(root,width=490,height=260,bg="#dbe0e3",bd=1)
Detail_entry.place(x=30,y=450)

#radio button
Label(Detail_entry,text="sex:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=10)
Label(Detail_entry,text="fbs:",font="arial 13",bg=framebg,fg=framefg).place(x=180,y=10)
Label(Detail_entry,text="exang:",font="arial 13",bg=framebg,fg=framefg).place(x=335,y=10)


def selection():
    if gen.get()==1:
        Gender = 1
        return (Gender)
        print(Gender)
    elif gen.get()==2:
        Gender = 0
        return (Gender)
        print(Gender)
    else:
        print(Gender)
    

def selection2():
    if fbs.get()==1:
        Fbs = 1
        return (Fbs)
        print(Fbs)
    elif fbs.get()==2:
        Fbs = 0
        return (Fbs)
        print(Fbs)
    else:
        print(Fbs)

def selection3():
    if exang.get()==1:
        Exang = 1
        return (Exang)
        print(Exang)
    elif exang.get()==2:
        Exang = 0
        return (Exang)
        print(Exang)
    else:
        print(Exang)

gen = IntVar()
R1 = Radiobutton(Detail_entry,text='Male',variable = gen,value = 1,command = selection)
R2 = Radiobutton(Detail_entry,text='Female',variable = gen,value = 2,command = selection)
R1.place(x=43,y=10)
R2.place(x=93,y=10)

fbs = IntVar()
R3 = Radiobutton(Detail_entry,text='True',variable = fbs,value = 1,command = selection2)
R4 = Radiobutton(Detail_entry,text='False',variable = fbs,value = 2,command = selection2)
R3.place(x=213,y=10)
R4.place(x=263,y=10)

exang = IntVar()
R5 = Radiobutton(Detail_entry,text='Yes',variable = exang,value = 1,command = selection3)
R6 = Radiobutton(Detail_entry,text='No',variable = exang,value = 2,command = selection3)
R5.place(x=387,y=10)
R6.place(x=430,y=10)



Label(Detail_entry,text="cp",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=50)
Label(Detail_entry,text="restecg",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=90)
Label(Detail_entry,text="slope:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=130)
Label(Detail_entry,text="ca:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=170)
Label(Detail_entry,text="thal:",font="arial 13",bg=framebg,fg=framefg).place(x=10,y=210)

def selection4():
    input=cp_combobox.get()
    if input == "0 = typical angina":
        return(0)
    elif input == '1 = atypical angina':
        return (1)
    elif input == '2 = non-anginal pain':
        return (2)
    elif input == '3 = asymptomatic':
        return(3)
    
def selection5():
    input=slope_combobox.get()
    if input == "0 = upsloping":
        return(0)
    elif input == '1 = flat':
        return (1)
    elif input == '2 = downsloping':
        return (2)

cp_combobox=Combobox(Detail_entry,values=['0 = typical angina','1 = atypical angina','2 = non-anginal pain','3 = asymptomatic' ],font="arial 12",state="r",width=14)
restecg_combobox=Combobox(Detail_entry,values=['0','1','2'],font="arial 12",state="r",width=11)
slope_combobox=Combobox(Detail_entry,values=['0 = upsloping','1 = flat','2 = downsloping'],font="arial 12",state="r",width=12)
ca_combobox=Combobox(Detail_entry,values=['0','1','2','3','4'],font="arial 12",state="r",width=14)
thal_combobox=Combobox(Detail_entry,values=['0','1','2','3'],font="arial 12",state="r",width=14)

cp_combobox.place(x=50,y=50)
restecg_combobox.place(x=80,y=90)
slope_combobox.place(x=70,y=130)
ca_combobox.place(x=50,y=170)
thal_combobox.place(x=50,y=210)


#Data Entry Box

Label(Detail_entry,text="Smoking:",font="arial 13",width = 7, bg = "#dbe0e3",fg="black").place(x=240,y=50)
Label(Detail_entry,text="trestbps:",font="arial 13",width = 7, bg = framebg,fg="white").place(x=240,y=90)
Label(Detail_entry,text="chol:",font="arial 13",width = 7, bg = framebg,fg="white").place(x=240,y=130)
Label(Detail_entry,text="thalach:",font="arial 13",width = 7, bg = framebg,fg="white").place(x=240,y=170)
Label(Detail_entry,text="oldpeak:",font="arial 13",width = 7, bg = framebg,fg="white").place(x=240,y=210)

trestbps = StringVar()
chol = StringVar()
thalach = StringVar()
oldpeak = StringVar()

trestbps_entry = Entry(Detail_entry,textvariable = trestbps,width = 10,font = "arial 15",bg = "#ededed",fg="#222222",bd=0)
chol_entry = Entry(Detail_entry,textvariable = chol,width = 10,font = "arial 15",bg = "#ededed",fg="#222222",bd=0)
thalach_entry = Entry(Detail_entry,textvariable = thalach,width = 10,font = "arial 15",bg = "#ededed",fg="#222222",bd=0)
oldpeak_entry = Entry(Detail_entry,textvariable = oldpeak,width = 10,font = "arial 15",bg = "#ededed",fg="#222222",bd=0)
trestbps_entry.place(x=320,y=90)
chol_entry.place(x=320,y=130)
thalach_entry.place(x=320,y=170)
oldpeak_entry.place(x=320,y=210)



#Report
report = Label(root,text="",font="arial 25 bold",bg="#f8dcd4",fg="#8dc63f")
report.place(x=1170,y=350)

report1 = Label(root,text="",font="arial 12 bold",bg="#f8dcd4")
report1.place(x=1150,y=410)


#Graph
graph_image=PhotoImage(file="Images/graph.png")
Label(image=graph_image).place(x=600,y=270)
Label(image=graph_image).place(x=860,y=270)
Label(image=graph_image).place(x=600,y=500)
Label(image=graph_image).place(x=860,y=500)

##Button
analysis_button = PhotoImage(file="Images/Analysis.png")
Button(root, image=analysis_button, bd=0, bg=background, cursor='hand2', command=increment_and_analyze).place(x=1130, y=240)

#info button
info_button = PhotoImage(file="Images/info.png")
Button(root,image=info_button,bd=0,bg=background,cursor='hand2',command = Info).place(x=10,y=240)

#Save button
save_button = PhotoImage(file="Images/save.png")
Button(root,image=save_button,bd=0,bg=background,cursor='hand2').place(x=1370,y=250)

#Smoke and Non Smoke

button_mode = True
choice = "smoking"

def changemode():
    global button_mode
    global choice

    if button_mode:
        choice = "non_smoking"
        mode.config(image=non_smoking_icon,activebackground="white")
        button_mode = False
    else:
        choice = "smoking"
        mode.config(image=smoking_icon,activebackground="white")
        button_mode = True
    
    print(choice)

smoking_icon = PhotoImage(file="Images/smoker.png")
non_smoking_icon = PhotoImage(file = "Images/non-smoker.png")

mode = Button(root,image=smoking_icon,bg = "#dbe0e3",bd=0,cursor = "hand2",command=changemode)
mode.place(x=350,y=495)


#Log Out Button

logout_icon = PhotoImage(file="Images/logout.png")
logout_button=Button(root,image=logout_icon,bg="#df2d4b",cursor="hand2",bd=0,command=logout)
logout_button.place(x=1390,y=60)


root.mainloop()
