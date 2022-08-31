from email.policy import default
import random

#este archivo servira como registro en el aprendisaje Python
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

#diccionario
context = {

1 : {'¿Por que hay luz en el refrigerador y no en el congelador?'},
2 : {'¿Por que las ovejas no se encogen cuando llueve?'},
3 : {'¿Por que se llaman apartamentos cuando estan todos pegados?'},
4 : {'¿Por que los autos conducen en la autopista y se estacionan en la entrada?'}

}
print(context.keys())
print(context.values())

#condicionales

x = 12
if x > 50:
    print("mayor que 50")
else:
    print("menor que 50")
    # ya que x es menor que 50, la segunda sentencia print es la única que se ejecutará.
x = 55
if x > 10:
	print("mayor que 10")
elif x > 50:
	print("mayor que 50")
else:
	print("menor que 10")
    # aunque x es mayor que 10 y 50, la primera sentencia verdadera es la única que se ejecutará, por lo que solo veremos 'mayor que 10'
    
if x < 10:
    print("menor que 10")
    # no pasa nada, porque la sentencia es falsa

    #bucler - For

for x in range(0,10, 2):
    print(x)
# salida: 0, 2, 4, 6, 8
for x in range(5,1,-3):
    print(x)

#recorrer cadenas
for x in 'Hola como estas':
    print(x)

#recorrer listas
mi_lista = ["abc", 123, "xyz"]
for i in range(0, len(mi_lista)):
    print(i, mi_lista[i])

for v in mi_lista:
    print(v)

#recorrer diccionarios
mi_dicc = { "nombre": "Noelle", "lenguaje": "Python" }
for k in mi_dicc:
    print(k)

capitales = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# otra forma de iterar a través de las claves
for key in capitales.keys():
    print(key)
# salida: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
# para iterar a través de los valores
for val in capitales.values():
    print(val)
# salida: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
# para iterar a través de las claves y valores
for key, val in capitales.items():
    print(key, " = ", val)
# salida: Washington = Olympia, California = Sacramento, Idaho = Boise, etc


#funciones
def add(a,b):	# nombre de la función: 'add', parámetros: a y b
    x = a + b	# proceso
    return x	# devuelve valor: x

hola=add(3,5)# llamar la función con los argumentos 3 y 5
print(hola)# el resultado de la función add se devuelve y guarda en new_val, por lo que veremos 8

def di_hola(nombre): #nombre es el parametro
    print("Hola, " + nombre)

di_hola('Gustavo')#el nombre Gustavo es un argumento

def di_hola(nombre):
    return "Hola " + nombre
saludo = di_hola("Michael") # el valor devuelto por la función di_hola se asigna a la variable 'saludo'
print(saludo) # esto dará como resultado 'Hola Michael'

def add(a, b):
    x = a + b
    return x
sum1 = add(4,6)
sum2 = add(1,4)
sum3 = sum1 + sum2

print(sum3)
print(sum2)
print(sum1)

# establece los valores predeterminados al declarar los parámetros
def sé_alegre(name='', repeat=2):
	print(f"buenos días {name}\n" * repeat)
sé_alegre()    # salida: buenos días (repetida en dos líneas)
sé_alegre("tim")    # salida: buenos días tim (repetida en dos líneas)
sé_alegre(name="john")    # salida: buenos días john (repetida en dos líneas)
sé_alegre(repeat=6)    # salida: buenos días (repetida en 6 líneas)
sé_alegre(name="michael", repeat=5)    # salida: buenos días michael (repetida en 5 líneas)
# NOTA: el nombre de los argumentos no importa si somos explícitos al enviarlos
sé_alegre(repeat=3, name="kb")    # salida: buenos días kb (repetida en 3 líneas)

#depuracion de codigo

def multiplicar(num_list, num):
    print(num_list, num)
    for x in range (len(num_list)):
        num_list[x] *= num
        print(num_list)
    return num_list
a = [2,4,10,16]
b = multiplicar(a,5)
print(b)
# salida:
# [2,4,10,16]