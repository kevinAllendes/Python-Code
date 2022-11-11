from Carta import Carta
from Mazo import Mazo
#Constantes 
MAXPUNTAJE=100
Q_DE_PICAS = 12
CORAZONES = 0
PICAS = 2
PESO_CARTAS = [2,3,4,5,6,7,8,9,10,11,12,13,1]#En orden ascendente el 1 corresponde al AS
CANT_JUGADORES = 4
MAX_ID = 3
MIN_ID = 0
NUM_MANO_SIN_INTERCAMBIO = [4,8,12,16,20,24]
NUM_MANO_INTERC_AGUJ_RLOJ = [1,5,9,13,17,21,25]
NUM_MANO_INTERC_CONTRA_AGUJ_RLOJ = [2,6,10,14,18,22,26]
NUM_MANO_INTERC_JUG_FRENTE = [3,7,11,15,19,23]

#Clases
class JuegoCorazones(object):
	"""Clase que representa un juego de Corazones"""

	def __init__(self, jugadores):
		"""Crea un juego en base a 4 jugadores
		;jugadores es una lista de jugadores"""
		if len(jugadores) != CANT_JUGADORES:
			raise Exception("Error en el ingreso de jugadores!")
		self.jugadores = jugadores
		self.puntajes = [0,0,0,0]
		self.mano_actual = None
		self.mostrar_intercambiadas = True #si es True se muestran las cartas intercambiadas
		self.cartas_levantadas = [[],[],[],[]]

	def puntaje_del_jugador(self,jugador):
		"""Devuelve el puntaje del jugador"""
		if not(jugador in self.jugadores):
			raise Exception("El jugador no pertenece al juego!")
		indice = self.jugadores.index(jugador)
		return self.puntajes[indice]

	def termino(self):
		"""Devuelve True si alguno de los jugadores alcanzo los 100 puntos""" 
		for puntos in self.puntajes:
			if puntos >= MAXPUNTAJE:
				return True
		return False

	def imprimir_puntajes(self):
		"""Imprime los puntajes de cada jugador hasta el momento""" 
		id_jugador = 0
		for puntos in self.puntajes:
			print "El jugador ",self.jugadores[id_jugador]," tiene "+str(puntos)+" puntos.."
			id_jugador +=1
		print
		print  "Fin de la Mano"
		continuar = raw_input("Para continuar presione Enter..")
		print

	def definir_siguiente(self,num_jugador):
		"""si el num_jugador es igual a tres el siguiente es el cero
		en caso contrario le sumamos 1 """
		if num_jugador == MAX_ID: 
			return MIN_ID
		else:
			return (num_jugador + 1)

	def barajar(self):
		"""Crea un mazo nuevo, lo mezcla y le reparte una carta a cada jugador hasta
		que el mismo queda vacio."""
		try:
			Mazo_principal = Mazo()
			Mazo_principal.mezclar()
			numero_jugador = 0
			while not(Mazo_principal.es_vacio()):
				carta_nueva = Mazo_principal.obtener_tope()
				self.jugadores[numero_jugador].recibir_carta(carta_nueva)
				numero_jugador = self.definir_siguiente(numero_jugador)
		except:
			raise Exception("Error al barajar el maso")


	def identificar_jugador_que_inicia(self): 
		"""Se fija cual de los 4 jugadores es primero y devuelve su id.
		Si no encuentra la carta en las manos de los jugadores
		devuelve excepcion"""
		for jugador in self.jugadores:
			if jugador.es_primero():
				id_jugador_inicia = jugador.obtener_id_jugador()
				return id_jugador_inicia
		raise Exception("No se encontro la carta inicial")


	def identificar_jugador_que_perdio(self, cartas_jugadas, id_primero):
		"""Recibe las 4 cartas jugadas en la mano y el id del jugador que abrio
		la jugada. Devuelve el id del jugador que perdio.
		Pierde el jugador que juega la carta mas alta del palo con el que inicio
		la jugada el primer jugador.
		Las cartas por orden creciente son: 2, 3,..., 10, J, Q, K, A."""
		carta_inicial = cartas_jugadas[0]
		id_actual = id_primero
		id_perdedor = id_primero 
		peso_actual = PESO_CARTAS.index(carta_inicial.obtener_numero())
		
		for carta in cartas_jugadas:
			if carta.obtener_palo() == carta_inicial.obtener_palo():
				peso = PESO_CARTAS.index(carta.numero)
				if peso > peso_actual:
					id_perdedor = id_actual 
					peso_actual = peso
			id_actual = self.definir_siguiente(id_actual)
		return id_perdedor


	def procesar_e_informar_resultado(self, cartas_jugadas, id_primero, id_perdedor): 
		"""Recibe las cartas de la jugada, el id del primer jugador, y el id del
		jugador que perdio.
		Almacena lo necesario para llevar la cuenta de puntos e informa a todos
		los jugadores del resultado de la jugada."""
		if not(MIN_ID <= id_primero <= MAX_ID) or not(MIN_ID <= id_perdedor <= MAX_ID):
			raise Exception("El id ingresado es incorrecto..")
		for carta in cartas_jugadas:
			self.cartas_levantadas[id_perdedor].append(carta)
		#_____________________________________________________________
		#Mostramos las cartas jugadas
		id_ = id_primero
		print "En esta ronda se realizaron los siguientes descartes: "
		for carta in cartas_jugadas:
			print self.jugadores[id_]," descarta: ",carta
			id_ = self.definir_siguiente(id_)
		print "....."
		#___________________________________________________________

	def hay_corazones(self, cartas):
		"""Devuelve True si hay algun corazon entre las cartas pasadas"""
		if len(cartas) == 0:
			raise Exception("No se han recibido cartas")
		for carta in cartas:
			if carta.obtener_palo() == CORAZONES: 
				return True
		return False

	def realizar_jugada(self, nro_mano, nro_jugada, id_primero, corazon_jugado):
		"""Recibe el numero de mano, de jugada el id del primer jugador y si ya
		se jugaron corazones hasta el momento.
		Hace jugar una carta a cada uno de los jugadores empezando por el primero.
		Devuelve las 4 cartas jugadas."""
		id_actual = id_primero
		cartas_jugadas = []
		tenemos_corazones = False
		while len(cartas_jugadas) < 4:#No pueden haber mas de cuatro cartas jugadas
			#Solo si hay cartas ya jugadas pregunta si hay corazones
			if len(cartas_jugadas) != 0:
				tenemos_corazones = self.hay_corazones(cartas_jugadas)
			#pedimos una nueva carta y la agregamos a las cartas ya jugadas
			carta_nueva = self.jugadores[id_actual].jugar_carta(nro_mano,nro_jugada,cartas_jugadas,tenemos_corazones)
			cartas_jugadas.append(carta_nueva)
			#modificamos el id dependiendo del valor del mismo
			id_actual = self.definir_siguiente(id_actual)
		return cartas_jugadas                

	def calcular_puntajes(self):
		"""Al finalizar la mano, calcula y actualiza los puntajes de los jugadores.
		Cada jugador suma un punto por cada corazon levantado en la mano y 13 puntos
		si levanto la Q de picas, salvo en el caso de que un solo jugador haya
		levantado todos los corazones y la Q de picas, caso en el cual todos los
		jugadores salvo el suman 26 puntos."""
		id_actual = 0
		for cartas in self.cartas_levantadas:
			suma_puntos = 0
			if len(cartas) != 0:
				for carta in cartas:
					if carta.obtener_palo() == CORAZONES:
						suma_puntos +=1
					if (carta.obtener_palo() == PICAS) and (carta.obtener_numero() == Q_DE_PICAS):
						suma_puntos += 13
				if suma_puntos == 26:#Reune todas las cartas que suman puntos
					id_especial = id_actual
					for jugador in self.jugadores:
						if jugador.obtener_id_jugador() != id_especial:
							self.puntajes[jugador.obtener_id_jugador()]+=26
				else:
					self.puntajes[id_actual]+= suma_puntos
			id_actual += 1
		#Vacia las lista de cartas levantadas de todos los jugadores
		self.cartas_levantadas = [[],[],[],[]]

#_______________________________________________________________________________________

	def Mostrar_cartas_de_intercambio(self,cartas,id_reci,id_da):
		"""en caso de que mostrar intercambiadas sea True mostrara las cartas
		del intercambio"""
		if self.mostrar_intercambiadas:
			print
			print "El jugador ",self.jugadores[id_da].nombre, " le da las cartas"
			for carta in cartas:
				print carta
			print "... a el jugador ",self.jugadores[id_reci].nombre
			print

	def Realizar_entrega_de_cartas(self,id_jug_recibe,id_jug_dio_cartas,cartas_a_pasar):
			"""Realiza la entrega de cartas a los jugadores"""
			for tres_cartas in cartas_a_pasar:
				self.jugadores[id_jug_recibe].recibir_cartas_pasadas(id_jug_dio_cartas,tres_cartas)
				self.Mostrar_cartas_de_intercambio(tres_cartas,id_jug_recibe,id_jug_dio_cartas)
				id_jug_recibe = self.definir_siguiente(id_jug_recibe)
				id_jug_dio_cartas = self.definir_siguiente(id_jug_dio_cartas)

	def intercambiar_cartas(self, nro_mano):
		"""Antes de hacer la primer jugada se pasan 3 cartas entre los rivales.
		En la primer mano, las cartas se pasan al jugador de la izquierda; en la
		segunda al jugador de la derecha; en la tercera al jugador del frente y
		en la cuarta no se pasan cartas. A partir de la quinta mano, se repite el
		mismo ciclo.
		El metodo debe primero pedirle las 3 cartas a pasar a cada oponente y luego
		entregarle las cartas que le fueron pasadas."""
		if (nro_mano > 26) or (nro_mano < 1):
			#El nro_mano no puede exceder las 25 manos ya que es el limite
			#logico que tiene el juego
			raise Exception("El numero de mano excede eL LIMITE !!!")

		if not(nro_mano in NUM_MANO_SIN_INTERCAMBIO):
			cartas_a_pasar = []
			for id_jugador in range(4):#id jugador va desde 0 a 3 
				#Pedimos las tres cartas a los cuatro jugadores
				cartas = self.jugadores[id_jugador].devolver_cartas_a_pasar(id_jugador)
				cartas_a_pasar.append(cartas)

			id_jug_dio_cartas = 0
			#Se realiza el intercambio dependiendo del numero de mano
			if nro_mano in NUM_MANO_INTERC_AGUJ_RLOJ:
				#Intercambiamos en el orden de las agujas del reloj
				id_jug_recibe = 1
			elif nro_mano in NUM_MANO_INTERC_CONTRA_AGUJ_RLOJ:
				#Intercambiamos en el orden contra las agujas del reloj
				id_jug_recibe = 3
			else:
				#Intercambiamos con el jugador de enfrente
				id_jug_recibe = 2
			self.Realizar_entrega_de_cartas(id_jug_recibe,id_jug_dio_cartas,cartas_a_pasar)
		else:
			#No realiza ninguna accion de pase de cartas
			pass

	def ganadores(self): 
		"""Una vez terminado el juego, devuelve la lista de ganadores.
		Son ganadores todos los es que hayan alcanzado el menor puntaje."""
		id_jugador = 0
		id_ganadores = []
		lista_ganadores = []
		min_puntaje = MAXPUNTAJE
		for puntaje in self.puntajes:
			if (puntaje < MAXPUNTAJE):
				if (puntaje == min_puntaje):
					id_ganadores.append(id_jugador)
					min_puntaje = puntaje
				elif (puntaje < min_puntaje):
					id_ganadores = [id_jugador]
					min_puntaje = puntaje
			id_jugador += 1
		for _id in id_ganadores:
			lista_ganadores.append(self.jugadores[_id])

		return lista_ganadores

	def jugar_mano(self, nro_mano):
		"""Realiza las 13 jugadas que corresponden a una mano completa."""
		corazon_jugado = False
		id_primero = self.identificar_jugador_que_inicia()
		
		# INICIO: Chequeos de trampa
		palos_faltantes = [[], [], [], []]
		cartas_en_mesa = []
		# FIN: Chequeos de trampa

		for nro_jugada in xrange(1, 13 + 1):
			print "Jugada %i" % nro_jugada
			print "Empieza %s" % self.jugadores[id_primero]
			print "****************************************"

			cartas_jugadas = self.realizar_jugada(nro_mano, nro_jugada, id_primero, corazon_jugado)

			corazon_jugado = self.hay_corazones(cartas_jugadas)

			id_perdedor = self.identificar_jugador_que_perdio(cartas_jugadas, id_primero)
			self.procesar_e_informar_resultado(cartas_jugadas, id_primero, id_perdedor)
			print
			print "Levanta %s" % self.jugadores[id_perdedor]
			chequeo = raw_input("Para continuar presione Enter..")
			print

			# INICIO: Chequeos de trampa
			if nro_jugada == 1 and not cartas_jugadas[0] == Carta(2, Carta.TREBOLES):
				raise Exception("El primer jugador no jugo el 2 de treboles""")
			if nro_jugada == 1 and (corazon_jugado or Carta(12, Carta.PICAS) in cartas_jugadas):
				raise Exception("Jugador jugo carta especial en primer juego""")
			for i in xrange(4):
				if cartas_jugadas[i].obtener_palo() in palos_faltantes[(i + id_primero) % 4]:
					raise Exception("El jugador %s dijo que no tenia %s" % (self.jugadores[(i + id_primero) % 4], Carta.PALOS[cartas_jugadas[i].obtener_palo()]))
			palo_jugada = cartas_jugadas[0].obtener_palo()
			for i in xrange(1, 4):
				if cartas_jugadas[i].obtener_palo() != palo_jugada and palo_jugada not in palos_faltantes[(i + id_primero) % 4]:
					palos_faltantes[(i + id_primero) % 4].append(palo_jugada)
			for carta in cartas_jugadas:
				if carta in cartas_en_mesa:
					raise Exception("Alguien se matufio el %s" % carta)
				cartas_en_mesa.append(carta)
			# FIN: Chequeos de trampa

			id_primero = id_perdedor #El id del primero pasa a ser el id del perdedor

	def jugar(self):
		"""Juega una partida completa de Corazones."""
		nro_mano = 1
		while not self.termino():
			print "Mano %d" % nro_mano
			self.barajar()
			self.intercambiar_cartas(nro_mano)
			self.jugar_mano(nro_mano)
			self.calcular_puntajes()
			self.imprimir_puntajes()

			nro_mano += 1
			
	def desactivar_muestreo_de_cartas_intercambiadas(self):
		"""Deshabilita la posibilidad de ver las cartas intercambiadas"""
		self.mostrar_intercambiadas = False
	
	def modificar_puntajes(self,nuevo_puntaje):
		"""Modifica los puntajes que ya existen
		para realizar las pruebas"""
		self.puntajes = nuevo_puntaje
	
	def devolver_lista_de_jugadores(self):
		"""Devuelve la lista de jugadores"""
		return self.jugadores
	
	def modificar_cartas_levantadas(self,nuevas_cartas):
		"""Recibe por parametro una lista de listas de cartas 
		que asigna a el atributo cartas levantadas"""
		self.cartas_levantadas = nuevas_cartas
	
	def devolver_puntajes(self):
		"""Devuelve los puntajes"""
		return self.puntajes