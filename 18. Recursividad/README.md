# 21. Recursividad
La recursividad es una técnica de programación que nos permite que un bloque de instrucciones se ejecute repetidas veces. Reemplaza en ocasiones a estructuras repetitivas.

En Python las funciones pueden llamarse a sí mismas. Si dentro de una función existe la llamada a sí misma decimos que es **recursiva**.

Cuando una función se llama a sí misma, se asigna espacio en la pila para las nuevas variables locales y parámetros.

Al volver de una llamada recursiva, se recuperan de la pila las variables locales y los parámetros antiguos y la ejecución se reanuda en el punto de la llamada al método.