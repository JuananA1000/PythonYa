## Operadores Relacionales con Objetos

Los métodos especiales que podemos implementar para redefinir los operadores relacionales cuando planteamos una clase son los siguientes:

Para el operador ==:

```python
__eq__(self,objeto2)
```

Para el operador !=:

```python
__ne__(self,objeto2)
```

Para el operador >:

```python
__gt__(self,objeto2)
```

Para el operador >=:

```python
__ge__(self,objeto2)
```

Para el operador <:

```python
__lt__(self,objeto2)
```

Para el operador <=:

```python
__le__(self,objeto2)
```

Debemos recordar que una redefinición de un operador tiene sentido si ayuda y hace más claro nuestro algoritmo.