'''
  Definir dos conjuntos que almacenen cada uno una serie de lenguajes de programación. Efectuar las cuatro operaciones 
  básicas con dichos conjuntos.
'''

leng_1 = {"C", "Pascal", "PHP", "Python"}
leng_2 = {"C++", "Java", "Python"}

print(f"Unión: {leng_1 | leng_2}")
print(f"Intersección: {leng_1 & leng_2}")
print(f"Diferencia: {leng_1 - leng_2}")
print(f"Diferencia simétrica: {leng_1 ^ leng_2}")
