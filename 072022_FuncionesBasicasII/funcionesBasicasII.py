#Cuenta regresiva
def cuenta_regresiva(num):
    lista=[]
    for x in range(num, -1, -1):
        lista.append(x);
    return (lista)    
cuenta=cuenta_regresiva(15)
print(cuenta)

#imprimir y devolver
def imprime_devuelve(list):
    print (list[0])
    return list[1]
imprime_devuelve([1,5])

#Primero mas longitud
def primero_longitud(list):
    x=list[0]
    y=len(list)
    return (x+y)

primero_longitud([80,5,7,8,25,65,75]) 

#Valores mayores que el segundo
def mayor_segundo(list):
    print(list)
    if len(list)<2:
        return False
    else:
        newlist=[]
        cont=0
        
        for x in range(len(list)):
            if list[x]> list[1]:
                newlist.append(list[x])
                cont+=1
            else:
                continue
        print (cont)
        return newlist       
mayor_segundo([5,2,3,2,1,4])

#Esta longitud, ese valor
def ese_valor(tamano,valor):
    lista=[]
    for x in range(tamano):
        lista.append(valor)
    return lista
ese_valor(6,2)