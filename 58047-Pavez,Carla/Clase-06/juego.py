from generador import generador_mejor, generador
adivinado=False
aleatorio=generador(0,100)
minimo=0
maximo=100
while adivinado == False:
    print ("Ingresa un numero")
    numero= int (input())
    if numero == aleatorio:
        print("Ganaste")
        adivinado=True
    if numero < aleatorio:
        print ("Ingrese un numero mayor")
    if numero > aleatorio:
        print ("Ingrese un numero menor")
    if adivinado == False:
        print ("ahora le toca a la coomputadora")
        computadora=generador(minimo,maximo)
        print("La computadora penso " + str(computadora))
        if computadora == aleatorio:
            print ("Gano la computadora")
            adivinado=True
        if computadora < aleatorio:
            minimo=computadora
        if computadora > aleatorio:
            maximo=computadora
