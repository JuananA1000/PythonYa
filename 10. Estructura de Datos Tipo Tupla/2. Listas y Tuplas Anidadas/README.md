## Listas y Tuplas Anidadas

Hemos visto dos estructuras de datos fundamentales en Python que son las **listas** y las **tuplas**. Las listas son estructuras **mutables**, en cambio, las tuplas son **inmutables**, es decir una vez definida no puede cambiar.

Dentro de una lista podemos definir datos de tipo lista, hablamos asi de **listas anidadas**.

En este caso, también podemos **anidar tuplas**.

En general podemos crear y combinar **tuplas con listas**...:
```
alumno = ('Pedro', [7, 9])
print(alumno)

alumno[1].append(10)
print(alumno)  # Imprime: ('Pedro', [7, 9, 10])
```

...y viceversa, es decir, **listas con tuplas**:
```
empleado = ['Juan', 53, (25, 11, 1999)]
print(empleado)

empleado.append((1, 1, 2016))
print(empleado)  # Imprime: ['Juan', 53, (25, 11, 1999), (1, 1, 2016)]
```

En cualquiera de los casos, como vemos, se pueden anidar con el método `.append()`.
