### Layout Manager (Administrador de Diseño)

Una de las herramientas fundamentales cuando armamos interfaces visuales es la metodología para colocar controles dentro de ellas. Hasta ahora hemos utilizado el administrador de diseño Grid.

En la librería GUI tkinter tenemos de tres Layout Manager para colocar controles en una ventana:

- Grid
- Pack
- Place

Solo se puede utilizar **uno** de estos Layout Manager dentro de un contenedor, recordemos que un contenedor puede ser la propie ventana, un Frame o un LabelFrame.

El gestor de diseño más completo y que se adapta en la mayoría de las situaciones es el Grid, pero, en muchos casos, podemos crear Frame o LabelFrame y definir dentro de estos Layout Manager de tipo Pack o Place.