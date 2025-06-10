# Método __init__ de la clase

El objetivo fundamental del método `__init__` es **inicializar** los atributos del objeto que creamos.

Básicamente el método `__init__` remplaza al método `inicializar()` del apartado anterior, lo cual tiene ciertas **ventajas**:

- Es el **primer método** que se ejecuta cuando se crea un objeto.
- Se llama automáticamente, por lo que es imposible que nos olvidemos de llamarlo.

Otras características del método `__init__` son:

- Se ejecuta inmediatamente luego de crear un objeto.
- No puede retornar datos.
- Puede recibir parámetros que se utilizan normalmente para inicializar atributos.
- Es un método opcional, de todos modos es muy común declararlo.

Veamos la sintaxis del constructor:

```python
def __init__([parámetros]):
    [algoritmo]
```