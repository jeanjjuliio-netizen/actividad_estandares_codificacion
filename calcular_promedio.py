"""
Script para calcular el promedio de calificaciones de un estudiante.

Este programa pide al usuario que ingrese varias calificaciones
y luego calcula y muestra el promedio.
"""
Los nombres de variables y funciones son claros y descriptivos --- Cumple
Hay una docstring o comentario inicial que explica el propósito --- Cumple                       
Los comentarios son utiles (no redundantes ni excesivos) --- Cumple  
La sangría y el espaciado son consistentes --- Cumple  
El código está bien estructurado (bloques lógicos, sin líneas inútiles) --- Cumple                
Se aplica la guía de estilo acordada  --- Cumple  

Bien Jean Cumpliste" 
ATT Carlos Velasquez 


def calcular_promedio(lista_calificaciones):
    """
    Calcula el promedio de una lista de calificaciones.
    
    Parámetros:
        lista_calificaciones: lista con las calificaciones (números)
    
    Retorna:
        El promedio calculado (float)
    """
    if len(lista_calificaciones) == 0:
        return 0
    
    suma = 0
    for nota in lista_calificaciones:
        suma += nota
    
    promedio = suma / len(lista_calificaciones)
    return promedio


def obtener_calificaciones():
    """
    Pide al usuario que ingrese las calificaciones.
    
    Retorna:
        Una lista con todas las calificaciones ingresadas
    """
    calificaciones = []
    
    print("Ingresa las calificaciones del estudiante")
    print("(escribe 'fin' cuando termines)\n")
    
    while True:
        entrada = input("Calificación: ")
        
        # Si el usuario escribe fin, salimos del ciclo
        if entrada.lower() == 'fin':
            break
        
        try:
            # Intentar convertir la entrada a número
            nota = float(entrada)
            
            # Verificar que la nota esté en rango válido
            if nota >= 0 and nota <= 10:
                calificaciones.append(nota)
            else:
                print("Por favor ingresa una nota entre 0 y 10")
        
        except:
            print("Eso no es un número válido, intenta de nuevo")
    
    return calificaciones


# Programa principal
print("=" * 50)
print("CALCULADORA DE PROMEDIO DE CALIFICACIONES")
print("=" * 50)
print()

# Obtener las calificaciones del usuario
notas = obtener_calificaciones()

# Verificar que se ingresaron calificaciones
if len(notas) > 0:
    print(f"\nCalificaciones ingresadas: {notas}")
    
    # Calcular el promedio
    resultado = calcular_promedio(notas)
    
    # Mostrar el resultado
    print(f"Promedio final: {resultado:.2f}")
    
    # Mensaje adicional según el promedio
    if resultado >= 7:
        print("¡Buen trabajo!")
    elif resultado >= 5:
        print("Aprobado, pero hay que mejorar")
    else:
        print("Necesitas estudiar más")
else:
    print("\nNo ingresaste ninguna calificación")

print("\n¡Gracias por usar el programa!")
