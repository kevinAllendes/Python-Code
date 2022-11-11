from Carta import Carta
from Corazones import JuegoCorazones
from Jugador_Inteligente import Jugador_Inteligente

#Constantes
MAXPUNTAJE=100
PUNTAJE_BAJO = 0
PUNTAJE_INTERM = 50
INDICE_JUG_NO_PERTENECE = 4
INDICE_JUG_PERTENECE = 0
ID_ULTIMO_JUGADOR = 3
ID_PRIMER_JUGADOR = 0
ID_SEGUNDO_JUGADOR = 1
ID_TERCER_JUGADOR = 2

#Implementacion Pruebas
def Crear_lista_de_cartas():
	Carta1 = Carta(12,2)# Q  de Picas
	Carta2 = Carta(2,2)# 2  de Picas
	Carta3 = Carta(1,2)# As de Picas
	Carta4 = Carta(6,2)# 6  de Picas
	Carta5 = Carta(2,3)# 2 de Treboles
	Carta6 = Carta(4,0)# 4 de Corazones
	return [Carta1,Carta2,Carta3,Carta4,Carta5,Carta6]
	

def Crear_lista_de_jugadores():
	jug_prueba1 = Jugador_Inteligente(0,"Kevin")
	jug_prueba2 = Jugador_Inteligente(1,"Alan")
	jug_prueba3 = Jugador_Inteligente(2,"Lucas")
	jug_prueba4 = Jugador_Inteligente(3,"Felipe")
	jug_prueba5 = Jugador_Inteligente(0,"Romualdo")
	return [jug_prueba1,jug_prueba2,jug_prueba3,jug_prueba4,jug_prueba5]


def Prueba_puntaje_del_jugador_que_no_pertenece(juego_prueba):
	"""Probamos si el metodo puntaje_del_jugador 
	funciona correctamente cuando le mandamos un jugador que no 
	pertenece al juego """
	excepcion_capturada = False
	try:
		jugador_q_no_pertenece = jugadores[INDICE_JUG_NO_PERTENECE]
		puntaje = juego_prueba.puntaje_del_jugador(jugador_q_no_pertenece)
	except:
		excepcion_capturada = True
	assert excepcion_capturada
		
def Prueba_puntaje_del_jugador_que_pertenece(juego_prueba):
	"""Probamos si el metodo_puntaje_del_jugador devuele el 
	puntaje del un jugador del juego correctamente"""
	juego_prueba.modificar_puntajes([PUNTAJE_INTERM,MAXPUNTAJE,PUNTAJE_BAJO,PUNTAJE_BAJO])
	jugador_q_pertenece = juego_prueba.devolver_lista_de_jugadores()[ID_PRIMER_JUGADOR]
	#A este jugador le corresponde el primer puntaje PUNTAJE_INTERM
	puntaje = juego_prueba.puntaje_del_jugador(jugador_q_pertenece)
	assert PUNTAJE_INTERM == puntaje
	

def Prueba_termino_verdadera(juego_prueba):
	"""Probamos la correcta ejecucion de 
	el metodo termino cuando se alcanzo el puntaje maximo"""
	juego_prueba.modificar_puntajes([PUNTAJE_BAJO,MAXPUNTAJE,PUNTAJE_BAJO,PUNTAJE_BAJO])
	assert juego_prueba.termino()

def Prueba_termino_falsa(juego_prueba):
	"""Probamos la correcta ejecucion de 
	el metodo termino cuando no se alcanzo el puntaje maximo"""
	juego_prueba.modificar_puntajes([PUNTAJE_BAJO,PUNTAJE_BAJO,PUNTAJE_BAJO,PUNTAJE_BAJO])
	assert not(juego_prueba.termino())

def Prueba_barajar_mazo(juego_prueba):
	"""Probamos el metodo barajar comprobando que haya
	otorgado las 13 cartas a cada un de los 
	jugadores participantes"""
	juego_prueba.barajar()
	jugadores = juego_prueba.devolver_lista_de_jugadores()
	for jugador in jugadores:
		assert len(jugador.obtener_mano_de_cartas()) == 13


def Prueba_identificar_jugador_que_perdio(juego_prueba):
	"""Prueba que al metodo identificar_jugador_que_perdio
	La lista de cartas enviadas por parametro
	seran: Q,2,As y 6 de Picas (en este orden), 
	el id del jugador que inicia sera el del primer jugador (0) 
	por lo tanto el id del que perdio sera igual al id 
	del tercer jugador (2)"""
	id_perdio = juego_prueba.identificar_jugador_que_perdio(Crear_lista_de_cartas()[:-2],ID_PRIMER_JUGADOR) 
	assert id_perdio == ID_TERCER_JUGADOR

def Prueba_hay_corazones_falsa(juego_prueba):
	"""Prueba el metodo de hay_corazones cuando no hay corazones
	entre las cartas enviadas
	se envian las cartas:  Q, 2 y As de Picas """
	assert not(juego_prueba.hay_corazones(Crear_lista_de_cartas()[:-3]))
	
def Prueba_hay_corazones_verdadera(juego_prueba):
	"""Prueba el metodo de hay_corazones cuando hay corazones
	entre las cartas enviadas se envian las cartas: 6 de Picas 
	2 de treboles y 4 de corazones"""
	assert juego_prueba.hay_corazones(Crear_lista_de_cartas()[3:]) 


def Prueba_calcular_puntajes(juego_prueba):
	"""Prueba el metodo calcular_puntajes 
	cambiamos las cartas levantadas de los jugadores
	asignandole el Q,2 y As de Picas al primero
	el 6 de Picas al segundo, el 2 de treboles al tercero y
	el 4 de Corazones al cuarto por lo tanto el puntaje de cada uno
	sera 13,0,0,1 """
	juego_prueba.modificar_puntajes([PUNTAJE_BAJO,PUNTAJE_BAJO,PUNTAJE_BAJO,PUNTAJE_BAJO])
	cartas = Crear_lista_de_cartas()
	cartas_prim = cartas[:-3] 
	cartas_seg  = [cartas[3]]
	cartas_ter  = [cartas[4]]
	cartas_cuar = [cartas[5]]
	juego_prueba.modificar_cartas_levantadas([cartas_prim,cartas_seg,cartas_ter,cartas_cuar])
	juego_prueba.calcular_puntajes()
	assert juego_prueba.devolver_puntajes() == [13,0,0,1]
	
def Prueba_ganadores(juego_prueba):
	"""Prueba que el metodo ganadores me de el resultado correcto
	le doy cuatro puntajes siendo el primero y el ultimo puntajes ganadores
	tengo que recibir el primer y ultimo jugador"""
	nuevos_puntos = [PUNTAJE_INTERM,MAXPUNTAJE,MAXPUNTAJE,PUNTAJE_INTERM]
	juego_prueba.modificar_puntajes(nuevos_puntos)
	jugadores = juego_prueba.devolver_lista_de_jugadores()
	ganadores = [jugadores[ID_PRIMER_JUGADOR],jugadores[ID_ULTIMO_JUGADOR]]
	assert juego_prueba.ganadores() == ganadores

#__________________________________________________________________________________________-

def Crear_juego_prueba():
	"""Crea un juego de pruebas en base a una lista
	de cuatro jugadores dada por la funcion 
	Crear_lista_de_jugadores"""
	jugadores = Crear_lista_de_jugadores()
	juego = JuegoCorazones(jugadores[:-1])
	return juego

""".........Crean un juego nuevo para realizar la prueba................"""
def Prueba_identificar_jugador_que_inicia():
	"""Probamos si el metodo identifica_jugador_que_inicia
	funciona correctamente"""
	juego_prueba = Crear_juego_prueba()
	cartas = Crear_lista_de_cartas()
	id_carta = 1
	for jugador in juego_prueba.devolver_lista_de_jugadores():
		jugador.recibir_carta(cartas[id_carta])
		#La carta 2 de treboles se la damos al ultimo jugador (id igual 3)
		id_carta += 1
	assert juego_prueba.identificar_jugador_que_inicia() == ID_ULTIMO_JUGADOR


def Prueba_identificar_jugador_que_inicia_sin_carta_inicial():
	"""Comprobamos que el metodo identificar_jugador_que_inicia lanze
	una excepcion cuando no esta la carta que inicia"""
	excepcion_capturada = False
	try:
		juego_prueba = Crear_juego_prueba()
		cartas = Crear_lista_de_cartas()
		id_carta = 0
		for jugador in juego_prueba.devolver_lista_de_jugadores():
			jugador.recibir_carta(cartas[id_carta])
			#El id_carta no correspondera al 2 de treboles en ningun caso
			id_carta += 1
		id_inicia = juego_prueba.identifica_jugador_que_inicia()
	except:
		excepcion_capturada = True
	assert excepcion_capturada


def Prueba_intercambiar_cartas():
	"""Prueba que los intercambios no lancen ningun error"""
	juego_prueba = Crear_juego_prueba()
	juego_prueba.barajar()#Teniendo en cuenta que ya se probo barajar_mazo
	juego_prueba.desactivar_muestreo_de_cartas_intercambiadas()
	for nro_mano in range(1,5):
		juego_prueba.intercambiar_cartas(nro_mano)

"""________________________________________________________________________"""


def pruebas(juego_prueba):
	for prueba in (
		Prueba_puntaje_del_jugador_que_no_pertenece,
		Prueba_puntaje_del_jugador_que_pertenece,
		Prueba_termino_verdadera,
		Prueba_termino_falsa,
		Prueba_barajar_mazo,
		Prueba_identificar_jugador_que_perdio,
		Prueba_hay_corazones_falsa,
		Prueba_hay_corazones_verdadera,
		Prueba_calcular_puntajes,
		Prueba_ganadores
	):
		print (prueba.__name__ + ":"),
		prueba(juego_prueba)
		print "OK"
#Fin de la seccion de definicion de Funciones de Prueba
#======================================================

juego_prueba_corazones = Crear_juego_prueba()

pruebas(juego_prueba_corazones)

Prueba_identificar_jugador_que_inicia()
print Prueba_identificar_jugador_que_inicia.__name__,": OK"
Prueba_identificar_jugador_que_inicia_sin_carta_inicial()
print Prueba_identificar_jugador_que_inicia_sin_carta_inicial.__name__,": Ok"
Prueba_intercambiar_cartas()
print Prueba_intercambiar_cartas.__name__,": Ok"
