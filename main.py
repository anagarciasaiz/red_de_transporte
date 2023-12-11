from grafo import Grafo
    
if __name__ == "__main__":
    grafo = Grafo()
    grafo.agregar_ciudad("A")
    grafo.agregar_ciudad("B")
    grafo.agregar_ciudad("C")
    grafo.agregar_ciudad("D")

    grafo.agregar_conexion("A", "B", 1)
    grafo.agregar_conexion("A", "C", 2)
    grafo.agregar_conexion("B", "C", 4)
    grafo.agregar_conexion("B", "D", 5)
    grafo.agregar_conexion("C", "D", 2)

    grafo.mostrar_grafo()


    # ejemplo de llamadas a funciones
    ruta, distancia = grafo.ruta_mas_corta("A", "D")
    print(f'Ruta más corta: {ruta}, Distancia: {distancia}')

    aristas_seleccionadas = grafo.arbol_recubrimiento_minimo()
    print(f'Aristas seleccionadas: {aristas_seleccionadas}')

    grafo.visualizar_grafo()




    
    


