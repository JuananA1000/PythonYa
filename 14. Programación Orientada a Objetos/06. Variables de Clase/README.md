## Variables de Clase

En ocasiones, necesitamos almacenar datos comunes a todos los objetos de dicha clase, en esas situaciones debemos emplear **variables de clase**.
Para definir una variable de clase lo haremos **dentro de la clase** pero **fuera de sus métodos**:

```python
class Persona:
    variable = 20 # variable de clase
    
    def __init__(self, nombre):
        self.nombre = nombre

persona1=Persona("Juan")
persona2=Persona("Ana")
persona3=Persona("Luis")

print(persona1.nombre) # Juan
print(persona2.nombre) # Ana
print(persona3.nombre) # Luis

print(persona1.variable) # 20
Persona.variable = 5
print(persona2.variable) # 5
```

La variable "variable" del código anterior será compartida por todos los objetos persona1, persona2 y persona3.
Para modificar el valor de la variable de clase hacemos referencia al nombre de la clase y seguidamente el nombre de la variable:

```python
Persona.variable = 5
```
