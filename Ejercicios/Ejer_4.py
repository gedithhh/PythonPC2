lista_alumnos=[]

n = int(input("Ingrese la cantidad de alumnos a registrar: "))

for i in range(n):
    nombre = input(f"\nIngrese el nombre del alumno {i+1}: ")
    nota1 = float(input("Ingrese la calificación de la primera materia: "))
    nota2 = float(input("Ingrese la calificación de la segunda materia: "))
    nota3 = float(input("Ingrese la calificación de la tercera materia: "))
    
    alumno = {
        "Alumno": nombre,
        "Notas": [nota1, nota2, nota3]
    }
    
    lista_alumnos.append(alumno)

print("\nEste es el listado completo de alumnos:")
for alumno in lista_alumnos:
    print(f"\nAlumno: {alumno['Alumno']}")
    print(f"Notas: {alumno['Notas']}")
    print("\n")






