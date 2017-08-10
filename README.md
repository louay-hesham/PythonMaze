# Python Maze
## A python maze solver with GUI

This python code generates a random 3D maze, then tries to solve it with different informed and uninformed search algorithms and compares the cost.

## Buttons Guide
* **R** to generate a new random map
* **A, B, C, D** or **E** to choose one of the predefined maps
* **1** for DFS algorithm
* **2** for BFS algorithm
* **3** for UCS algorithm
* **4** for A* algorithm with h = Manhattan distance
* **5** for A* algorithm with h = Euclidean distance
* **6** for greedy algorithm with h = Manhattan distance
* **7** for greedy algorithm with h = Euclidean distance
* **Right arrow** to navigate to the next step

## Colors guide
* **White:** unvisited and not in the frontier list
* **Yellow:** in the frontier list
* **Blue:** node currently being visited in this step
* **Purple:** node previously visited in previous steps
* **Cyan:** node in the final path to the goal
