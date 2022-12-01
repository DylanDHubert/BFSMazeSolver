# BFSMazeSolver
CSC256 BFS Maze Solver Submission

To use our code, drag and drop and image of a maze you wish to solve into the "Images" folder.

Use photoshop or a similar tool to add one blue (0, 0, 255) pixel as the end, and one red (255, 0, 0) pixel as the start.

I would recommend you use this page to generate a maze if you would like to test for yourself:

https://keesiemeijer.github.io/maze-generator/#generate

Removing maze walls or making the width of walls anything larger than one pixel makes the algorithm extremely slow.
It is not optimized...
So use a width of 1 for the walls and do not remove any edges. It took my computer ~10 minutes to run the large maze, and a few seconds for the small...

You can play around with it if you like.

the file "main.py" is where you can run the stuff, it explains how in the file...

the file "MazeSolver.py" is a class which uses the algorithm as implemented in the "BreadthFirstSearch.py" file...

I have comments through most of the files so I think things should be pretty self explanatory!
