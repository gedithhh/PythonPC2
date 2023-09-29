
lista_numeros= []
cant_par=0
cant_impar=0

while True:
    respuesta= input("Desea ingresar un numero? Escribir SI/NO : ")

    if respuesta=='SI':
        num=float(input("Ingrese el numero: "))
        lista_numeros.append(num)

        if num%2==0:
            cant_par += 1
        else:
            cant_impar += 1
    elif respuesta=='NO':
        break
    else: 
        print("Su respuesta no es valida, responda con 'SI' o 'NO'.")
print(f"Números ingresados: {lista_numeros}")
print(f"Cantidad de números pares: {cant_par}")
print(f"Cantidad de números impares: {cant_impar}")
    