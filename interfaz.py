import tkinter as tk
root = tk.Tk()
sw = False
num1 = tk.StringVar()
num2 = tk.StringVar()
mensaje = tk.StringVar()
def suma():
    n1 = int(num1.get())
    n2 = int(num2.get())
    s = n1 + n2
    num1.set('')
    num2.set('')
    mensaje.set(f"La suma es {s}")
    print(f"La suma es {s}")

def resta():
    n1 = int(num1.get())
    n2 = int(num2.get())
    r = n1 - n2
    num1.set('')
    num2.set('')
    mensaje.set(f"La resta es {r}")
    print(f"La resta es {r}")

def multiplicacion():
    n1 = int(num1.get())
    n2 = int(num2.get())
    p = n1 * n2
    num1.set('')
    num2.set('')
    mensaje.set(f"La multiplicación es {p}")
    print(f"La multiplicación es {p}")

def division():
    n1 = int(num1.get())
    n2 = int(num2.get())
    d = n1 / n2
    num1.set('')
    num2.set('')
    mensaje.set(f"La división es {d}")
    print(f"La división es {d}")

def cerrar_programa():
    print("Seleccionó salir de la aplicación. Hasta la próxima")
    global sw
    sw = False
root. geometry('600x400')
root.title('Proyecto final')
root.configure(bg="#455A64")
tk.Label(root,text='CALCULADORA',bg='#455A64',fg='white',font=('',30)).place(x=150,y=30)

#Texto y campo de texto
tk.Label(root, text='Ingrese primer número:', bg="#455A64", fg='white', font=('', 18)).place(x=30, y=140)
tk.Entry(root, justify='center',textvariable=num1).place(x=320, y=150)
tk.Label(root, text='Ingrese segundo número:', bg="#455A64", fg='white', font=('', 18)).place(x=30, y=190)
tk.Entry(root, justify='center',textvariable=num2).place(x=320, y=200)
tk.Button(root, text="Sumar", bd=0,command=suma).place(x=468, y=150)
tk.Button(root, text="Restar", bd=0,command=resta).place(x=530, y=150)
tk.Button(root, text="Multiplicar", bd=0,command=multiplicacion).place(x=455, y=200)
tk.Button(root, text="Dividir", bd=0,command=division).place(x=530, y=200)
tk.Label(root, textvariable=mensaje, bg='#455A64', fg='white', font=('', 20)).place(x=30, y=300)
tk.Button(root,text="SALIR", bd=0,command=root.destroy).place(x=300, y=360)


root.mainloop()