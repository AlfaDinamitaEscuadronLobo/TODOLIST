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




#------------INTERFAZ 2

def interfaz2():
    global ventana2
    ventana2=Toplevel()
    ventana2.geometry("600x900")
    ventana2.resizable(0,0)

    Frame21=Frame(ventana2,width=1500,height=900)
    Frame21.config(bg="#e0d8c3")
    Frame21.pack()





    ventana2.mainloop()


#-----BOTON COMENZAR
img2=PhotoImage(file="comenzar.png")
label01img=Label(Frame1,image=img2,bg="#e0d8c3")


botoncom1=Button(interfaz1,image=img2,bg="#e0d8c3",borderwidth=0,width=290,height=90,command=interfaz2).place(x=140,y=740)

interfaz1.mainloop()
