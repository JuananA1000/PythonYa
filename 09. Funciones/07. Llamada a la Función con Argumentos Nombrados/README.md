## Llamada a la Función con Argumentos Nombrados

En Python podemos llamar a la función indicando **en cualquier orden los parámetros de la misma**, pero debemos especificar en la llamada el nombre y el valor del parámetro.

Como podemos ver no hay ningún cambio cuando definimos la función:

```python
def calcular_sueldo(nombre, costo_hora, cantidad_horas):
    sueldo = costo_hora*cantidad_horas
    print(nombre, "trabajo", cantidad_horas, "y cobra un sueldo de", sueldo)

calcular_sueldo("juan",10,120)
```

Pero también podemos indicar los datos **en cualquier orden pero poniendo antes el nombre del parámetro**:

```python
calcular_sueldo(costo_hora=12, cantidad_horas=40, nombre="ana")
calcular_sueldo(cantidad_horas=90, nombre="luis", costo_hora=7)
```

Ahora vamos a profundizar la función `print()` que hemos utilizado desde los primeros conceptos.

Como hemos trabajado hasta ahora, cuando llamamos a la función `print()` se muestran todos los datos que le enviamos separados por coma y provoca un salto de línea al final.

Por ejemplo si ejecutamos:

```python
print("uno") # Imprime "uno"
print("dos") # Imprime "dos"
```

Para evitar ese saollto de línea, La función `print()` tiene un parámetro llamado `end=`, que **suprime ese salto de línea**. También podemos indicar al parámetro `end=` otro valor, por ejemplo un guión:

```python
print("uno", end="-")
print("dos") # Este código imprime: uno-dos
```
