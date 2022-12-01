import copy
import queue

import numpy
import pandas

"""
DYLAN HUBERT + GROUP
PROFESSOR OWRANG
CSC-256
APPLICATION OF DISCRETE STRUCTURES: BREADTH FIRST SEARCH ALGORITHM
PATHFINDING/MAZE-SOLVING

CITATION: https://www.youtube.com/watch?v=hettiSrJjM4&list=WL&index=37&t=860s
Tech With Tim, "Python Path Finding Tutorial - Breadth First Search Algorithm" YouTube.

**** I USED HIS EXPLANATION OF THE BFS ALGORITHM & QUEUES BUT I DID MY OWN IMPLEMENTATION ****
"""

"""
# MAKE A TEST MAZE
Maze1 = list()
Maze1.append(["X"] + [" "] + ["#"] + ["S"] + [" "])
Maze1.append(["#"] + [" "] + ["#"] + ["#"] + [" "])
Maze1.append(["#"] + [" "] + ["#"] + [" "] + [" "])
Maze1.append([" "] + [" "] + ["#"] + [" "] + ["#"])
Maze1.append([" "] + ["#"] + ["#"] + [" "] + ["#"])
Maze1.append([" "] + [" "] + [" "] + [" "] + ["#"])
Maze1 = numpy.array(Maze1)
"""


# VERIFY POSITION EXISTS AND IS OKAY WITHIN WALLS
def verifyPosition(Maze, Position):  # POS: [i, j] [DOWN, ACROSS]
    Height, Width = Maze.shape  # GET THE DIMENSIONS OF THE MAZE/SPACE
    Y, X = Position  # THIS IS BC OF PANDAS DATAFRAMES
    if 0 <= X < Width:  # VALIDATE X
        if 0 <= Y < Height:  # VALIDATE Y
            if Maze[Y][X] == " ":  # VALIDATE SPACE IS MOVABLE
                return 'VALID'
            elif Maze[Y][X] == "X":  # IF NOT MOVABLE CHECK FOR FINISH
                return "SOLVED"
    return "INVALID"  # THIS LINE IS NOT REALLY NEEDED BUT ITS GOOD HERE BECAUSE IT MAKES MORE SENSE TO READ THIS WAY


def turnDirections_Into_Position(Directions: str,
                                 startPos: list):  # INPUT( STRING OF DIRECTIONS IE: "URLDRRLDDDL", START-POSITION: Y, X)
    Directions = list(Directions)  # LIST OUR DIRECTIONS
    thisPos = copy.copy(startPos)  # DON'T ACCIDENTALLY CHANGE THE START
    for eachStep in Directions:  # FOR EACH DIRECTION, GO: Up or Down or Left or Right...
        if eachStep == "U":
            thisPos[0] -= 1
        elif eachStep == "D":
            thisPos[0] += 1
        elif eachStep == "R":
            thisPos[1] += 1
        else:  # "L"
            thisPos[1] -= 1
    return thisPos  # RETURN THE RESULTING POSITION


def getStartPosition(Maze):  # FIND THE START POSITION OF INPUT MAZE
    for i in range(Maze.shape[0]):  # CHECK EACH ROW
        for j in range(Maze.shape[1]):  # CHECK EACH COLUMN IN THAT ROW
            if Maze[i][j] == "S":  # IF IT IS THE START: S,
                return [i, j]  # RETURN THAT POSITION


solutionQueue = queue.Queue()  # IMPORT QUEUE DATA STRUCTURE
solutionQueue.put("")  # BLANK STRING SO THAT THE GET AND STRING.__ADD__ METHODS WORK...


def solveMaze(Maze):
    print("SEARCHING FOR SOLUTION...")
    S = getStartPosition(Maze)  # GET START POSITION
    global solutionQueue  # GET GLOBAL ACCESS TO THE QUEUE
    nextMoveDict = {"U": ("R", "L", "U"), "D": ("R", "L", "D"), "R": ("R", "U", "D"), "L": ("L", "U", "D"), "": ("U", "D", "L", "R")}

    while True:  # LOOP UNTIL SOLVED
        currentSolution = solutionQueue.get()  # GET THE CURRENT SOLUTION FROM THE QUEUE
        if currentSolution != "":  # IN COMBINATION WITH THE DICT THIS SIGNIFICANTLY INCREASES SPEED
            key = currentSolution[-1]
        else:
            key = currentSolution
        for eachPosition in nextMoveDict.get(key):  # FOR EACH POSSIBLE STEP FROM THAT SOLUTIONS POSITION
            newDirection = currentSolution + eachPosition  # ADD THAT NEXT DIRECTION : DIRECTIONS ARE STORED AS STRINGS
            # THE turnDirection_Into_Position TAKES THE START POSITION AND TURNS THE DIRECTION STRING INTO MOVES AND RETURNS THE POSITION TRAVELLED TO
            if verifyPosition(Maze, turnDirections_Into_Position(newDirection,
                                                                 S)) == "VALID":  # TAKES MAZE AND THE DIRECTIONS AS A COORDINATE PAIR, CHECKS VALIDITY OF NEXT MOVES
                solutionQueue.put(newDirection)  # IF THE MOVE IS VALID ADD IT TO THE QUEUE
            elif verifyPosition(Maze, turnDirections_Into_Position(newDirection,
                                                                   S)) == "SOLVED":  # IF THE MOVE FINDS THE END RETURN THAT MOVE
                return newDirection
