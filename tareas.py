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
    
    #---------------IMAGEN------------
    imga2=PhotoImage(file="icono2.png")
    labelima2=Label(Frame21,image=imga2,bg="#e0d8c3")
    

    #---------------LABEEL------------
    label21=Label(Frame21,text="INICIAR SESION",bg="#e0d8c3",font=("Monofonto",35),fg="black")

    labelusua=Label(Frame21,text="Usuario",bg="#e0d8c3",font=("Monofonto",28),fg="black")
    labelcontraseña=Label(Frame21,text="Contraseña",bg="#e0d8c3",font=("Monofonto",28),fg="black")


    #segundo global
    global noom_usu_ingre
    global password_usu_ingre
    
    #GLOBAL
    global nom_user
    global password_usu
    #StringVAR
    nom_user=StringVar()
    password_usu=StringVar()
#
# ---LABEL usuario
    iconuser=PhotoImage(file="iconologin2.png")
    labelicon=Label(Frame21,image=iconuser,bg="#e0d8c3")
    Frame(ventana2,width=300,height=3,bg="black").place(x=110,y=690)

 # ---LABEL CONTRASEÑA
    iconcon=PhotoImage(file="iconcontra.png")
    labelicontr=Label(Frame21,image=iconcon,bg="#e0d8c3")

    Frame(ventana2,width=300,height=3,bg="black").place(x=110,y=790)


    labelicon.place(x=60,y=655)
    labelicontr.place(x=60,y=755)




#---------------UBICACION------------
    labelima2.place(x=40,y=90)
    label21.place(x=130,y=530)
    labelusua.place(x=60,y=600)
    labelcontraseña.place(x=60,y=700)


    Frame21.pack()





    ventana2.mainloop()


#-----BOTON COMENZAR
img2=PhotoImage(file="comenzar.png")
label01img=Label(Frame1,image=img2,bg="#e0d8c3")


botoncom1=Button(interfaz1,image=img2,bg="#e0d8c3",borderwidth=0,width=290,height=90,command=interfaz2).place(x=140,y=740)

interfaz1.mainloop()
