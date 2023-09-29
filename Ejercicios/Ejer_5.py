def contar_num(numero, digito):

    numero_str= str(numero)

    cantidad= numero_str.count(str(digito))

    return cantidad

numero=int(input("Ingrese su numero entero: "))
digito=int(input("Ingrese el digito a buscar: "))

pedido= contar_num(numero, digito)

print(f"""Numero ingresado: {numero}
Digito: {digito}
La cantidad de veces {digito} en el numero {numero} es: {pedido}""")