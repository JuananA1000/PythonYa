## 17.1 Creación, Escritura y Lectura

Como es una actividad tan común en todo programa el lenguaje Python incluye por defecto todas las funcionalidades para trabajar con archivos de texto.

Veamos con un ejemplo como crear y almacenar caracteres en un archivo de texto.

### Crear y escribir. Método `open()`

Usamos `open()` para abrir un archivo. El modo `"w"` lo crea si no existe y sobrescribe su contenido si ya existe. El método `open()` incluirá:

1. el nombre del archivo a crear
2. un string con el caracter "w" (de escritura, _write_):

```python
archivo = open("nombre_archivo.txt","w")
```

Ejemplo de código:

```python
archivo = open("archivo.txt", "w", encoding="utf-8")
archivo.write("Hola, mundo! \n")
archivo.write("Segunda línea")
archi1.close()
```

- `"w"`: **write**. Escribir, sobrescribiendo el contenido.
- `"a"`: **amend**. Añadir contenido al final.
- `encoding="utf-8"`: permite utilizar tildes y caracteres especiales.

---

### Leer. Método `read()`

El modo `"r"` permite leer el contenido de un archivo existente.

```python
archivo = open("archivo.txt", "w", encoding="utf-8")
contenido = archivo.read()
print(contenido)
```

Otros métodos de lectura. Métodos `readline()` y `readlines()`:

```python
archivo.readline()  # Lee una línea.
archivo.readlines() # Devuelve una lista de líneas.
```

### Leer línea por línea

Podemos recorrer el archivo con un bucle `for`:

```python
archivo = open("archivo.txt", "r", encoding="utf-8"):
for linea in archivo:
    print(linea.strip())
```

`strip()` elimina espacios y saltos de línea al principio y al final.

**Nota:** Si el archivo está en otra carpeta, indica su ruta en `open()`.
