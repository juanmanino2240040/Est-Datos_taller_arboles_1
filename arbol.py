# ===========================================
# By: Juan Niño 2240040- Franchesco Hernandez 2240032- Estructuras Datos
# Name: Arboles con Listas Doblemente Enlazadas 
# ===========================================

# Clase Nodo
class Nodo:
	def __init__(self, data):
		self.data = data
		self.siguiente = None

# CLase Listas enlazada simple
class Hijo:
	def __init__(self):
		self.cabeza = None
  
  	# Lista Vacia
	def vacio(self):
		if self.cabeza == None:
			print("Está vacia")
		else:
			print("Lista no vacia")

	# Agregar al inicio
	def agregarInicio(self, data):
		nuevo_nodo = Nodo(data)
		if self.cabeza is None:
			self.cabeza = nuevo_nodo
			return
		else:
			nuevo_nodo.siguiente = self.cabeza
			self.cabeza = nuevo_nodo

	# Imprimir lista
	def imprimirLista(self):
		print('[', end="")
		if self.cabeza == None:
			print(' ]')
			return
		temp = self.cabeza
		while( True ):
			print("",temp.data, end="")
			if (temp.siguiente == None):
				break
			temp = temp.siguiente
			print(" ,", end="")
		print(' ]')
  
	# Buscar último
	def ultimo(self):
		temp = self.cabeza
		while (True):
			if temp.siguiente == None:
				return temp
			temp = temp.siguiente
   
	# Insertar al final
	def agregarFinal(self,data):
		nuevo_nodo = Nodo(data)
		if self.cabeza is None:
			self.cabeza = nuevo_nodo
			return
		temp = self.ultimo()
		temp.siguiente = nuevo_nodo

	# Eliminar primero
	def eliminarInicio(self):
		self.cabeza = self.cabeza.siguiente

	# Eliminar último
	def eliminarUltimo(self):
		if (self.cabeza.siguiente == None):
			self.cabeza = None
			return
		temp = self.cabeza
		while( True ):
			if temp.siguiente.siguiente == None:
				temp.siguiente = None
				return
			temp = temp.siguiente

	# Buscar un elemento por su valor
	def buscar(self,data):
		temp = self.cabeza
		while ( True ):
			if temp.data == data:
				return True
			if temp.siguiente == None:
				return False
			temp = temp.siguiente

    # Insertar valor data antes del valor x
	def insertarAntes(self,data,x):
		if not self.buscar(x) :
			print('El valor', data, 'no está en la lista')
			return
		if self.cabeza.data == x:
			self.agregarInicio(data)
			return
		nuevo_nodo = Nodo(data)
		temp = self.cabeza
		while ( True ):
			if temp.siguiente.data == x:
				nuevo_nodo.siguiente = temp.siguiente
				temp.siguiente = nuevo_nodo
				return
			temp = temp.siguiente

	# Insertar valor data despues del valor x
	def insertarDespues(self,data,x):
		if not self.buscar(x) :
			print('El valor', data, 'no está en la lista')
			return
		nuevo_nodo = Nodo(data)
		temp = self.cabeza
		while ( True ):
			if temp.data == x:
				nuevo_nodo.siguiente = temp.siguiente
				temp.siguiente = nuevo_nodo
				return
			temp = temp.siguiente

	# Contar la cantidad de elementos
	def contar(self):
		temp = self.cabeza
		cont = 1
		while ( True ):
			if temp.siguiente == None:
				return cont
			cont += 1
			temp = temp.siguiente
		
  
  
  	
# CLase Listas enlazada simple
class Arbol:
	def __init__(self):
		self.raiz = None
  
  	# Lista Vacia
	def vacio(self):
		if self.cabeza == None:
			print("Está vacia")
		else:
			print("Lista no vacia")

	# Agregar la raiz del arbol
	def agregarRaiz(self, data):
		nuevo_nodo = Nodo(data)
		self.raiz=nuevo_nodo

 
 	# Insertar al final
	def agregarHijo(self, data):
		nuevo_nodo = Nodo(data)
		if self.cabeza is None:
			self.cabeza = nuevo_nodo
			return
		temp = self.ultimo()
		temp.siguiente = nuevo_nodo
  
	# Imprimir lista
	def toStringPreOrden(self):
		
	def toStringPosOrden(self):
	def toStringInOrden(self):
	def toStringPorNiveles(self):
   


	# Eliminar primero
	def eliminarInicio(self):
		self.cabeza = self.cabeza.siguiente

	# Eliminar último
	def eliminarUltimo(self):
		if (self.cabeza.siguiente == None):
			self.cabeza = None
			return
		temp = self.cabeza
		while( True ):
			if temp.siguiente.siguiente == None:
				temp.siguiente = None
				return
			temp = temp.siguiente

	# Buscar un elemento por su valor
	def buscar(self,data):
		temp = self.cabeza
		while ( True ):
			if temp.data == data:
				return True
			if temp.siguiente == None:
				return False
			temp = temp.siguiente

    # Insertar valor data antes del valor x
	def insertarAntes(self,data,x):
		if not self.buscar(x) :
			print('El valor', data, 'no está en la lista')
			return
		if self.cabeza.data == x:
			self.agregarInicio(data)
			return
		nuevo_nodo = Nodo(data)
		temp = self.cabeza
		while ( True ):
			if temp.siguiente.data == x:
				nuevo_nodo.siguiente = temp.siguiente
				temp.siguiente = nuevo_nodo
				return
			temp = temp.siguiente

	# Insertar valor data despues del valor x
	def insertarDespues(self,data,x):
		if not self.buscar(x) :
			print('El valor', data, 'no está en la lista')
			return
		nuevo_nodo = Nodo(data)
		temp = self.cabeza
		while ( True ):
			if temp.data == x:
				nuevo_nodo.siguiente = temp.siguiente
				temp.siguiente = nuevo_nodo
				return
			temp = temp.siguiente

	# Contar la cantidad de elementos
	def contar(self):
		temp = self.cabeza
		cont = 1
		while ( True ):
			if temp.siguiente == None:
				return cont
			cont += 1
			temp = temp.siguiente
