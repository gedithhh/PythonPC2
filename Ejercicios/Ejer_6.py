def serie_Fibonacci(final):
    resultado_serie=[]
    num_antes=0
    num_desp=1
    while num_antes<=final:
        resultado_serie.append(num_antes)
        
        num_antes, num_desp = num_desp, num_antes + num_desp
        
    return resultado_serie

fibonacci_final= serie_Fibonacci(50)
print(f"Fibonacci entre 0 y 50: {fibonacci_final}")

