#Cambia el valor 10 en x a 15
x = [ [5,2,3], [10,8,9] ] 
x[1][0]=15
print(x)

#Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
estudiantes[0]['last_name']='Bryant'
print(estudiantes)

# cambia "Messi" por "Andrés".
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'futbol' : ['Messi', 'Ronaldo', 'Rooney']
}
directorio_deportes['futbol'][0]='Andres'
print(directorio_deportes)

#Cambia el valor 20 en z a 30
z = [ 
    {'x': 10, 'y': 20} 
    ]

for eleme in z:
    for k,v in eleme.items():
        if v==20:
            eleme.update({'y':30})
print (z)           


estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
#Iterar a través de una lista de diccionarios
def iterateDictionary(lista):
    for ele in lista:
        texto=''
        for k,v in ele.items():
            texto=texto+', '+k+' - '+v
        print(texto)

iterateDictionary(estudiantes) 

#Obtener valores de una lista de diccionarios
def iterateDictionary2(key, lista):
    for ele in lista:
        for k,v in ele.items():
            if k==key:
                print(v)

iterateDictionary2('last_name', estudiantes)

dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon','Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dic):
    for ele in dic:
        print (len(dic[ele]), ele)
        
        print('\n'.join(map(str, dic[ele])))



printInfo(dojo)
