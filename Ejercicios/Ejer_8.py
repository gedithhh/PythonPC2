def calcular_factorial(numero):
    if numero < 0:
        return "Ingrese un entero positivo porfavor"
    
    else:
        resultado_factorial = 1
        for i in range(1, numero + 1):
            resultado_factorial *= i
        return resultado_factorial


numero = int(input("Ingrese un número entero: "))
resultado_final = calcular_factorial(numero)
print(f"El factorial del numero solicitado es {resultado_final}")
