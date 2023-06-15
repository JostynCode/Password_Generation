import random
import tkinter as tk
from tkinter import Label, Button, Entry

#Here are the list where the functions will be getting the parts of the password
letras = ["a", "b", "c", "d","e","f", "g","h","i","j","k","m","n","l","o","p","q","r","s","t","u","v","w","x","y","z","A","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
numeros = ["1","2","3","4","5","6","7","8","9"]
signos = ["!","#","$","%","&","/","(",")","=","?","¡","*","+","-",":",";","."]

#This the function that will be getting the password
def generacion():
    empty = ['']
    passwd_letras = random.sample(letras, 4)
    passwd_num = random.sample(numeros, 4)
    passwd_signos = random.sample(signos, 2)

    empty.extend(passwd_letras)
    empty.extend(passwd_num)
    empty.extend(passwd_signos)

    password_final = ''.join(empty)

    Resultado.delete(0,'end')
    Resultado.insert(0 ,password_final)
    

#This is the part of the windows
ventana = tk.Tk()
ventana.title("Ventana_suma")
ventana.geometry("400x200")


lbl1 = Label(ventana, text="Generador de contraseña", fg="black", bg="yellow")
lbl1.place(x="100", y="10", width="200", height="30")

btn1 = Button(ventana, text="Generar contraseña" ,fg= "white", bg="black" ,command= generacion)
btn1.place(x="100", y="50", width="200", height="40")

Resultado = Entry(ventana, fg="black", bg="pink")
Resultado.place(x="130", y="140", width="150", height="35")

ventana.mainloop()