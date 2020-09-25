##### JUEGO DE 21 #####
#MAURICIO GONZALEZ
#CLASE DE INFORMATICA

###librerias
import random

###Funcion barajar: Prepara la baraja, la revuelve y reparte juego inicial
def barajar():
    baraja=[]
    for i in ["02","03","04","05","06","07","08","09","10"," J"," Q"," K","A"]:
        for j in ["p", "c", "t", "d"]:
            carta = "{}{}".format(i,j)
            baraja.append(carta)
    random.shuffle(baraja) 
    return baraja

###funcion contar: Determina el valor en puntos de cada carta
def contar (val):
    if val[0]=='A':
        return 11
    elif val[0]== ' ':
        return 10
    else:
        return int(val[0:2])

###Funcion repartir carta: Entrega una carta y devuelve la sumatoria en [1] . En [2] marca si hay un AS ... el resto son las cartas
def repartircarta(B,J):
    if len(J) == 1:
        J.append(contar(B[0]))
        if contar(B[0])==11:
            J.append(1)
        else:
            J.append(0)
    else:
        J[1] = J[1] + contar(B[0])
        if contar(B[0])==11:
            J[2] = 1
    if (J[1])>21:
        if J[2] == 1:
            J[1]=(J[1]-10)
            J[2]=0
    J.append(B.pop(0))
    #mostrarCartas(J)
    return J

###Funcion jugar21: Pregunta al jugador si quiere mas cartas
def jugar21(B,J):
    while J[1]<21:
        print("\nJugando ",J[0])
        print ("\n   Oprima ""s"" para recibir otra carta, o ""p"" para plantarse...")
        if input()=="s":
            J=repartircarta(B,J)
            mostrarCartas(J)
        else:
            mostrarCartas(J)
            break
    return J

###Funcion MostrarCartas: Representacion Visual de las cartas
def mostrarCartas(J):
    P = ["corazones", "picas", "diamantes", "treboles"]
    print ("\n", J[0], "tiene", J[1], "puntos, y sus cartas son...")
    for i in range(3, len(J)):
        if (J[i])[0]=="A":
            print("   AS de", [a for a in P if (a[0] == (J[i])[-1:])][0])
        elif (J[i])[0]==" ":
            print("   ", (J[i])[1], "de",  [a for a in P if (a[0] == (J[i])[-1:])][0])
        else:
            print("   ",(contar(J[i])), "de",  [a for a in P if (a[0] == (J[i])[-1:])][0])

##VARIABLES GLOBALES
J1=[]
J2=[]

#################MAIN######################
print ("\n ")
print ("\n##########   JUEGO DE 21   ###########")
print ("\n ")
BAR = barajar()                                     #se crea la baraja y se revuelve
print(BAR)

J1.append("Jugador 1")
J2.append("LA CASA")

for i in range (2):
    J1 = repartircarta(BAR,J1)                        #reparte 2 cartas a jugador 1
    J2 = repartircarta(BAR,J2)                        #reparte 2 cartas a jugador 2

mostrarCartas(J1)
mostrarCartas(J2)

while 1>0:
    J1 = jugar21(BAR,J1)
    if J1[1]>21:
        print("", J1[0], "perdió, se pasó con ", J1[1])
        break
    J2 = jugar21(BAR,J2)
    if J2[1]>21:
        print("", J2[0], "perdió, se pasó con ", J2[1])
        break

    if (J1[1] > J2[1]):
        print ("\nHa ganado", J1[0], J1[1], "contra", J2[1])
        break
    else:
        print ("\nHa ganado", J2[0], J2[1], "contra", J1[1])
        break
