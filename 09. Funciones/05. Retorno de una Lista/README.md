## Retorno de una Lista

Una función puede recibir como parámetros tipos de datos simples como **enteros**, **flotantes** y **listas**.

También hemos visto que la función puede retornar este tipo de datos.

Ahora veremos que una función también puede **retornar una estructura de datos tipo lista**. Con esto logramos que una función retorne varios datos.

Ejemplo: *Función que genera y retorna una lista de números pares hasta un límite dado*:

```
def generar_lista_pares(lim):
    lista_pares = []
    for i in range(0, lim):
        if i % 2 == 0:
            lista_pares.append(i)
    return lista_pares

# Ejemplo de uso
limite = 11
lista_pares = generar_lista_pares(limite)
print(lista_pares) # Imprime: [0, 2, 4, 6, 8, 10]
```