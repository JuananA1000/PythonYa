
## 5.1 Estructura Repetitiva *WHILE*.

Esta estructura, repite el código contenido en ella **mientras** la condición sea verdadera.

> [!IMPORTANT]  
> Si la condición es siempre verdadera estamos en presencia de un **bucle infinito**. Dicha situación suele ser un **error**, ya que nunca finalizará el programa.

![Bucle While](https://github.com/JuananA1000/PythonYa/blob/main/05.%20Estructuras%20Repetitivas/01.%20Bucle%20WHILE/while.jpg?raw=true)

```mermaid
flowchart TD
    A([Inicio]) --> B{¿Se cumple la condición?}
    B -->|Verdadero| C[Ejecutar operaciones]
    C --> B
    B -->|Falso| D([Fin])
```

El código esquemático para el bucle while, sería el siguiente:

```python
while condition:
```