## 4.1 Condicionales Simples y Compuestos

Los condicionales simples y compuestos, permiten **tomar decisiones** en función de si una condición es verdadera o falsa.

## Estructura Condicional Simple

En este tipo de estructuras tenemos la opción de **realizar una actividad** o **no realizar ninguna**.

```mermaid
flowchart TD
    Inicio([ ]) --> Condicion{"Condición"}
    Condicion -->|Verdadero| Operaciones["Operaciones"]
    Condicion -->|Falso| Fin([ ])
    Operaciones --> Fin([ ])
```

![Estructura Condicional Simple](https://github.com/JuananA1000/PythonYa/blob/main/04.%20Estructuras%20Condicionales/01.%20Condicionales%20Simples%20y%20Compuestos/ECS.jpg?raw=true)

El esquema básico de este tipo de estructuras es el siguiente:
```python
if condition:
    # code
```

## Estructura Condicional Compuesta.

En este otro tipo de estructuras tenemos la tenemos la opción de **realizar una actividad u otra**. Es decir tenemos actividades por el verdadero y por el falso de la condición. En este caso, **nunca** se realizan las actividades de las dos ramas.

```mermaid
flowchart TD
    Inicio([ ]) --> Condicion{"(Condición)"}
    Condicion -->|Falso| Op2["Operación 2"]
    Condicion -->|Verdadero| Op1["Operación 1"]
    Op2 --> Fin([ ])
    Op1 --> Fin([ ])
```

![Estructura Condicional Compuesta](https://github.com/JuananA1000/PythonYa/blob/main/04.%20Estructuras%20Condicionales/01.%20Condicionales%20Simples%20y%20Compuestos/ECC.jpg?raw=true)

El esquema básico de este tipo de estructuras sería el siguiente:
```python
if condition:
    # code
else:
    # code
```
