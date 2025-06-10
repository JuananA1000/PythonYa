
# Programación Orientada a Objetos (POO)

Python permite utilizar distintas metodologías de programación. Hemos implementado inicialmente **programación lineal**, luego vimos **funciones** y trabajamos con **programación estructurada**.

Ahora introduciremos los conceptos de **Programación Orientada a Objetos (POO)**. A partir de este concepto mostraremos en forma sencilla la metodología de POO.

Se irán introduciendo conceptos de **objeto**, **clase**, **atributo**, **método** etc.

Prácticamente todos los lenguajes desarrollados en los últimos 25 años implementan la posibilidad de trabajar con POO 

## Conceptos básicos de Objetos

Un **objeto** es una entidad independiente con datos propios. Por ejemplo, las ventanas, menús, carpetas de archivos pueden ser identificados como objetos; un coche también es considerado un objeto, en este caso, sus datos (atributos) describen sus características físicas y sus métodos, el funcionamiento interno.

A la suma de funciones a elementos de datos se le llama **encapsulamiento**.
Por ejemplo, un objeto Coche contiene ruedas, motor, velocidad, color, etc, llamados **atributos**. Encapsulados con estos datos se encuentran los **métodos** para arrancar, detenerse, girar, frenar etc.

Cuando otros objetos del programa necesitan que el coche realice alguna de las tareas le envía un mensaje. A estos objetos que envían mensajes no les interesa la manera en que el objeto auto lleva a cabo sus tareas ni las estructuras de datos que maneja, por ello, están ocultos.

Un objeto contiene información de dos tipos:
- **Pública**, lo que necesitan los otros objetos para interactuar con él.
- **Privada**, lo que necesita el objeto para operar por sí mismo y que es irrelevante para los otros objetos de la aplicación.
