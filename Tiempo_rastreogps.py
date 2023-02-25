import math
from tkinter import *

raiz = Tk()
raiz.title("Tiempo de Rastreo")
raiz.geometry('400x300')
raiz.config(bg= '#E6E6FA')
raiz.resizable(False, False)

fondo = Frame(raiz, width=300, height=250, bg='#F8F8FF')
x = (raiz.winfo_width() - fondo.winfo_reqwidth()) / 2
y = (raiz.winfo_height() - fondo.winfo_reqheight()) / 2
fondo.place(x=80, y=50)


def validar_input(nuevo_valor):
    if nuevo_valor.isdigit() or nuevo_valor == "":
        # Permitir solo números o un campo vacío
        return True
    else:
        # No permitir otros caracteres
        return False

validacion = fondo.register(validar_input)


def DistKm():
    
    lat1 = float(textPunto1.get())
    lon1 = float(textPunto2.get())
    lat2 = float(textPunto3.get())
    lon2 = float(textPunto4.get())

    lat1r = math.radians(lat1) 
    lon1r = math.radians(lon1) 
    lat2r = math.radians(lat2) 
    lon2r = math.radians(lon2) 

    # Formula para calcular la distancia geodésica    
    d = 6371 * math.acos(math.cos(lat1r)*math.cos(lat2r)*math.cos(lon2r-lon1r) +math.sin(lat1r)*math.sin(lat2r))

    a = round(d, 4)
    t = a
    tm = ( 65 + ((3 * t - 10)))
    hr = tm/60
    redontp = round(hr, 4)
    hours_decimal = redontp
    hours, remainder = divmod(hours_decimal, 1)
    minutes = round(remainder * 60)
    time = f'{int(hours):02d}:{int(minutes)}'

    label_1.config(text=f"Distancia : {str(a)}  km")
    label_2.config(text=f"Tiempo : {str(time)}  Horas")

titulo = Label(raiz, text= 'Coordenadas Elipsoidales en Decimal', font=("Arial", 10))
titulo.config(justify="center", anchor="center")
titulo.place(x=80, y=10)  # Colocar en la coordenada (50, 50)

Punto1=Label(fondo, text='Latitud Punto1',font=("Arial", 10))
Punto1.grid(row=2,column=0,sticky='e', padx=5,pady=5)
textPunto1 =Entry(fondo)
textPunto1.config(validate="key", validatecommand=(validacion, '%P'))
textPunto1.grid(row=2,column=1, padx=5,pady=5)

Punto2=Label(fondo, text='Longitud Punto1', font=("Arial", 10))
Punto2.grid(row=3,column=0,sticky='e', padx=5,pady=5)
textPunto2 =Entry(fondo)
textPunto2.config(validate="key", validatecommand=(validacion, '%P'))
textPunto2.grid(row=3,column=1, padx=5,pady=5)

Punto3=Label(fondo, text='Latitud Punto2', font=("Arial", 10))
Punto3.grid(row=4,column=0,sticky='e', padx=5,pady=5)
textPunto3 =Entry(fondo)
textPunto3.config(validate="key", validatecommand=(validacion, '%P'))
textPunto3.grid(row=4,column=1, padx=5,pady=5)

Punto4=Label(fondo, text='Longitud Punto2', font=("Arial", 10))
Punto4.grid(row=5,column=0,sticky='e', padx=5,pady=5)
textPunto4 =Entry(fondo)
textPunto4.config(validate="key", validatecommand=(validacion, '%P'))
textPunto4.grid(row=5,column=1, padx=5,pady=5)

boton_sumar = Button(raiz, text="Calcular", command=DistKm)
boton_sumar.place(x= 100, y= 200)

label_1 = Label(raiz, text="Distancia :", font=("Arial", 10))
label_1.place(x= 180, y= 180)

label_2 = Label(raiz, text="Tiempo :", font=("Arial", 10))
label_2.place(x= 180, y= 210)

label_3 = Label(raiz, text="ing. Sebastian Martinez", font=("Arial", 9))
label_3.place(x= 10, y= 270)

raiz.mainloop()