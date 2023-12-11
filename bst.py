class NodoBST:
    def __init__(self, distancia, ciudades):
        self.distancia = distancia
        self.ciudades = ciudades
        self.izquierda = None
        self.derecha = None


class BST:
    def __init__(self):
        self.root = None #arbol binario de busqueda

    def insert(self, distancia, ciudades):
        # Inserta un nuevo nodo en el árbol con una clave (distancia) y un valor (ciudades)
        self.root = self._insert(distancia, ciudades, self.root)

    def _insert(self, distancia, ciudades, nodo):
        # Función auxiliar para insertar un nodo en el árbol
        if nodo is None:
            return NodoBST(distancia, ciudades)
        if distancia < nodo.distancia:
            nodo.izquierda = self._insert(distancia, ciudades, nodo.izquierda)
        elif distancia > nodo.distancia:
            nodo.derecha = self._insert(distancia, ciudades, nodo.derecha)
        return nodo
    
    def display(self):
        # Muestra el árbol en orden
        self._display(self.root)

    def _display(self, nodo):
        if nodo is not None:
            self._display(nodo.izquierda)
            print(f'Distancia: {nodo.distancia}, Ciudades: {nodo.ciudades}')
            self._display(nodo.derecha)