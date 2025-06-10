# Importar Funcionalidades

Si queremos acceder solo a **una única** función del módulo **random**, lo podemos expresar utilizando la palabra clave **from** y el nombre del módulo que deseemos. Luego indicamos la palabra clave **import** y la funcionalidad que queremos importar, en nuestro ejemplo la función `randint()`.
Para utilizar la función, simplemente hacemos referencia a ella directamente.

```python
from random import randint

valor = randint(1,10)
print(valor)
```

Si necesitamos importar más de una funcionalidad de un módulo podemos separar por comas las funcionalidades importadas..:

```python
from random import randint,shuffle
```

...o importarlas una a una:

```python
from random import randint
from random import shuffle
```
