from tkinter import *

class Displayable:
    def getX(self): # Get x-coordinate of the vertex
        return 0

    def getY(self): # Get y-coordinate of the vertex
        return 0
    def getName(self): # Get display name of the vertex
        return ""

		
class GraphView(Canvas):
    def __init__(self, graph, container, width = 800, height = 450):
        super().__init__(container, width = width, height = height)
        self.graph = graph
        self.drawGraph()
    def drawGraph(self):
        vertices = self.graph.getVertices()
        for i in range(self.graph.getSize()):
            x = vertices[i].getX()
            y = vertices[i].getY()
            name = vertices[i].getName()
# Display a vertex
            tam =  10
            self.create_oval(x - tam, y - tam, x + tam, y + tam,
            fill = "blue")
# Display the name
            self.create_text(x, y - tam-5, text = str(name),fill="red")

# Draw edges for pair of vertices
        for i in range(self.graph.getSize()):
            neighbors = self.graph.getNeighbors(i)
            x1 = self.graph.getVertex(i).getX()
            y1 = self.graph.getVertex(i).getY()
            for v in neighbors:
                x2 = self.graph.getVertex(v).getX()
                y2 = self.graph.getVertex(v).getY()
# Draw an edge for (i, v)
                self.create_line(x1, y1, x2, y2,fill="green")



