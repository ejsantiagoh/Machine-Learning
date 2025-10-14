def primos(lista):
    # Filtra números primos de una lista
    resultado = [] # Lista para almacenar los números primos encontrados
    for n in lista:  # Iterar sobre cada número en la lista de entrada
        if n > 1: # Los números primos deben ser mayores que 1
            es_primo = True # Asumimos inicialmente que el número es primo
            # Verificar divisibilidad desde 2 hasta la raíz cuadrada del número
            # Optimización: solo necesitamos verificar hasta sqrt(n)
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:  # Si n es divisible por i
                    es_primo = False # No es primo
                    break # Salir del bucle interno temprano
            if es_primo: # Si mantuvo la condición de primo después de las verificaciones
                resultado.append(n) # Agregar a la lista de resultados
    return resultado # Retornar la lista filtrada con solo primos

print(primos([2,3,4,5,10,11]))  # Output: [2, 3, 5, 11]
