import copy

import PIL.Image
import numpy
from queue import Queue, LifoQueue

import BreadthFirstSearch

class MazeSolver:
    def __init__(self):
        self.Maze = None  # WILL BE NUMPY.ARRAY() OF MAZE, "#"=WALL, " "=MOVABLE, "End", "Start"
        self.solutionText = str
        self.solvedMaze = None
        self.fName = str
        self.startPos = [None, None]


    # LOAD MAZE FROM IMAGE, BLACK PIXELS WALLS, WHITE MOVABLE, BLUE END, RED START.
    def loadMaze(self, Maze: str):
        self.fName = Maze
        with PIL.Image.open(f"Images/{Maze}") as thisMaze:
            thisMaze = numpy.array(thisMaze)
            useMaze = []
            for i, Rows in enumerate(thisMaze):
                newRow = []
                for j, eachPixel in enumerate(Rows):
                    eachPixel = list(eachPixel)
                    if eachPixel == [0, 0, 0]:
                        newRow.append("#")
                        thisMaze[i][j] = [0, 0, 0]
                    elif eachPixel == [255, 255, 255]:
                        newRow.append(" ")
                        thisMaze[i][j] = [255, 255, 255]
                    elif eachPixel == [255, 0, 0]:
                        newRow.append("S")
                        thisMaze[i][j] = [255, 0, 0]
                        self.startPos = [i , j]
                    elif eachPixel == [0, 0, 255]:
                        newRow.append("X")
                        thisMaze[i][j] = [0, 0, 255]
                useMaze.append(newRow)
            self.Maze = numpy.array(useMaze)
            self.solvedMaze = thisMaze
        print("Maze Dimensions:", self.Maze.shape)

    def solveMaze(self):
        self.solutionText = BreadthFirstSearch.solveMaze(self.Maze)
        pos = self.startPos
        for eachInstruction in list(self.solutionText):
            if eachInstruction == "U":
                pos[0] -= 1
            elif eachInstruction == "D":
                pos[0] += 1
            elif eachInstruction == "R":
                pos[1] += 1
            else:  # "L"
                pos[1] -= 1
            self.solvedMaze[pos[0]][pos[1]] = [255, 0, 0]

    def run(self, mazeFileName):
        self.loadMaze(mazeFileName)
        self.solveMaze()
        solvedMazeImage = PIL.Image.fromarray(self.solvedMaze)
        solvedMazeImage.show()
        solvedMazeImage.save(f"solved{mazeFileName}")
