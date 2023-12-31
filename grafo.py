import heapq  # librería para implementar colas con prioridad
import networkx as nx
from bst import BST
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self):
        self.ciudades = [] #almacenamos las cuidades
        self.matriz_adyacente = [] #almacenamos la matriz de adyacencia para las conexiones entre ciudades
        self.registro_distancias = BST() #mantener un registro ordenado de las distancias entre ciudades

    def agregar_ciudad(self, ciudad):
        '''Método para agregar una nueva ciudad al grafo'''
        self.ciudades.append(ciudad) # Añadimos una nueva ciudad al grafo
        for fila in self.matriz_adyacente:  # Añadimos una nueva columna a la matriz de adyacencia
            fila.append(0)
        self.matriz_adyacente.append([0] * len(self.ciudades)) # Añadimos una nueva fila de ceros  a la matriz de adyacencia


    def agregar_conexion(self, ciudad1, ciudad2, distancia):
        '''Método para agregar una nueva conexión entre dos ciudades'''
        # Añade una conexión entre dos ciudades con su respectiva distancia
        indice_ciudad1 = self.ciudades.index(ciudad1)
        indice_ciudad2 = self.ciudades.index(ciudad2)
        self.matriz_adyacente[indice_ciudad1][indice_ciudad2] = distancia
        self.matriz_adyacente[indice_ciudad2][indice_ciudad1] = distancia 
         # Actualiza el registro ordenado de distancias en el BST
        self.registro_distancias.insert(distancia, (ciudad1, ciudad2))

    def mostrar_grafo(self):
        '''Método para mostrar el grafo en forma de matriz de adyacencia'''
        print("Ciudades:", self.ciudades)
        print("Matriz de Adyacencia:")
        for fila in self.matriz_adyacente:
            print(fila)
        print("Registro de Distancias:")
        self.registro_distancias.display()
    
    def visualizar_grafo(self):
        '''Método para visualizar el grafo'''
        G = nx.Graph()

        # Agregamos nodos al grafo
        G.add_nodes_from(self.ciudades)

        # y aristas
        for i in range(len(self.ciudades)):
            for j in range(i+1, len(self.ciudades)):
                distancia = self.matriz_adyacente[i][j]
                if distancia > 0:
                    G.add_edge(self.ciudades[i], self.ciudades[j], weight=distancia)

        # Para visualizar el grafo
        pos = nx.spring_layout(G)  # Puedes ajustar el diseño según tus preferencias
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw(G, pos, with_labels=True)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()


    def ruta_mas_corta(self, ciudad1, ciudad2):
        '''Método para encontrar la ruta más corta entre dos ciudades'''

        # Creamos un diccionario para almacenar las distancias mínimas desde el origen a cada ciudad
        distancias = {ciudad: float("inf") for ciudad in self.ciudades}
        distancias[ciudad1] = 0  # la distancia inicial es 0 (desde el origen a sí mismo)
        padres = {ciudad: None for ciudad in self.ciudades} # diccionario para almacenar los padres de cada ciudad

        # Cola de prioridad para almacenar las ciudades ordenadas por su distancia mínima
        cola_prioridad = [(0, ciudad1)]

        while len(cola_prioridad) > 0:  # extraemos la ciudad con la distancia mínima
            distancia_ciudad, ciudad_actual = heapq.heappop(cola_prioridad)

            # si la distancia extraída es mayor a la almacenada en el diccionario, no nos sirve y pasa a la siguiente iteración
            if distancia_ciudad > distancias[ciudad_actual]:
                continue
            
            # si la distancia extraída es menor o igual a la almacenada en el diccionario, actualizamos la distancia y el padre
            # Recorremos las ciudades adyacentes a la ciudad actual
            for ciudad_adyacente in self.ciudades:
                distancia_adyacente = self.matriz_adyacente[self.ciudades.index(ciudad_actual)][self.ciudades.index(ciudad_adyacente)]
                
                
                if distancia_adyacente > 0:  # nos aseguramos de que la distancia_adyacente sea mayor o igual a cero
                    if distancias[ciudad_adyacente] > distancia_ciudad + distancia_adyacente:
                        distancias[ciudad_adyacente] = distancia_ciudad + distancia_adyacente
                        padres[ciudad_adyacente] = ciudad_actual
                        heapq.heappush(cola_prioridad, (distancias[ciudad_adyacente], ciudad_adyacente))

        # Reconstruimos la ruta desde el origen a la ciudad destino
        ruta = []
        ciudad_actual = ciudad2
        while ciudad_actual != ciudad1 and ciudad_actual is not None:
            ruta.insert(0, ciudad_actual)
            ciudad_actual = padres[ciudad_actual]

        # Si no hay ruta, la ciudad destino no es alcanzable desde la ciudad origen
        if ciudad_actual is None:
            return None, float('inf')

        # Agregamos la ciudad origen al inicio de la ruta, solo si la distancia total es finita
        if distancias[ciudad2] < float('inf'):
            ruta.insert(0, ciudad1)

        # Devolvemos la ruta y la distancia total
        return ruta, distancias[ciudad2]


    def arbol_recubrimiento_minimo(self):
        '''Método para encontrar el Árbol de Recubrimiento Mínimo del grafo'''
        # Diccionario para almacenar las distancias mínimas desde el origen a cada ciudad
        distancias = {ciudad: float("inf") for ciudad in self.ciudades}
        distancias[self.ciudades[0]] = 0
        # Cola de prioridad para almacenar las ciudades ordenadas por distancia mínima 
        cola_prioridad = [(0, self.ciudades[0], None)]

        # Conjunto para almacenar las aristas seleccionadas en el Árbol de Recubrimiento Mínimo
        aristas_seleccionadas = set()
        while cola_prioridad: 
            distancia_actual, ciudad_actual, ciudad_padre = heapq.heappop(cola_prioridad)
            # si ya hemos procesado esta ciudad
            if distancia_actual > distancias[ciudad_actual]:
                continue  # pasamos a la siguiente iteración
            
            # Agregamos la arista al árbol de recubrimiento mínimo
            if ciudad_padre:
                aristas_seleccionadas.add((ciudad_padre, ciudad_actual))

            # Actualizamos las distancias para las ciudades adyacentes
            for ciudad_adyacente, distancia_adyacente in enumerate(self.matriz_adyacente[self.ciudades.index(ciudad_actual)]):
                if distancia_adyacente >= 0:
                    nueva_distancia = distancia_actual + distancia_adyacente
                    if nueva_distancia < distancias[self.ciudades[ciudad_adyacente]]:
                        distancias[self.ciudades[ciudad_adyacente]] = nueva_distancia
                        heapq.heappush(cola_prioridad, (nueva_distancia, self.ciudades[ciudad_adyacente], ciudad_actual))

        # Devolvemos el conjunto de aristas seleccionadas
        return aristas_seleccionadas
