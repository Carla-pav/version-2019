from tablero import draw_tablero, win, validate, full
tablero=[]
for i in range(0,9):
    tablero.append(" ")
draw_tablero(tablero)
while win(tablero)==False and full(tablero)==False:
    print ("turno de la X")
    valido=False
    while not valido:
        print("Ingrese una posocion valida del 1 al 9")
        posicion=int(input())
        valido=validate(tablero,posicion)
        if not valido:
            print ("Error de posicion")
    tablero[posicion-1]="X"
    draw_tablero(tablero)
    gano=win(tablero)
    if gano:
        print ("Gano X")
    else:
        print ("turno de la O")
        valido=False
        while not valido:
            print("Ingrese una posocion valida del 1 al 9")
            posicion=int(input())
            valido=validate(tablero,posicion)
            if not valido:
                print ("Error de posicion")
        tablero[posicion-1]="O"
        draw_tablero(tablero)
        gano=win(tablero)
        if gano:
            print ("Gano O")
if full(tablero) and not win(tablero):
    print("nadie gano")