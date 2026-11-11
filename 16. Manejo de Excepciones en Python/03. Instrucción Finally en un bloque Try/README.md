## 19.3 Instrucción `finally` en un Bloque `try`

Hemos visto que la sintaxis para la captura de excepciones es:

```python
try:
    [algoritmo principal]
except [nombre de la excepción 1]:
    [algoritmo alternativo 1]
except [nombre de la excepción 2]:
    [algoritmo alternativo 2]
    ...
```

Hay otra sección opcional de la cláusula `try` llamada `finally`:

```python
try:
    [algoritmo principal]
except [nombre de la excepción 1]:
    [algoritmo alternativo 1]
except [nombre de la excepción 2]:
    [algoritmo alternativo 2]
    ...
finally:
    [algoritmo que siempre se ejecuta]
```

Cuando en el algoritmo principal se genera una excepción las instrucciones que continúan nunca se ejecutarán ya que pasa a ejecutar el bloque del `except`. Hay situaciones donde queremos que haya un algoritmo que siempre se ejecute ya sea que se dispare una excepción o no.

Veamos algunos ejemplos donde es conveniente emplear el bloque `finally`.