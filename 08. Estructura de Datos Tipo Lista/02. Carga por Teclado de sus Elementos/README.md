## Carga por Teclado de sus Elementos

Las listas en Python son estructuras **mutables** porque **pueden cambiar durante la ejecución del programa**.

Podemos definir listas **por asignación** indicando entre corchetes sus valores:

```
lista = [10, 20, 40]
```

Una vez definida, podremos **agregarle más elementos** mediante el método `append()` :

```
lista = [10, 20, 30]
print(len(lista))    # imprime un 3
lista.append(100)
print(len(lista))    # imprime un 4

print(lista)         # imprime [10, 20, 30, 100]
```

