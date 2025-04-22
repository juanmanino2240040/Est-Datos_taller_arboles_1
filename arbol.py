# ========================================================================
# By: Juan Niño 2240040 - Franchesco Hernandez 2240032 - Estructuras Datos
# Name: Arboles con Listas simplemente enlazadas
# ========================================================================

# Clase Nodo


class Nodo:
	def __init__(self, data):
		self.data = data
		self.hijo = None
		self.hermano = None
	
	def toString(self):
		return self.data.string()
  	
# CLase Lista enlazada simple modificada
class Arbol:
	def __init__(self):
		self.raiz = None
  
  	# Lista Vacia
	def vacio(self):
		if self.cabeza == None:
			print("Está vacia")
		else:
			print("Lista no vacia")
 
 	# Insertar hijos a la raiz
	def agregarHijo(self, data):
		if self.raiz is None:
			nuevo_nodo = Nodo(data)
			self.raiz = nuevo_nodo
			return
		self.agregarHijoNodo(self.raiz,data)

	def agregarHijoNodo(self, nodo, data):
		nuevo_nodo = Nodo(data)
		if nodo.hijo is None:
			nodo.hijo = nuevo_nodo
			return
		temp = nodo.hijo
		while(True):
			if temp.hermano is None:
				temp.hermano = nuevo_nodo
				return
			temp = temp.hermano

	def getPeso(self):
		if self.raiz is None:
			return 0
		return self.getPesoNodo(self.raiz)

	def getPesoNodo(self,nodo):
		if nodo.hijo is None:
			return 1
		peso = 1
		temp = nodo.hijo
		while(True):
			peso += self.getPesoNodo(temp)
			if temp.hermano is None:
				return peso
			temp = temp.hermano

	def getOrden(self):
		if self.raiz is None:
			return 0
		return self.getOrdenNodo(self.raiz)

	def getOrdenNodo(self,nodo):
		if nodo.hijo is None:
			return 0
		temp = nodo.hijo
		cont = 0
		while True:
			cont += 1
			if temp.hermano is None:
				break
			temp = temp.hermano
		temp = nodo.hijo
		while True:
			orden = self.getOrdenNodo(temp)
			if orden > cont:
				cont = orden
			if temp.hermano is None:
				return cont
			temp = temp.hermano

	def getAltura(self):
		if self.raiz is None:
			return 0
		return self.getAlturaNodo(self.raiz)

	def getAlturaNodo(self,nodo):
		if nodo.hijo is None:
			return 1
		temp = nodo.hijo
		if temp.hermano == None:
			return self.getAlturaNodo(temp)+1
		t = self.getAlturaNodo(temp)
		while(True):
			h = self.getAlturaNodo(temp.hermano)
			if h > t:
				t = h 
			if temp.hermano.hermano is None:
				return t+1
			temp = temp.hermano

arbol = Arbol()
arbol.agregarHijo(input('Ingrese el dato del nodo raíz: '))
select=arbol.raiz
while(True):
	selec = input(f'\nNodo seleccionado: {select.data}\n1. Agregar hijo al nodo seleccionado.\n2. Seleccionar un hijo del nodo seleccionado.\n3. Volver a la raiz.\n4. Peso, altura y orden del árbol.\n5. Salir.\n\nElija una opción: ')
	if selec == "1":
		arbol.agregarHijoNodo(select,input("Ingrese el dato del nodo hijo: "))
	elif selec == "2":
		print(f"\nNodos hijos del nodo {select.data}:\n")
		if select.hijo is None:
			print("No hay hijos")
		else:
			temp = select.hijo
			cont=0
			while True:
				cont+=1
				print(f"{cont}. {temp.data}")
				if temp.hermano is None:
					break
				temp=temp.hermano
			elec = int(input("\nEscriba el número del nodo a elegir: "))
			temp = select.hijo
			cont=0
			while True:
				cont+=1
				if cont == elec:
					select = temp
				if temp.hermano is None:
					break
				temp=temp.hermano
	elif selec == "3":
		select = arbol.raiz
	elif selec == "4":
		print("\nPeso del arbol: ", arbol.getPeso())
		print("Orden del arbol: ", arbol.getOrden())
		print("Altura del arbol: ", arbol.getAltura())
	elif selec == "5":
		print("\n\nSaliendo del programa...\n")
		break
