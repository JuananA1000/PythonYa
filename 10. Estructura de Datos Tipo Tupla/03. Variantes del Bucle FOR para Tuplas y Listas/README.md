## Variantes del Bucle FOR para Tuplas y Listas

Hasta ahora, siempre recorríamos listas o tuplas con un `for` procedíamos así:
```
lista = [2, 3, 50, 7, 9]

for i in range(len(lista)):
    print(lista[i])
```

Esta forma de recorrer listas se utiliza **obligatoriamente para modificar sus elementos**:
```
lista=[2, 3, 50, 7, 9]

print(lista) # [2, 3, 50, 7, 9]

for i in range(len(lista)):
    if lista[i] < 10:
        lista[i] = 0

print(lista) # [0, 0, 50, 0, 0]
```

Existe una **segunda forma** de recorrer listas con el bucle `for` **sin subíndices**.
```
lista=[2, 3, 50, 7, 9]

for elemento in lista:
    print(elemento)
```

Como vemos, la instrucción `for` requiere una variable (_elemento_, en este caso), luego la palabra clave `in` y por último el **nombre de la lista**. El bucle `for` se ejecutará tantas veces como elementos tenga la lista, _5, en este caso_.
