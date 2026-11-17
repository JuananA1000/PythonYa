# 19. Otras Funciones en Python

Existen **dos tipos más** de funciones importantes para comprender la programación funcional en Python.
Las **Funciones de Orden Superior** permiten trabajar con otras funciones como si fueran datos, mientras que las **Funciones Lambda** permiten crear pequeñas funciones anónimas de rápidamente.

## Diferencias entre funciones tradicionales y Lambda

| Característica |              `def`              |      `lambda`       |
|----------------|---------------------------------|---------------------|
| Nombre         | Suelen tener nombre             | Son anónimas        |
| Sintaxis       | Varias instrucciones            | Una expresión       |
| `return`       | Necesario para devolver valores | Implícito           |
| Complejidad    | Permite operaciones complejas   | Operaciones simples |
| Reutilización  | Ideal para reutilizar código    | Para usos puntuales |

## ¿Cuándo utilizar cada una?

**FOS:**
- Cuando necesitamos pasar funciones como argumentos.
- Cuando queremos transformar o filtrar colecciones.
- Cuando buscamos reutilizar operaciones de forma flexible.

**FL:**
- Cuando necesitamos una función pequeña y sencilla.
- Cuando utilizamos `map()`, `filter()` o `sorted()`.
- Cuando queremos evitar declarar funciones que solo se utilizarán una vez.

> [!WARNING]  No conviene utilizar lambda para operaciones complejas. En esos casos, es preferible utilizar `def`, ya que facilita la lectura, el mantenimiento y la depuración del código.