lista1 = ['Madrid', 'Oaxaca', 'Berlin', 'Oslo', 'Toronto']
print (lista1) 

print (lista1[1])

print (lista1[1:4])

print (type(lista1))

print (lista1[2:])

print (lista1[:4])

lista1.append('Roma')
print(lista1)

lista1.append('Toronto')
print(lista1)

lista1.insert(3,'Amsterdam')
print(lista1)

lista1.extend(['Bruselas','Paris'])
print(lista1)

print(lista1.index('Toronto'))

#print(lista.index('Barcelona'))

lista1.remove('Madrid')
print(lista1)
#lista1.remove('Barcelona')
#print(lista1)
ultimo = lista1.pop()
print(ultimo)
print(lista1*4)

tuple1 = tuple (range (1,21))
print (tuple1)

print (tuple1[9:15])

print (20 in tuple1)
print (30 in tuple1)

print ('Paris'in lista1)
print (lista1.count('Paris'))
print (tuple1.count(10))
milista2 = list(tuple1)
print(milista2)
tuple2 = tuple (range (1,21))

primero,segundo, tercero = tuple2 [:3]
print("Primero", primero, "segundo", segundo, 'Tercero', tercero)

mi_diccionario = {  'ciudad' : [lista1],
                    'numeros': [milista2]}
print(mi_diccionario ['ciudad'])
print(mi_diccionario.keys())