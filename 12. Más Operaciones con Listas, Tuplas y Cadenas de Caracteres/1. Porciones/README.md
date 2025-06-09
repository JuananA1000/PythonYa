## Porciones

Python tiene una sintaxis muy sencilla para recuperar una **parte** de una lista, tupla o cadena de caracteres.

Ejemplos:
```python
lista1 = [0,1,2,3,4,5,6]
lista2 = lista1[2:5]
print(lista2) # 2,3,4

lista3 = lista1[1:3]
print(lista3) # 1,2

lista4 = lista1[:3]
print(lista4) # 0,1,2

lista5 = lista1[2:]
print(lista5) # 2,3,4,5,6
```

Para recuperar una parte de una lista indicaremos en el subíndice dos valores separados por el caracter ":".

Del lado izquierdo indicamos la primera posición a partir de la cual recuperar y del lado derecho hasta qué posición **sin incluir dicho valor**.

Por ejemplo con la sintaxis:

```python
lista1 = [0,1,2,3,4,5,6]
lista2 = lista1[2:5]
print(lista2) # 2,3,4
```

Estamos recuperando de la posición 2 hasta la 5 sin incluirla.

Si no indicamos el primer valor recuperaremos valores **desde el principio** de la lista **hasta la posición n-1** indicada después de los dos puntos.

```python
lista1 = [0,1,2,3,4,5,6]
lista4 = lista1[:3]
print(lista4) # 0,1,2
```

En cambio si no indicamos el valor después de los dos puntos, recuperaremos **hasta el final de la lista**:

```python
lista5 = lista1[2:]
print(lista5) # 2,3,4,5,6
```
