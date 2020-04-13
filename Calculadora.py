def suma(n1,n2):
    s = n1 + n2
    print(f"La suma es {s}")

def resta(n1,n2):
    r = n1 - n2
    print(f"La resta es {r}")

def multiplicacion(n1,n2):
    p = n1 * n2
    print(f"La multiplicacion es {p}")

def division(n1,n2):
    d = n1 / n2
    print(f"La division es {d}")

def cerrar_programa():
    print("Seleccionó salir de la aplicación. Hasta la próxima")
    global sw
    sw = False


sw = True
print("***--- PROYECTO ---***")
lista="""
-*** CALCULADORA ***-
1. SUMAR
2. RESTAR
3. MULTIPLICAR
4. DIVIDIR
5. SALIR
"""
while(sw):
    print(lista)
    dato = int(input("Ingrese opción a realizar (1-5):"))
    if dato == 1:
        print("Seleccionó operación suma")
        n1 = int(input("Ingrese primer número:"))
        n2 = int(input("Ingrese segundo número:"))
        suma(n1,n2)
    elif dato == 2:
        print("Seleccionó operación resta")
        n1 = int(input("Ingrese primer número:"))
        n2 = int(input("Ingrese segundo número:"))
        resta(n1,n2)
    elif dato == 3:
        print("Seleccionó operación multiplicación")
        n1 = int(input("Ingrese primer número:"))
        n2 = int(input("Ingrese segundo número:"))
        multiplicacion(n1,n2)
    elif dato == 4 :
        print("Seleccionó operación división")
        n1 = int(input("Ingrese primer número:"))
        n2 = int(input("Ingrese segundo número:"))
        division(n1,n2)
    elif dato == 5 :
        cerrar_programa()
    else:
        print("No existe la opción ingresada")