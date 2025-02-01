#Cargar la informacion
G = []
#Generar una funcion para obtener los hijos del grafo
#Si me dan el Grafo de la Raiz "A", obtendre 
def obtener_hijos(G,Raiz):
    #EL grafo esta representado como una lista de listas
    return [a for r,a in G if r == Raiz]

def cargarDatos():
    import json
    R = []
    with open('grafo.json') as entrada:
        R = json.load(entrada)
    G.extend(R)

#G    - grafo
#Raiz - Raiz o nodo inicial
#Bus  - El nodo a buscar
#Anchura recorre todos los nodos del arbol en cola por prioridad, eliminando por los que ya paso y dejando los que deberia de pasar
def primero_anch(G, Raiz, Bus):
    cola = [Raiz]                               # Cola de nodos por visitar, comenzamos con la raíz
    visitados = [Raiz]                          # Lista de nodos visitados para evitar ciclos
    recorrido = []                              # Lista para almacenar el recorrido
    
    while cola:                                 # Mientras haya nodos por visitar
        nodo_actual = cola.pop(0)               # Sacamos el primer nodo de la cola (FIFO)
        recorrido.append(nodo_actual)           # Añadimos al recorrido
        
        if nodo_actual == Bus:                  # Si encontramos el nodo buscado
            return f"Nodo {Bus} encontrado. Recorrido: {recorrido}"
        
        hijos = obtener_hijos(G, nodo_actual)   # Obtener los hijos del nodo actual
        
        for hijo in hijos:                      # Añadir a la cola los hijos no visitados
            if hijo not in visitados:
                cola.append(hijo)
                visitados.append(hijo)          # Marcamos el nodo como visitado para evitar ciclos

    return f"Nodo {Bus} no encontrado. Recorrido completo: {recorrido}"

#Consola
def consola():
    #Read Evualte Print Loop (REPL)
    #Ciclo infinito:
    Terminar = False
    while not Terminar:
        #Leer
        R = input(">")
        #Si la lectura es un "quit()" | Termina el ciclo
        if R == "quit()":
            Terminar = True
            continue
        #Evaluate
        P = eval(R)
        #Solo aparecer cuando haya un valor, eliminando los NONE al cargar las funciones
        if P:
            #Imprimir
            print(P)

if __name__ == "__main__":
    cargarDatos()
    consola()