import random

print('Welcome to Python!')

print('This is a loop printing 5 times')
for x in range(1, 6):
    print(f'x is: {x}')

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
day = random.choice(weekdays)

print(f'Today is: {day}')

if day == 'Monday':
    print('It will be a long week!')
elif(day == 'Friday'):
    print('Woohoo, time for the weekend!')
else:
    print('Not quite there yet.')

# imprime el tipo de numero
print(type(24))
print(type(3.9))
print(type(3j))

# proporciona un número aleatorio entre 2 y 5
import random
print(random.randint(2,5)) 

#cadenas
name = "Zen"
lastname= "Alyper"
print("Mi nombre es", name, "y mi apellido es", lastname)


#importante al momento de trabajar con numeros en operaciones aritmeticas
total = 35
user_val = 26
total = total + user_val		# salida: TypeError
print(total)
total = total + int(user_val)		# el total será 61
print(total)

#concatenar texto y numeros por el metodo f (Interpolación de cadenas literal)
first_name = "Zen"
last_name = "Coder"
age = 27
print(f"Mi nombre is {first_name} {last_name} and tengo {age} años de edad.")

#algunos metodos de cadena

edad=17
if(edad>18):
    cadena = 'Mayor de edad'
else:
    cadena="Menor de edad"
print("El alumno es ", cadena) #pasamos la cadena a mayuscula


#crea una lista e imprime el largo de esa lista
mi_lista = [1, 'Zen', 'hola']
lista2=['hola','como','estas']

mi_lista.extend(lista2)
print(mi_lista)
mi_lista.index('como')

#ejemplo tuplas
perro = ("Canis Familiaris", "perro", "carnívoro", 12)
print(perro[2])
perro[1]="gato"#arroja error ya que no podemos modificar una tupla (principal diferencia con una lista)
perro = perro + ("doméstico",)#agregamos un valor a la tupla
print(perro)
perro = perro[:3] + ("el mejor amigo del hombre",) + perro[4:]
print(perro)