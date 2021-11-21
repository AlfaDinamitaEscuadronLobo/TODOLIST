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


#-----------------LABEL------------- 

img1=PhotoImage(file="iconota.png")
label0img=Label(Frame1,image=img1,bg="#e0d8c3")
label2=Label(Frame1,text="TO DO",bg="#e0d8c3",font=("Monofonto",40),fg="black")
label3=Label(Frame1,text="Una  aplicacion sencilla para la \ngestion de tareas,Sientase libre \nde expresar sus ideas ",bg="#e0d8c3",font=("Source Code Pro",18),fg="black")

#----------------PLACE LABEL--------

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
    
    #-----------------------IMAGEN------------
    imga2=PhotoImage(file="icono2.png")
    labelima2=Label(Frame21,image=imga2,bg="#e0d8c3")
    

    #----------------------LABEEL------------
    label21=Label(Frame21,text="INICIAR SESION",bg="#e0d8c3",font=("Monofonto",35),fg="black")
    labelusua=Label(Frame21,text="Usuario",bg="#e0d8c3",font=("Monofonto",28),fg="black")
    labelcontraseña=Label(Frame21,text="Contraseña",bg="#e0d8c3",font=("Monofonto",28),fg="black")


    #---------------------segundo global
    global noom_usu_ingre
    global password_usu_ingre
    
    #---------------------GLOBAL
    global nom_user
    global password_usu

    #---------------------StringVAR
    nom_user=StringVar()
    password_usu=StringVar()

    #----------------------ENTRY-------------
    noom_usu_ingre=Entry(ventana2,border=0,textvariable=nom_user,fg="black",font=("Source Code Pro",20),bg="#e0d8c3")
    password_usu_ingre=Entry(ventana2,border=0,textvariable=password_usu,fg="black",font=("Source Code Pro",20),bg="#e0d8c3",show="*")

    #---------------ENTRY LABEL------------
    noom_usu_ingre.place(x=130,y=585,width=280,height=30)
    password_usu_ingre.place(x=130,y=690,width=280,height=30)
    
    # -----------------------LABEL usuario
    iconuser=PhotoImage(file="iconologin2.png")
    iconcon=PhotoImage(file="iconcontra.png")
    labelicon=Label(Frame21,image=iconuser,bg="#e0d8c3")
    labelicontr=Label(Frame21,image=iconcon,bg="#e0d8c3")

    # ----------------------------LABEL FRAME--------------------------

    Frame(ventana2,width=360,height=3,bg="black").place(x=130,y=718)
    Frame(ventana2,width=360,height=3,bg="black").place(x=130,y=618)

    # ----------------------------LABEL ICONO

    labelicon.place(x=80,y=585)
    labelicontr.place(x=80,y=685)

    #-------------------------------LABEL------------
    labelima2.place(x=40,y=50)
    label21.place(x=130,y=470)
    labelusua.place(x=80,y=530)
    labelcontraseña.place(x=80,y=630)


    Frame21.pack()

    img3boton=PhotoImage(file="acceder.png")
    labelboac=Label(image=img3boton)

    botacc=Button(ventana2,image=img3boton,bg="#e0d8c3",borderwidth=0,width=290,height=90,command=interfaz1).place(x=140,y=740)
    #---------------BOTON REGISTRASE------------

    mybuttonregi=Button(ventana2,text="Registrarse",bg="#e0d8c3",fg="black",borderwidth=0,font=("Source Code Pro",15),activebackground="#e0d8c3",command=interfaz3Regi)
    mybuttonregi.place(x=210,y=830)

    




    ventana2.mainloop()

  #----------------------------TERCERA INTERFAZ DE REGISTROO----------------------------------
def interfaz3Regi():
    
    ventana2.destroy() #------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    global ventana3
    ventana3=Toplevel()
    ventana3.geometry("600x900")
    ventana3.resizable(0,0)
    frame3re=Frame(ventana3,width=1500,height=900,bg="#e0d8c3")
    frame3re.pack()
    
    interregis=PhotoImage(file="loginregistro.png")
    i2logo=Label(frame3re,image=interregis,bg="#e0d8c3")
    i2logo.place(x=170,y=10)

    
    global nombre
    global apellido
    global Correo
    global Nuusuario
    global nuevacontraseña
    global repitacontra

    #---------------------Stringvar
    nombre=StringVar()
    apellido=StringVar()
    Correo=StringVar()
    Nuusuario=StringVar()
    nuevacontraseña=StringVar()
  

    
    #LABEL
    lanomb=Label(frame3re,text="Nombres",bg="#e0d8c3",font=("Monofonto",20),fg="black")
    laape=Label(frame3re,text="Apellidos",bg="#e0d8c3",font=("Monofonto",20),fg="black")
    lacorreo=Label(frame3re,text="Correo",bg="#e0d8c3",font=("Monofonto",20),fg="black")
    lanuusu=Label(frame3re,text="Nuevo Usuario",bg="#e0d8c3",font=("Monofonto",20),fg="black")
    lnuevocontr=Label(frame3re,text="Contraseña",bg="#e0d8c3",font=("Monofonto",20),fg="black")
    
    

    #---------------------ENTRYS
    nombre=Entry(ventana3,width=25,bg="#e0d8c3",border=0,textvariable=nombre,fg="black",font=("Source Code Pro",15))
    apellido=Entry(ventana3,width=25,bg="#e0d8c3",border=0,textvariable=apellido,fg="black",font=("Source Code Pro",15))
    Correo=Entry(ventana3,width=25,bg="#e0d8c3",border=0,textvariable=Correo,fg="black",font=("Source Code Pro",15))
    Nuusuario=Entry(ventana3,width=25,bg="#e0d8c3",border=0,textvariable=Nuusuario,fg="black",font=("Source Code Pro",15))
    nuevacontraseña=Entry(ventana3,width=25,bg="#e0d8c3",border=0,textvariable=nuevacontraseña,fg="black",font=("Source Code Pro",15),show="*")
    
    
    #---------------------PLACE LABEL
    lanomb.place(x=90,y=280)
    laape.place(x=90,y=370)
    lacorreo.place(x=90,y=460)
    lanuusu.place(x=90,y=550)
    lnuevocontr.place(x=90,y=640)
    
    
    #---------------------PLACE entry
    nombre.place(x=130,y=320)
    apellido.place(x=130,y=410)
    Correo.place(x=130,y=500)
    Nuusuario.place(x=130,y=590)
    nuevacontraseña.place(x=130,y=680)
    

    #---------------------FRAMES
    Frame(ventana3, width=350, height=3,bg="black").place(x=130,y=350)
    Frame(ventana3, width=350, height=3,bg="black").place(x=130,y=440)
    Frame(ventana3, width=350, height=3,bg="black").place(x=130,y=530)
    Frame(ventana3, width=350, height=3,bg="black").place(x=130,y=620)
    Frame(ventana3, width=350, height=3,bg="black").place(x=130,y=710)
    
    #---------------------ICONOS DE REGISTRO
    iconnom=PhotoImage(file="icon2nom.png")
    iconapel=PhotoImage(file="icon2nom.png")
    iconcor=PhotoImage(file="icon2mensa.png")
    iconusuar1=PhotoImage(file="icon2usu.png")
    iconoPASWOORD=PhotoImage(file="icon2con.png")
    
    icononombre=Label(frame3re,image=iconnom,bg="#e0d8c3")
    iconapellido=Label(frame3re,image=iconapel,bg="#e0d8c3")
    iconocorreo=Label(frame3re,image=iconcor,bg="#e0d8c3")
    iconousuario2=Label(frame3re,image=iconusuar1,bg="#e0d8c3")
    icono2PASWOORD=Label(frame3re,image=iconoPASWOORD,bg="#e0d8c3")
    

    #---------------------PLACE DE ICONOS DE REGISTROSS
    icononombre.place(x=90,y=320)
    iconapellido.place(x=90,y=410)
    iconocorreo.place(x=90,y=500)
    iconousuario2.place(x=90,y=585)
    icono2PASWOORD.place(x=90,y=675)





    crearcuenta=PhotoImage(file="registrarse.png")
    
    mybuttoncrearcuen=Button(ventana3,image=crearcuenta,bg="#e0d8c3",borderwidth=0,width=290,height=90,command=insertar_datos)
    mybuttoncrearcuen.place(x=140,y=740)

    regresar=Button(ventana3,text="Regresar",bg="#e0d8c3",fg="black",borderwidth=0,font=("Source Code Pro",15),activebackground='#e0d8c3',command=interfaz2).place(x=230,y=830,height=32)
    
    ventana3.mainloop()


def insertar_datos():
    
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="geidar",
        db="pytangui"
    )
    cursor=bd.cursor()
    sql="INSERT INTO registrar(Nombres,Apellidos,Correo,Nuevo_Usuario, Contraseña) VALUES('{0}','{1}','{2}','{3}','{4}')".format(nombre.get(),apellido.get(),Correo.get(),Nuusuario.get(),nuevacontraseña.get())
    try:
        cursor.execute(sql)
        bd.commit()
        messagebox.showinfo(message="Registro Existoso",title="Aviso")
    except:
        bd.rollback()
        messagebox.showinfo(message="No registrado", title="Aviso")
        bd.close()
 #---------------------------- ACCESO inicio de sesiooon----------------------------------   
def inicio():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="geidar",
        db="USARIOSLIST"
    )
    fcursor=bd.cursor()
    fcursor.execute("select Contraseña from registrar where Nuevo_Usuario='"+noom_usu_ingre.get()+"' and Contraseña='"+password_usu_ingre.get()+"'")
    if fcursor.fetchall():
        messagebox.showinfo(title="Inicio de Sesion correcto",message="Usted Ingreso Correctamente")
        #interfazquese dirigira()
        
    else:
         messagebox.showinfo(title="Inicio de Sesion Incorrecto",message="Inicio de Sesion Incorrecto")
    bd.close()





#-----BOTON COMENZAR
img2=PhotoImage(file="comenzar.png")
label01img=Label(Frame1,image=img2,bg="#e0d8c3")


botoncom1=Button(interfaz1,image=img2,bg="#e0d8c3",borderwidth=0,width=290,height=90,command=interfaz2).place(x=140,y=740)

interfaz1.mainloop()
