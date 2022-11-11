from Corazones import JuegoCorazones
from Jugador_Inteligente import Jugador_Inteligente

jug_prueba1 = Jugador_Inteligente(0,"Kevin")
jug_prueba2 = Jugador_Inteligente(1,"Alan")
jug_prueba3 = Jugador_Inteligente(2,"Lucas")
jug_prueba4 = Jugador_Inteligente(3,"Felipe")

juego_prueba = JuegoCorazones([jug_prueba1,jug_prueba2,jug_prueba3,jug_prueba4])

print
print "Bienvenidos al Juego Corazones:"
print 
print "Participaran cuatro jugadores: Kevin, Alan, Lucas y Felipe"
print "=========================================================="
print
juego_prueba.jugar()
ganadores = juego_prueba.ganadores()
print 

if len(ganadores) > 1:
	print "Los Ganadores Son con el minimo puntaje: "
	for ganador in ganadores:
		print ganador
else:
	print "El Ganador es ",ganadores[0]
print
print "Gracias por usar el Juego Corazones !!!"