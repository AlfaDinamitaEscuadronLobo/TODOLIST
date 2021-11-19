from tkinter import *
from tkinter import messagebox
from tkinter import font
#from tkinter import font


import pymysql

interfaz1= Tk()
#-- ventana
interfaz1.geometry("600x900")
interfaz1.resizable(0,0)

Frame1=Frame(interfaz1,width=1500,height=900)
Frame1.config(bg="#e0d8c3")


#------LABEL 

img1=PhotoImage(file="iconota.png")

label0img=Label(Frame1,image=img1,bg="#e0d8c3")
label2=Label(Frame1,text="TO DO",bg="#e0d8c3",font=("Monofonto",40),fg="black")

label3=Label(Frame1,text="Una  aplicacion sencilla para la \ngestion de tareas,Sientase libre \nde expresar sus ideas ",bg="#e0d8c3",font=("Source Code Pro",18),fg="black")

#-----POSIUC

label0img.place(x=70,y=90)
label2.place(x=230,y=550)
label3.place(x=50,y=620)
Frame1.pack()
interfaz1.mainloop()
