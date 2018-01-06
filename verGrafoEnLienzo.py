#from Displayable import Displayable

from tkinter import * # Import tkinter para version 3.
from verGrafo import *
from claseGrafo import *

class City(Displayable):
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

# Override the getX method
    def getX(self):
        return self.x

# Override the getY method
    def getY(self):
        return self.y
    # Override the getName method
    def getName(self):
        return self.name


vertices = [City("Chiclayo", 290, 140), City("Piura", 280, 100),
            City("Trujillo", 320, 180), City("Lima", 350, 230),
            City("Ica", 385, 285),
            City("Cajamarca", 330, 120), City("Puno", 585, 320),
            City("Cusco", 510, 250), City("Moquegua", 530, 370),
            City("Tacna", 600, 400), City("Arequipa", 440, 325),
            City("Iquitos", 390, 70)]

# Edge array for graph in Figure 19.1
edges = [
    [0, 1], [0, 2],
    [1, 0], [1, 5],
    [2, 0], [2, 3],
    [3, 2], [3, 4],
    [4, 3], [4, 10],
    [5, 1], [5, 11],[5, 0], [5, 2],
    [6, 9], [6, 7],[6, 8],[6,10],
    [7, 11], [7, 6],[7, 3], [7, 10],[7, 3],[7, 4],
    [8, 9], [8, 10],
    [9, 8], [9,6],
    [10, 8],[10,4],
    [11, 5],[11, 7],[11,3]
    ]


window = Tk() # Create a window
window.title("MAPA DE PERU") # Set title

graph3 = Graph(vertices, edges)

view = GraphView(graph3, window, 1000, 600)
view.pack()

window.mainloop() # Create an event loop





















