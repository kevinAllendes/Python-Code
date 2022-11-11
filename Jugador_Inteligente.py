from Carta import Carta
from Jugador import Jugador

Q_PICAS=Carta(12,Carta.PICAS)
TREBOLES_2=Carta(2,Carta.TREBOLES)
PICAS_1=Carta(1,Carta.PICAS)
PICAS_13=Carta(13,Carta.PICAS)

class Jugador_Inteligente(Jugador):
	
	def recibir_carta(self, carta):
		"""Recibe una carta y la agrega a su mano"""
		self.ordenar_cartas(carta)

	def es_primero(self):
		"""Devuelve True si el usuario tiene el 2 de treboles"""
		return TREBOLES_2 in self.mano
	
	def ordenamiento_de_ases(self):
		"""Ordena las cartas "As" de la mano poniendolos
		en la ultima posicion de la misma"""
		for carta in self.mano:
			if carta.obtener_numero()==1:
				self.mano.append(carta)
				self.mano.remove(carta)

	def buscar_carta(self,lista_de_cartas,carta):
		"""Busca la carta pasada por parametro en la mano 
		y si la misma es encontrada se saca de la mano y
		se la agrega a la lista de cartas pasada tambien
		por parametro"""
		if carta in self.mano:
			self.mano.remove(carta)
			lista_de_cartas.append(carta)
		
	def devolver_cartas_a_pasar(self, id_jugador):
		"""Antes de comenzar la mano, retira de su mano y devuelve 3 cartas para
		pasarle al oponente con id id_jugador"""

		self.ordenamiento_de_ases()
		cartas_a_pasar=[]
		self.buscar_carta(cartas_a_pasar,Q_PICAS)
		self.buscar_carta(cartas_a_pasar,TREBOLES_2)
		self.buscar_carta(cartas_a_pasar,PICAS_1)
		if len(cartas_a_pasar)<3:
			self.buscar_carta(cartas_a_pasar,PICAS_13)
		
		for carta in self.mano[::-1]:
			if carta.obtener_palo()==Carta.CORAZONES:
				if (carta.obtener_numero()>8 or carta.obtener_numero()==1) and len(cartas_a_pasar)<3:
					cartas_a_pasar.append(carta)
					self.mano.remove(carta)
					
		for carta in self.mano[::-1]:
				if len(cartas_a_pasar)<3:
					cartas_a_pasar.append(carta)
					self.mano.remove(carta)
				else:
					return cartas_a_pasar
		
	def recibir_cartas_pasadas(self, id_jugador, cartas):
		"""Antes de comenzar la mano y despues de haber devuelto sus cartas, recibe
		3 cartas del oponente con id id_jugador"""
		for carta in cartas:
			self.ordenar_cartas(carta)

	def jugar_carta(self, nro_mano, nro_jugada, cartas_jugadas, corazon_jugado):
		"""Saca una carta de su mano y la devuelve jugandola. Recibe el numero de
		mano, el numero de jugada, las cartas ya jugadas en la mesa en esa jugada
		y un booleano que indica si ya se jugaron corazones en las jugadas previas.
		Si ya hay cartas_jugadas y el jugador posee una carta del palo de la primer
		carta debe jugarla obligatoriamente.
		Si nro_jugada es 1 y no hay cartas_jugadas, el jugador debe jugar el 2 de
		treboles.
		Si nro_jugada es 1 el jugador no puede jugar ni un corazon ni la Q de picas.
		Si no hay cartas_jugadas y corazon_jugado es False el jugador no podra jugar
		un corazon salvo que no tenga otra carta."""
		
		self.ordenamiento_de_ases()
		
		if nro_jugada==1 and len(cartas_jugadas)==0: 
			self.mano.remove(TREBOLES_2)
			return TREBOLES_2
		
		if len(cartas_jugadas)==0:	#si el jugador es el primero
			return self.primer_jugador(nro_jugada,corazon_jugado)
		
		primera_carta=cartas_jugadas[0]
		
		if len(cartas_jugadas)==3: 	#si el jugador es el ultimo
			return self.ultimo_jugador(cartas_jugadas,primera_carta,corazon_jugado,nro_jugada)
		
		if nro_jugada<3: 			#si el jugador es el segundo o el tercero
		
			privilegiar_corazones=True
			carta=self.obtener_carta_mas_chica(primera_carta,cartas_jugadas,privilegiar_corazones) #obtiene la carta mas chica de los corazones
			if carta:
				return carta
			
			for carta in self.mano[::-1]:
				if carta.obtener_palo()==primera_carta.obtener_palo():
					if carta.obtener_palo()==Carta.PICAS and carta.obtener_numero()<12 and carta.obtener_numero()<>1:
						return self.borrar_carta_de_mano(carta)
					elif carta.obtener_palo()==Carta.DIAMANTES or carta.obtener_palo()==Carta.TREBOLES:
						return self.borrar_carta_de_mano(carta)

			for carta in self.mano[::-1]: #juego la carta mas grande ya que no tenia mas chica, de igual palo que la priemra carta
				if carta.obtener_palo()==primera_carta.obtener_palo():
					return self.borrar_carta_de_mano(carta)
				
			#ya que no hay cartas del mismo palo que la primera carta....
			return self.obtener_cartas_especiales_o_mayores(corazon_jugado,nro_jugada)
		
		else: #nro_jugada >= 3 
		
			privilegiar_corazones=False
			carta= self.obtener_carta_mas_chica(primera_carta,cartas_jugadas,privilegiar_corazones) #obtiene la carta mas chica
			if carta:
				return carta
								
			for carta in self.mano: #juega alguna de las cartas que no jugo antes
				if not carta==Q_PICAS and carta.obtener_palo()==primera_carta.obtener_palo():
					return self.borrar_carta_de_mano(carta)
			
			if Q_PICAS in self.mano and primera_carta.obtener_palo()==Carta.PICAS:
				self.mano.remove(Q_PICAS)
				return Q_PICAS
				
			#ya que no hay cartas del mismo palo que la primera carta....
			return self.obtener_cartas_especiales_o_mayores(corazon_jugado,nro_jugada)
			
	def ordenar_cartas(self,carta_pasada):
		"""Ordena las cartas dentro de la mano de cartas"""
		cont=1
		for carta in self.mano:
			if carta.obtener_numero()>carta_pasada.obtener_numero() or (carta.obtener_numero()==carta_pasada.obtener_numero() and carta.obtener_palo()>carta_pasada.obtener_palo()):
				self.mano.insert(cont-1,carta_pasada)
				return
			cont+=1
		if not carta_pasada in self.mano:
			self.mano.append(carta_pasada)
					
	def ultimo_jugador(self,cartas_jugadas,primera_carta,corazon_jugado,nro_jugada):
		""" Se recorre la lista carta_jugadas y se procede en orden de prioridad:
		a)	Si alguna de esas cartas es un corazon o la Q de Picas se recorre la mano de 
		cartas y se devuelve la carta de valor menor a la que se haya jugado primero en la 
		mano de igual palo que la primera carta jugada.
		b)	En caso contrario se devuelve la carta de valor mayor a la que se haya jugado 
		primero en la mano, de igual palo que la primera carta jugada.
		c)	En caso que no haya cartas del mismo palo, se llama a la funcion 
		obtener_cartas_especiales_o_mayores """
		
		tirar_carta_chica=False
		for carta in cartas_jugadas: #me fijo si hay alguna carta de corazones o la q de picas
			if carta.obtener_palo()==Carta.CORAZONES or carta==Q_PICAS:
				privilegiar_corazones=False
				carta= self.obtener_carta_mas_chica(primera_carta,cartas_jugadas,privilegiar_corazones) #juego la carta mas chica
				if carta:
					return carta
		
		for carta in self.mano[::-1]: #tiro cualquier carta mas grande del mismo palo que la primera carta que no sea el q de picas
			if not carta==Q_PICAS and carta.obtener_palo()==primera_carta.obtener_palo():
					return self.borrar_carta_de_mano(carta)
		
		if primera_carta.obtener_palo()==Carta.PICAS and Q_PICAS in self.mano:
			return self.borrar_carta_de_mano(Q_PICAS)
						
		#ya que no hay cartas del mismo palo que la primera carta....
		return self.obtener_cartas_especiales_o_mayores(corazon_jugado,nro_jugada)
	
	def primer_jugador(self,nro_jugada,corazon_jugado):
		"""
		*Si el numero de jugada es 1 o 2 se procede en orden de prioridad:
			a) Se recorre inversamente la mano de cartas, y se borra y devuelve de la mano 
			la primera carta que no sea de corazones ni que sea la Q de Picas, ni mayor a la misma.
			b) En caso de que se encuentren en la mano se devuelve el As de Picas o la K de Picas.
			c) En caso de no haber devuelto ninguna carta, se devuelve la primera carta que tenga en
			la mano menos la Q de picas. (Que sera un corazon).
		*Si el numero de jugada es mayor a 2, se procede en orden de prioridad:
			a) Si ya se jugo un corazon se recorre la mano de cartas y se devuelve la carta con menor valor,
			exceptuando  los corazones con valor mayor a 5 y la Q de Picas.
			b) Si no se jugo ningun corazon tambien se recorre la mano de cartas y se devuelve  la carta con 
			menor valor que no sea un corazon ni la Q de Picas.
			c) Se recorre la mano de cartas y se devuelve la primera carta de la mano, exceptuando la Q de Picas.
			d) Si la unica carta que no se jugo de la mano fue la Q de Picas, la misma se devuelve.
		"""
		if nro_jugada<3:
			for carta in self.mano[::-1]: #juego la mas grande que no sea de corazones ni la q de picas
				if not carta.obtener_palo()==Carta.CORAZONES:
					if carta.obtener_palo()==Carta.PICAS:
						if carta.obtener_numero()>11 or carta.obtener_numero()==1: 
							pass
						else:
							return self.borrar_carta_de_mano(carta)
					else:

						return self.borrar_carta_de_mano(carta)
			
			#En orden se fija si estan estas carta y las devuelve
			
			carta=self.devolver_carta_en_mano(PICAS_1) 
			if carta:
				return carta
			carta=self.devolver_carta_en_mano(PICAS_13) 
			if carta:
				return carta
			carta=self.devolver_carta_en_mano(Q_PICAS) 
			if carta:
				return carta
			for carta in self.mano: #si nada mas hay corazones 
				return self.borrar_carta_de_mano(carta)
				
		else: #si nro_jugada >= 3
			for carta in self.mano: #juego la mas chica que no sea de corazon mayor a 5 
				if corazon_jugado and not carta==Q_PICAS and not (carta.obtener_palo()==Carta.CORAZONES and (carta.obtener_numero()==1 or carta.obtener_numero()>5)):
						return self.borrar_carta_de_mano(carta)
				elif not carta==Q_PICAS and carta.obtener_palo()<>Carta.CORAZONES:
					
					return self.borrar_carta_de_mano(carta)
			
			if corazon_jugado:
				for carta in self.mano:
					if carta.obtener_palo()==Carta.CORAZONES:
						return self.borrar_carta_de_mano(carta)
							
			carta=self.devolver_carta_en_mano(Q_PICAS) #se fija si esta la q de picas
			if carta:
				return carta
			for carta in self.mano:
				return self.borrar_carta_de_mano(carta)
				
	def devolver_carta_en_mano(self,carta):
		"""Si la carta ingresada por parametro
		no se encuentra en la mano devuelve None,
		caso contrario borra la carta de la mano
		de cartas y la devuelve"""
		if carta in self.mano:
			return self.borrar_carta_de_mano(carta)
		else:
			return None
	
	def obtener_carta_mas_chica(self,primera_carta,cartas_jugadas,privilegiar_corazones):
		"""Devuelve la carta de mayor valor que haya en la mano y de menor valor que las
		cartas jugadas (siempre y cuando sean del mismo palo). No devuelve los Ases.
		En caso de no encontrar cartas que cumplan con la condicion devuelve None"""
		
		for carta in self.mano[::-1]:	
			if carta.obtener_palo()==primera_carta.obtener_palo():
				for carta_mazo in cartas_jugadas:
					if carta_mazo.obtener_palo()==carta.obtener_palo() and carta.obtener_numero()<>1 and carta.obtener_numero()<carta_mazo.obtener_numero():
						if privilegiar_corazones:
							if carta.obtener_palo()==Carta.CORAZONES:
								return self.borrar_carta_de_mano(carta)
						else:
							return self.borrar_carta_de_mano(carta)
		return None
		
	def borrar_carta_de_mano(self,carta):
		"""Borra la carta pasado por parametro de la mano de cartas y
		la devuelve"""
		carta_aux=carta
		self.mano.remove(carta)
		return carta_aux

	def obtener_cartas_especiales_o_mayores(self,corazon_jugado,nro_jugada): 
		"""Devuelve si se encuentra en la mano: en primer lugar
		el q de picas, en segundo lugar algun corazon mayor a 5, y 
		en ultimo lugar cualquier carta priorizando las de mayor valor"""
		
		if Q_PICAS in self.mano and corazon_jugado: #juego q de picas
			self.mano.remove(Q_PICAS)
			return Q_PICAS	
		for carta in self.mano[::-1]: #juego algun corazon mayor a 5
			if carta.obtener_palo()==Carta.CORAZONES and (carta.obtener_numero()>5 or carta.obtener_numero()==1) and nro_jugada<>1:
				return self.borrar_carta_de_mano(carta)			
		for carta in self.mano[::-1]: #juego cualquier otra que sea grande
			if (carta.obtener_palo()==Carta.CORAZONES or carta==Q_PICAS) and nro_jugada==1:
				pass
			else:
				return self.borrar_carta_de_mano(carta)
		
	def obtener_mano_de_cartas(self):
		"""Devuelve las cartas que el jugador posee en la mano """
		return self.mano[::]