from Carta import Carta
from Jugador_Inteligente import Jugador_Inteligente
MASO_A_REPARTIR1=[Carta(13,0),Carta(4,1),Carta(10,0),Carta(2,0),Carta(5,3),Carta(5,2),Carta(11,1),Carta(6,3),Carta(10,2),Carta(11,3),Carta(12,2),Carta(1,2),Carta(10,3)]
MASO_ORDENADO=[Carta(1,2),Carta(2,0),Carta(4,1),Carta(5,2),Carta(5,3),Carta(6,3),Carta(10,0),Carta(10,2),Carta(10,3),Carta(11,1),Carta(11,3),Carta(12,2),Carta(13,0)]
TREBOLES_2=Carta(2,Carta.TREBOLES)

def obtener_jugador_para_prueba():
	"""Devuelve un jugador con 13 cartas para
	realizar las pruebas y valida si el maso 
	esta ordenado probando ademas el metodo
	ordenar_cartas"""
	jugador1=Jugador_Inteligente(1,"Chango Cardenas")
	for carta in MASO_A_REPARTIR1:
		jugador1.recibir_carta(carta)
	assert MASO_ORDENADO==jugador1.obtener_mano_de_cartas()
	return jugador1

def Prueba_primero_en_jugar():
	"""Ejemplos de pruebas donde el jugador decide
	que carta jugar en caso de ser el primer jugador"""
	
	#si el numero de jugada es 1 o 2
	maso_supuesto=[Carta(11,3),Carta(11,1),Carta(10,3),Carta(10,2),Carta(6,3),Carta(5,3),Carta(5,2),Carta(4,1),Carta(1,2),Carta(12,2),Carta(2,0),Carta(10,0),Carta(13,0)]
	jugador=obtener_jugador_para_prueba()
	
	for carta in maso_supuesto:
		assert carta==jugador.jugar_carta(2,2,[],True) 
		
	#si el numero de jugada es >2 y hay ya se jugo un corazon
	maso_supuesto=[Carta(2,0),Carta(4,1),Carta(5,2),Carta(5,3),Carta(6,3),Carta(10,2),Carta(10,3),Carta(11,1),Carta(11,3),Carta(1,2),Carta(10,0),Carta(13,0),Carta(12,2)]
	jugador=obtener_jugador_para_prueba()
	
	for carta in maso_supuesto:
		assert carta==jugador.jugar_carta(3,3,[],True)
	
	#si el numero de jugada es >2 y hay no se jugo un corazon
	maso_supuesto=[Carta(4,1),Carta(5,2),Carta(5,3),Carta(6,3),Carta(10,2),Carta(10,3),Carta(11,1),Carta(11,3),Carta(1,2),Carta(12,2),Carta(2,0),Carta(10,0),Carta(13,0)]
	jugador=obtener_jugador_para_prueba()
	
	for carta in maso_supuesto:
		assert carta==jugador.jugar_carta(3,3,[],False)
		

def Prueba_ultimo_en_jugar():
	"""Ejemplos de pruebas donde el jugador decide que carta jugar
	en caso de ser el ultimo jugador.Tambien se prueba el metodo 
	obtener_cartas_especiales_o_mayores, ya que al no quedar ninguna 
	carta del mismo palo que la primera de las cartas_jugadas, 
	debe proceder a ese metodo"""

	#no depende del numero de jugada (probado 2 veces con distintas cartas_jugadas)
	
	#Prueba 1
	maso_supuesto=[Carta(10,0),Carta(2,0),Carta(13,0),Carta(12,2),Carta(1,2),Carta(11,3),Carta(11,1),Carta(10,3),Carta(10,2),Carta(6,3),Carta(5,3),Carta(5,2),Carta(4,1)]
	cartas_jugadas=[Carta(4,0),Carta(5,1),Carta(11,0)]
	jugador=obtener_jugador_para_prueba()
	
	for carta in maso_supuesto:
		assert carta==jugador.jugar_carta(2,2,cartas_jugadas,True)
	
	#Prueba 2
	maso_supuesto=[Carta(1,2),Carta(10,2),Carta(5,2),Carta(12,2),Carta(13,0),Carta(10,0),Carta(11,3),Carta(11,1),Carta(10,3),Carta(6,3),Carta(5,3),Carta(4,1),Carta(2,0)]
	cartas_jugadas=[Carta(9,2),Carta(5,1),Carta(4,2)]
	jugador=obtener_jugador_para_prueba()
	
	for carta in maso_supuesto:
		assert carta==jugador.jugar_carta(3,3,cartas_jugadas,True)

def Prueba_segundo_o_tercero_en_jugar():
	"""Ejemplos de pruebas donde el jugador decide que carta jugar
	en el caso de ser el segundo o tercer jugador. Se prueba con
	dos numeros de manos diferentes.Tambien se prueba el metodo 
	obtener_cartas_especiales_o_mayores, ya que al no quedar ninguna 
	carta del mismo palo que la primera de las cartas_jugadas, 
	debe proceder a ese metodo"""
	
	#si el numero de jugada es 1 o 2
	
	#Prueba 1
	maso_supuesto=[Carta(10,2),Carta(5,2),Carta(1,2),Carta(12,2),Carta(13,0),Carta(10,0),Carta(11,3),Carta(11,1),Carta(10,3),Carta(6,3),Carta(5,3),Carta(4,1),Carta(2,0)]
	cartas_jugadas=[Carta(2,2)]
	jugador=obtener_jugador_para_prueba()
	
	for carta in maso_supuesto:
		assert carta==jugador.jugar_carta(2,2,cartas_jugadas,True) 
	
	#Prueba 2
	maso_supuesto=[Carta(10,0),Carta(2,0),Carta(13,0),Carta(12,2),Carta(1,2),Carta(11,3),Carta(11,1),Carta(10,3),Carta(10,2),Carta(6,3),Carta(5,3),Carta(5,2),Carta(4,1),]
	cartas_jugadas=[Carta(3,0),Carta(12,0)]
	jugador=obtener_jugador_para_prueba()
	
	for carta in maso_supuesto:
		assert carta==jugador.jugar_carta(2,2,cartas_jugadas,True)

	#si el numero de jugada es >2
	
	#Prueba 1
	maso_supuesto=[Carta(5,2),Carta(10,2),Carta(1,2),Carta(12,2),Carta(13,0),Carta(10,0),Carta(11,3),Carta(11,1),Carta(10,3),Carta(6,3),Carta(5,3),Carta(4,1),Carta(2,0)]
	cartas_jugadas=[Carta(2,2)]
	jugador=obtener_jugador_para_prueba()
	
	for carta in maso_supuesto:
		assert carta==jugador.jugar_carta(3,3,cartas_jugadas,True) 
	
	#Prueba 2
	maso_supuesto=[Carta(5,3),Carta(6,3),Carta(10,3),Carta(11,3),Carta(12,2),Carta(13,0),Carta(10,0),Carta(1,2),Carta(11,1),Carta(10,2),Carta(5,2),Carta(4,1),Carta(2,0)]
	cartas_jugadas=[Carta(3,3),Carta(12,0)]
	jugador=obtener_jugador_para_prueba()
	
	for carta in maso_supuesto:
		assert carta==jugador.jugar_carta(3,3,cartas_jugadas,True)
	
def Prueba_borrar_carta_de_mano():
	"""Ejemplos de prueba del metodo borrar_carta_de_maso
	del jugador"""
	jugador=obtener_jugador_para_prueba()
	carta=Carta(12,2)
	carta_a_comparar=jugador.borrar_carta_de_mano(carta)
	assert carta_a_comparar==carta
	assert not carta in jugador.obtener_mano_de_cartas()

def Prueba_devolver_carta_en_mano():
	"""Ejemplos de prueba del metodo devolver_carta_en_mano
	del jugador"""
	jugador=obtener_jugador_para_prueba()
	carta_en_maso=Carta(4,1)
	carta_fuera_de_maso=Carta(1,1)
	carta_a_comparar=jugador.devolver_carta_en_mano(carta_en_maso)
	assert carta_a_comparar==carta_en_maso
	assert not carta_en_maso in jugador.obtener_mano_de_cartas()
	carta_a_comparar=jugador.devolver_carta_en_mano(carta_fuera_de_maso)
	assert carta_a_comparar==None
	
def Prueba_devolver_cartas_a_pasar():
	"""Ejemplos de pruebas de devolver_cartas_a_pasar del jugador"""
	jugador=obtener_jugador_para_prueba()
	
	#Prueba 1
	maso_a_devolver=[Carta(12,2),Carta(1,2),Carta(13,0)]
	assert maso_a_devolver==jugador.devolver_cartas_a_pasar(1)
	
	#Prueba 2
	maso_a_devolver=[Carta(10,0),Carta(11,3),Carta(11,1)]
	assert maso_a_devolver==jugador.devolver_cartas_a_pasar(1)

def Prueba_es_primero():
	"""Ejemplo de prueba del metodo es_primero"""
	jugador=obtener_jugador_para_prueba()
	assert not jugador.es_primero()
	jugador.recibir_carta(TREBOLES_2)
	assert jugador.es_primero()
	
def Prueba_buscar_carta():
	"""Ejemplo de prueba del metodo buscar_carta"""
	lista_cartas=[]
	jugador=obtener_jugador_para_prueba()
	
	#Prueba 1, la carta se encuentra en la mano de cartas
	carta=Carta(13,0)
	jugador.buscar_carta(lista_cartas,carta)
	assert carta in lista_cartas
	assert carta not in jugador.obtener_mano_de_cartas()
	
	#Prueba 2, la carta no se encuentra en la mano de cartas
	cantidad_de_cartas=len(lista_cartas)
	jugador.buscar_carta(lista_cartas,TREBOLES_2)
	assert cantidad_de_cartas==len(lista_cartas)
	
def Prueba_jugar_2_treboles():
	"""Ejemplo de prueba del metodo jugar_carta cuando se
	posee el 2 de treboles"""
	jugador=obtener_jugador_para_prueba()
	jugador.recibir_carta(TREBOLES_2)
	
	assert jugador.jugar_carta(2,1,[],False)==TREBOLES_2
	assert not TREBOLES_2 in jugador.obtener_mano_de_cartas()
	
def Prueba_recibir_cartas_pasadas():
	"""Ejemplo de prueba del metodo recibir_cartas_`pasadas"""
	lista_cartas=[Carta(2,1),Carta(2,2),Carta(2,3)] #cartas que no estan en la mano
	jugador=obtener_jugador_para_prueba()
	jugador.recibir_cartas_pasadas(3,lista_cartas)
	for carta in lista_cartas:
		assert carta in jugador.obtener_mano_de_cartas()
		
def Prueba_recibir_carta():
	"""Ejemplo de prueba del metodo recibir_carta"""
	carta=Carta(2,1) #carta que no esta en la mano
	jugador=obtener_jugador_para_prueba()
	jugador.recibir_carta(carta)
	assert carta in jugador.obtener_mano_de_cartas()
	
	
def pruebas():
	for prueba in (
		obtener_jugador_para_prueba,
		Prueba_devolver_carta_en_mano,
		Prueba_borrar_carta_de_mano,
		Prueba_segundo_o_tercero_en_jugar,
		Prueba_ultimo_en_jugar,
		Prueba_primero_en_jugar,
		Prueba_devolver_cartas_a_pasar,
		Prueba_recibir_carta,
		Prueba_recibir_cartas_pasadas,
		Prueba_jugar_2_treboles,
		Prueba_buscar_carta,
		Prueba_es_primero
		
	):
		print (prueba.__name__ + ":"),
		prueba()
		print "OK"

pruebas()
	
	