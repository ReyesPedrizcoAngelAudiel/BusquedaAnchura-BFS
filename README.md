# ⚙️ Búsqueda en Anchura (BFS) en Grafos
#### 💻 Proyecto en Python para realizar búsqueda de anchura en un grafo representado en JSON.
> Este proyecto implementa la búsqueda en anchura (BFS) en un grafo representado como una lista de adyacencia. Permite cargar los datos desde un archivo JSON y ejecutar consultas a través de una consola interactiva.

#### 🌐 Visualización del Grafo
---
![](/pa.png)

#### 🚀 Características
>+ **Carga de Datos desde JSON:** 
>   + Se carga la información del grafo desde un archivo JSON.
>+ **Obtención de Hijos:** 
>   + Se extraen los nodos hijos de un nodo dado.
>+ **Búsqueda en Anchura (BFS):** 
>   + Implementa una búsqueda por niveles utilizando una cola FIFO (First-In, First-Out).
>   + Evita ciclos almacenando nodos visitados en la lista visitados.
>   + Devuelve el camino recorrido hasta encontrar el nodo buscado.
>+ **Interfaz por Consola (REPL):** 
>   + Se puede interactuar con el sistema mediante comandos en la terminal.
>   + Implementa un bucle interactivo (Read-Eval-Print Loop, REPL).

#### 📚 Estructura del Proyecto
    E2-Anchura/
    │── grafo.json             # Archivo con la representación del grafo
    │── repl_PPApy           # Implementación de la búsqueda BFS y la consola interactiva


#### 🛠️ Instalación y Uso
    Clonar el repositorio.
	Ejecutar el programa: "repl_PP.py"
	Ejemplo de uso:
	        1 - Para buscar un camino desde "A" hasta "AC2A3", en la consola ingresar: primero_anch(G, "A", "AC2A3")
		2 - Salida esperada: "Nodo AC2A3 encontrado. Recorrido: ['A', 'AA', 'AB', 'AC', 'AD', 'AAA', 'AAB', 'ABA', 'ACA', 'ACB', 'ACC', 'ADA', 'ADB', 'A3A', 'A3B', 'A2BA', 'A2B2', 'ABA2', 'AC2A', 'ADBA', 'ADB2', 'ABA3', 'ABA2B', 'AC2A2', 'ADAB', 'AC2A3']"
		3 - Para salir de la consola, ingresar: "quit()"

#### 🔄 Funcionamiento del Código
##### Carga de datos
    def cargarDatos():
    import json
    R = []
    with open('grafo.json') as entrada:
        R = json.load(entrada)
    G.extend(R)
##### Obtención de Hijos
    def obtener_hijos(G,Raiz):
    return [a for r,a in G if r == Raiz]
##### Algoritmo BFS
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
##### Consola Interactiva (REPL)
    def consola():
    while True:
        R = input("> ")
        if R == "quit()":
            break
        P = eval(R)
        if P:
            print(P)

#### 🎨 Mejoras Futuras
>- **Visualización del grafo:** 
>Implementar una librería para visualizar el grafo de manera gráfica.
---
###### 🌟 ¡Gracias por revisar este proyecto! 
###### Si tienes sugerencias o mejoras, no dudes en contribuir. 🦊
