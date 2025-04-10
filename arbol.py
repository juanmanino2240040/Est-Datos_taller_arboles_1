# ===========================================
# By: Juan Niño 2240040- Franchesco Hernandez 2240032- Estructuras Datos
# Name: Arboles con Listas Doblemente Enlazadas 
# ===========================================

# Clase Nodo
class Nodo:
	def __init__(self, data):
		self.data = data
		self.prev=None
		self.next = None

# CLase Listas Circular Doblemente Enlazada 
class ListaDE:
	def __init__(self):
		self.cabeza = None
		self.cola = None
  
  	# Lista Vacia
	def vacio(self):
		if self.cabeza == None:
			print("Está vacia")
		else:
			print("Lista no vacia")
	def void(self):
		if self.cabeza == None:
			return False
		else:
			return True

	# Agregar al inicio // Reescribir self.cabeza
	def agregarInicio(self, data):
		nuevo_nodo = Nodo(data)


	       # Agregar al final
	def agregarFinal(self, data):
		nuevo_nodo = Nodo(data)

   
   #  Eliminar nodo por su data
	def Delete(self, data):
		temp_nodo=self.cabeza
		while temp_nodo.data != data and temp_nodo != self.cola:
			antes_nodo=temp_nodo
			temp_nodo=temp_nodo.next

    

   
	#  Imprimir todos los elementos de la lista
	def printPreOrden(self):
    def printInOrden(self):
    def printPostOrden(self):


		

       
				
			

# Crear la lista enlazada
mi_lista = ListaDE()

# Agregar elementos
mi_lista.agregarInicio(20)
mi_lista.agregarInicio(10)
mi_lista.agregarFinal(30)
mi_lista.agregarFinal(40)

# Imprimir la lista
mi_lista.printLista()

# Imprimir la lista después de modificaciones
mi_lista.printLista()

# Eliminar elementos
mi_lista.Delete(10)
mi_lista.Delete(140400)

# Imprimir la lista final
mi_lista.printLista ()