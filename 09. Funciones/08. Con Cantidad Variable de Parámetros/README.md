## Con Cantidad Variable de Parámetros

Otra variante de las funciones en Python es la **definición de una cantidad variable de parámetros**.

Para definir una cantidad variable de parámetros debemos anteceder el caracter asterísco '*' al **último parámetro** de la función.

Ejemplo: *Definimos tres parámetros en la función, el primero y el segundo reciben enteros y el tercero, una tupla (por ahora, pensemos que una tupla es lo mismo que una lista, más adelante veremos sus diferencias)*:

```python
def sumar(v1, v2, *lista):
    suma = v1 + v2

    for x in range(len(lista)):
        suma = suma + lista[x]

    return suma

print(sumar(1, 2)) # Si enviamos solo dos parámetros la lista está vacía
print(sumar(1, 2, 3, 4)) # Si enviamos 4 parámetros, en este caso la lista tiene dos elementos
print(sumar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) # En general, podemos llamar la función enviando cualquier cantidad de enteros.
```