
class Graph:
    # Constructor de clase, recibe lista de vertices, y lista de aristas.
	# La lista arista guarda vertice inicio y destino
    def __init__(self, vertices, edges):
         self.vertices = vertices
         self.neighbors = self.getAdjacnecyLists(edges)
		 
    def getAdjacnecyLists(self, edges):
        neighbors = []
	    # Llena la lista de aristas desde edges	
        for i in range(len(self.vertices)):
             neighbors.append([]) # Each element is another list

        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]
            neighbors[u].append(v) # Insert a neighbor for u
        return neighbors
    
# Devuelve el número de vértices en el grafo
    def getSize(self):
         return len(self.vertices)

# Devuelve los vértices en el grafo
    def getVertices(self):
        return self.vertices

# Devuelva el vértice en el índice especificado
    def getVertex(self, index):
        return self.vertices[index]

# Devuelve el indice del vértice especificado
    def getIndex(self, v):
        return self.vertices.index(v)

# Devuelve los vecinos del vértice con el índice especificado
    def getNeighbors(self, index):
        return self.neighbors[index]
    
 # Devuelve el grado de un vértice especificado
    def getDegree(self, v):
        return len(self.neighbors[self.getIndex(v)])

# Imprime las aristas
    def printEdges(self):
        for u in range(0, len(self.neighbors)):
             print(self.getVertex(u) + " (" + str(u), end = "): ")
        for j in range(len(self.neighbors[u])):
            print("(" + str(u) + ", " +
    str(self.neighbors[u][j]), end = ") ")
    print()

# Clear graph
    def clear(self):
        vertices = []
        neighbors = []

# Adicionar un vertice al grafo
    def addVertex(self, vertex):
         if not (vertex in self.vertices):
            self.vertices.append(vertex)
            self.neighbors.append([]) # add a new empty adjacency list

# Agregar una arista no dirigida al grafo
    def addEdge(self, u, v):
        if u in self.vertices and v in self.vertices:
            indexU = self.getIndex(u)
            indexV = self.getIndex(v)
        if not (indexV in self.neighbors[indexU]):
            self.neighbors[indexU].append(indexV)










                
