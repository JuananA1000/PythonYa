## 18.1 Introducción

Toda función recursiva necesita dos elementos:

- **Caso base:** condición que detiene las llamadas recursivas.
- **Caso recursivo:** parte en la que la función vuelve a llamarse a sí misma.

*Ejemplo de código 1: cuenta atrás*
```python
def cuenta_atras(numero):
    if numero == 0:  # Caso base
        print("¡Despegue!")
    else:  # Caso recursivo
        print(numero)
        cuenta_atras(numero - 1)

cuenta_atras(5)
```

*Resultado:*

```text
5
4
3
2
1
¡Despegue!
```

*Ejemplo de código 2: factorial de un número*

El factorial de un número entero positivo es el producto de todos los números enteros desde 1 hasta ese número.

Por ejemplo: 5! = 5 × 4 × 3 × 2 × 1 = 120.

```python
def factorial(numero):
    if numero == 0:  # Caso base
        return 1
    else:
        return numero * factorial(numero - 1)

print(factorial(5))  # 120
```

> [!IMPORTANT]  
> Toda función recursiva debe tener un caso base.
> Sin un caso base adecuado, se producirán llamadas infinitas hasta alcanzar `RecursionError`.
> Cada llamada genera un nuevo contexto de ejecución en la pila de llamadas (_call stack_).
> La recursividad puede simplificar problemas complejos, aunque no siempre es la solución más eficiente.
> En Python existe un límite de profundidad de recursividad que se puede consultar mediante `sys.getrecursionlimit()`.

> [!TIP]  
> Utiliza la recursividad cuando un problema pueda dividirse naturalmente en subproblemas más pequeños, como recorridos de árboles, factoriales o algoritmos de búsqueda.
