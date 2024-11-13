## Eliminación de Elementos

Hemos visto que podemos iniciar listas por asignación con elementos.

```python
lista = [10, 20, 30, 40]
```

Podemos agregar elementos **al final** mediante el método `.append()`:

```python
lista = [10, 20, 30, 40]
lista.append(120) # Resultado al imprimir: [10, 20, 30, 40, 120]
```

Y, por supuesto, podremos eliminar cualquiera de sus componentes llamando al método `.pop()` e indicando la posición del elemento a borrar:

```python
lista.pop(0) # Resultado al imprimir: [20, 30, 40, 120]
```

Cuando un elemento de la lista se elimina no queda una posición vacía, sino que **se desplazan todos los elementos de la derecha una posición**.

El método `.pop()` retorna el valor almacenado en la lista en la posición indicada, aparte de borrarlo.

```python
lista = [10, 20, 30, 40]
print(lista.pop(0)) # imprime un 10
```




