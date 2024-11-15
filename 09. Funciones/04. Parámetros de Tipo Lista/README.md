## Parámetros de Tipo Lista

Trabajando con **programación estructurada**, dividimos nuestro problema por partes implementando **funciones**. La comunicación entre funciones se produce mediante el envío de datos a través de **parámetros** y el valor que retorna la función.

Hasta ahora hemos resuelto problemas enviando datos simples como **enteros**, **floats** y **cadenas de caracteres**. 

Ahora veremos que una función puede recibir también **estructuras de datos** como parámetro.

Ejemplo: *Ordena una lista de enteros de menor a mayor:*
```python
def ordenar_lista(lista):
    return sorted(lista)

# Ejemplo de uso
mi_lista = [5, 3, 8, 1, 2]
lista_ordenada = ordenar_lista(mi_lista)

print('Lista de menor a mayor: ', lista_ordenada)
```

