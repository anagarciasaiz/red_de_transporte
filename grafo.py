import heapq
from bst import BST

class Grafo:
    def __init__(self):
        self.ciudades = [] #almacenamos las cuidades
        self.matriz_adyacente = [] #almacenamos la matriz de adyacencia para las conexiones entre ciudades
        self.registro_distancias = BST() #mantener un registro ordenado de las distancias entre ciudades

    def agregar_ciudad(self, ciudad):
        self.ciudades.append(ciudad) # Añadimos una nueva ciudad al grafo
        for fila in self.matriz_adyacente:  # Añadimos una nueva columna a la matriz de adyacencia
            fila.append(0)
        self.matriz_adyacente.append([0] * len(self.ciudades)) # Añadimos una nueva fila de ceros  a la matriz de adyacencia


    def agregar_conexion(self, ciudad1, ciudad2, distancia):
        # Añade una conexión entre dos ciudades con su respectiva distancia
        indice_ciudad1 = self.ciudades.index(ciudad1)
        indice_ciudad2 = self.ciudades.index(ciudad2)
        self.matriz_adyacente[indice_ciudad1][indice_ciudad2] = distancia
        self.matriz_adyacente[indice_ciudad2][indice_ciudad1] = distancia 
         # Actualiza el registro ordenado de distancias en el BST
        self.registro_distancias.insert(distancia, (ciudad1, ciudad2))

    def mostrar_grafo(self):
        # Muestra el grafo en forma de matriz de adyacencia
        print("Ciudades:", self.ciudades)
        print("Matriz de Adyacencia:")
        for fila in self.matriz_adyacente:
            print(fila)
        print("Registro de Distancias:")
        self.registro_distancias.display()
    

    def ruta_mas_corta(self, ciudad1, ciudad2):
        # Diccionario para almacenar las distancias mínimas desde el origen a cada ciudad
        distancias = {ciudad: float("inf") for ciudad in self.ciudades}
        distancias[ciudad1] = 0  # La distancia desde el origen a sí mismo es 0
        padres = {ciudad: None for ciudad in self.ciudades} # Diccionario para almacenar los padres de cada ciudad

        # Cola de prioridad para almacenar las ciudades ordenadas por su distancia mínima
        cola_prioridad = [(0, ciudad1)]

        while len(cola_prioridad) > 0:
            # Extrae la ciudad con la distancia mínima
            distancia_ciudad, ciudad_actual = heapq.heappop(cola_prioridad)

            # Si la distancia extraída es mayor a la almacenada en el diccionario, no nos sirve y pasa a la siguiente iteración
            if distancia_ciudad > distancias[ciudad_actual]:
                continue
            
            # si la distancia extraída es menor o igual a la almacenada en el diccionario, actualizamos la distancia y el padre
            # Recorremos las ciudades adyacentes a la ciudad actual
            for ciudad_adyacente in self.ciudades:
                distancia_adyacente = self.matriz_adyacente[self.ciudades.index(ciudad_actual)][self.ciudades.index(ciudad_adyacente)]
                
                # Verifica que la distancia_adyacente sea mayor o igual a cero
                if distancia_adyacente > 0:
                    # Si la distancia desde el origen a la ciudad adyacente es mayor a la distancia desde el origen a la ciudad actual + la distancia entre la ciudad actual y la adyacente
                    if distancias[ciudad_adyacente] > distancia_ciudad + distancia_adyacente:
                        distancias[ciudad_adyacente] = distancia_ciudad + distancia_adyacente
                        padres[ciudad_adyacente] = ciudad_actual
                        heapq.heappush(cola_prioridad, (distancias[ciudad_adyacente], ciudad_adyacente))

        # Reconstruir la ruta desde el origen a la ciudad destino
        ruta = []
        ciudad_actual = ciudad2
        while ciudad_actual != ciudad1 and ciudad_actual is not None:
            ruta.insert(0, ciudad_actual)
            ciudad_actual = padres[ciudad_actual]

        # Si no hay ruta, la ciudad destino no es alcanzable desde la ciudad origen
        if ciudad_actual is None:
            return None, float('inf')

        # Agrega la ciudad origen al inicio de la ruta solo si la distancia total es finita
        if distancias[ciudad2] < float('inf'):
            ruta.insert(0, ciudad1)

        # Devolver la ruta y la distancia total
        return ruta, distancias[ciudad2]


    def arbol_recubrimiento_minimo(self):
        # Diccionario para almacenar las distancias mínimas desde el origen a cada ciudad
        distancias = {ciudad: float("inf") for ciudad in self.ciudades}
        distancias[self.ciudades[0]] = 0
        # Cola de prioridad para almacenar las ciudades ordenadas por distancia mínima 
        cola_prioridad = [(0, self.ciudades[0], None)]

        # Conjunto para almacenar las aristas seleccionadas en el Árbol de Recubrimiento Mínimo
        aristas_seleccionadas = set()
        while cola_prioridad: 
            distancia_actual, ciudad_actual, ciudad_padre = heapq.heappop(cola_prioridad)
            # Verificar si ya hemos procesado esta ciudad
            if distancia_actual > distancias[ciudad_actual]:
                continue
            # Agregar la arista al árbol de recubrimiento mínimo
            if ciudad_padre:
                aristas_seleccionadas.add((ciudad_padre, ciudad_actual))

            # Actualizar las distancias para las ciudades adyacentes
            for ciudad_adyacente, distancia_adyacente in enumerate(self.matriz_adyacente[self.ciudades.index(ciudad_actual)]):
                if distancia_adyacente >= 0:
                    # Corregir el cálculo de la nueva distancia
                    nueva_distancia = distancia_actual + distancia_adyacente
                    if nueva_distancia < distancias[self.ciudades[ciudad_adyacente]]:
                        distancias[self.ciudades[ciudad_adyacente]] = nueva_distancia
                        heapq.heappush(cola_prioridad, (nueva_distancia, self.ciudades[ciudad_adyacente], ciudad_actual))

        # Devolver el conjunto de aristas seleccionadas
        return aristas_seleccionadas