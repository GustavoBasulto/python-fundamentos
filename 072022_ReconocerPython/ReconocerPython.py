num1 = 42 #Se crea una variable de tipo entero con valor 42 asignado
num2 = 2.3 #Se crea una variable de tipo float con valor 2.3 asignado, esta variable permite decimales
boolean = True #Se crea una variable de tipo bolean con valor verdadero asignado, booleano solo puede ser verdadero o falso
string = 'Hello World' #Se crea una variable de tipo string con el texto hello world asignado
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #se crea una lista con valores prededterminados
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #se crea un objeto con atributos
fruit = ('blueberry', 'strawberry', 'banana') #se asignan objetos a una clase
print(type(fruit))#imprime el typo de variable ded fruit
print(pizza_toppings[1])#imprime el valor que se encuentra en la segunda posicion del arreglo
pizza_toppings.append('Mushrooms')#agrega un valor al final del arreglo
print(person['name'])#imprime solo los nombres de los objetos persona
person['name'] = 'George'# asigna un nombre al atributo name del objeto persona
person['eye_color'] = 'blue'# crea y asigna un valor a un atributo de el objeto persona 
print(fruit[2])# imprime el valor en el indice 2 

if num1 > 45: #operador de condicion si num1 es mayor a 45
    print("It's greater")# imprime texto si se cumple condicion
else:# si no se cumple la condicion anterior
    print("It's lower")# imprime texto si no se cumple condicion

if len(string) < 5:#operador de condicion si el largo de caracteres de la variable string es menor a 5
    print("It's a short word!")# imprime texto si se cumple condicion
elif len(string) > 15:#operador de condicion si el largo de caracteres de la variable string es mayor a 15
    print("It's a long word!")# imprime texto si se cumple condicion
else:
    print("Just right!")# imprime texto si no se cumple ninguna de las condiciones anteriores 

for x in range(5):#ejecuta el contenido 5 veces
    print(x)#imprime el valor de la variable x
for x in range(2,5):
    print(x)#imprime el valor de la variable x
for x in range(2,10,3):
    print(x)#imprime el valor de la variable x
x = 0#cambia el valor de la variable x a 0
while(x < 5): #se ejecuta mientras x sea menor que 5
    print(x) #imprime el valor de x
    x += 1 #cada ves que se pasa por aca se le suma 1 al valor de x

pizza_toppings.pop()#elimina el ultimo valor de la lista    
pizza_toppings.pop(1)#elimina el valor en el indice 1 de la lista

print(person)#imprime el objeto persona
person.pop('eye_color')#elimina el atributo 'eye_color'  del objeto persona
print(person)#imprime el objeto persona modificado

for topping in pizza_toppings:#recorre el arreglo pizza_toppings
    if topping == 'Pepperoni': # si el valor en la posicion del recorrido es igual a pepperoni continua
        continue
    print('After 1st if statement')
    if topping == 'Olives': # si el valor en la posicion del recorrido es igual a Olives termina
        break

def print_hello_ten_times():#genera una funcion que imprime la palabra Hello 10 veces
    for num in range(10):
        print('Hello')

print_hello_ten_times()#Ejecuta la funcion anteriomente creada

def print_hello_x_times(x):#genera una funcion que imprime la palabra Hello X veces
    for num in range(x):
        print('Hello')

print_hello_x_times(4) #Ejecuta la funcion anteriomente creada y le asigna el valor 4 para que se ejecute 4 veces

def print_hello_x_or_ten_times(x = 10):#genera una funcion que imprime la palabra Hello X veces, y si no hay valor asume el 10
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()#Ejecuta la funcion anteriomente creada y se repite 10 veces
print_hello_x_or_ten_times(4)#Ejecuta la funcion anteriomente creada y se repite 4 veces


"""
Bonus section
"""

# print(num3) #No imrpime nada ya que la variable no tiene valor
# num3 = 72 #le asigna el valor 72 a la variable num3
# fruit[0] = 'cranberry' #asigna el texto 'cranberry' al indice 0 del arreglo fruit
# print(person['favorite_team']) #No imprime nada ya que el objeto persona no tiene el atributo 'favorite_team'
# print(pizza_toppings[7])#No imprime nada ya que pizza_toppings no tiene nada en el indice 7
#   print(boolean) #imprime true
# fruit.append('raspberry')#agrega otro valor al arreglo fruit, el valor 'raspberry'
# fruit.pop(1) #Elimina el valor recien agregado 