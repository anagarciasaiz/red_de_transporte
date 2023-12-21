link repositorio: https://github.com/anagarciasaiz/red_de_transporte

# Entrega: Red de Transporte
Se te ha encargado crear un sistema para optimizar la red de transporte entre ciudades. Debes modelar este problema como un grafo donde cada nodo representa una ciudad y
cada arista representa una conexión entre dos ciudades. Cada arista tiene asociado un peso que representa la distancia entre las ciudades. Además, se requiere mantener un registro ordenado de las distancias entre ciudades. Para esto, se debe utilizar un árbol binario de búsqueda (BST) donde las claves sean las distancias y los valores sean las ciudades conectadas por esa distancia.  

Se te pide implementar lo siguiente:  
- Una clase Grafo que represente el grafo de ciudades y sus conexiones. Debe permitir añadir ciudades, agregar conexiones entre ellas con sus respectivos pesos y mostrar el grafo resultante.

- Un método para encontrar la ruta más corta entre dos ciudades. Deberás implementar una función ruta_mas_corta(origen, destino) que devuelva la ruta
más corta entre las ciudades origen y destino (el camino de ciudades recorridas), junto con la distancia total de esa ruta.

- Integrar un BST para mantener un registro ordenado de las distancias entre ciudades. Implementa funciones para agregar una nueva distancia con sus ciudades correspondientes y para mostrar el registro ordenado.

- Un método que seleccione una colección de aristas tal que el grafo quede conectado y la suma de las distancias sea mínima (Árbol de recubrimiento mínimo).
