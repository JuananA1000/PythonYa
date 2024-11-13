
# Procesar cadenas de caracteres

Ya hemos visto que podemos cargar cadena de caracteres por asignación:

```python
cadena1 = "juan" # Con comillas dobles
cadena2 = 'ana' # Con comillas simples
```

O cargarla por teclado:

```python
nombre = input("Ingrese su nombre: ")
```

Ahora explicaremos cómo usar operadores relacionales para identificar si dos cadenas son iguales, distintas o la que tiene una mayor posición alfabéticamente:

|  Signo  |     Significado     |
|:-------:|:-------------------:|
|    ==   |      Igualdad       |
|    !=   |     Desigualdad     |
|    <    |      Menor que      |
|    >    |      Mayor que      |
|    <=   |  Menor o igual que  |
|    >=   |  Mayor o igual que  |

Podremos acceder en forma individual a cada caracter del string mediante un subíndice:

```python
nombre = 'juan'
print(nombre[0]) # se imprime una j

if nombre[0] == "j": # si el primer caracter es una 'j'...
    print(nombre, " comienza con la letra j")
```

Los subíndices se numeran a partir de **cero**.

|  j  |  u  |  a  |  n  |
|:---:|:---:|:---:|:---:|
|  0  |  1  |  2  |  3  |

Para saber la longitud de un string en Python usaremos la función `len()` que retorna la cantidad de caracteres que contiene:

```python
nombre = 'juan'
print(len(nombre)) # imprime un 4
```