
## Conway's Game of Life in Python with Pygame

This is a Python implementation of Conway's Game of Life using the Pygame library.

**Description:**

The simulation known as "Conway's Game of Life" is a cellular automaton devised by John Horton Conway in 1970. We are going to build it with Python using Pygame.


**Rules:**

* A live cell with two or fewer live neighbors dies.
* A live cell with three live neighbors lives.
* A live cell with more than three live neighbors dies.
* A dead cell with exactly three live neighbors becomes alive.


**Features:**

* Implements the classic Conway's Game of Life rules.
* Allows manual placement of live cells with mouse clicks.
* Offers different simulation speeds: Normal, Slow, and Fast (controlled with keyboard shortcuts).
* Supports random generation of live cells.

**Instructions:**

**Installation:**

Make sure you have Python 3 and Pygame installed. You can install Pygame using:

```bash
pip install pygame
```

**Running the Simulation:**

Save the code as a Python file (e.g., game_of_life.py). Then, run it from the command line:

```bash
python game_of_life.py
```

**Controls:**

* Spacebar: Pause/Unpause the simulation.
* R Key: Randomly generate a new set of live cells.
* C Key: Toggle slow simulation mode.
* S Key: Toggle fast simulation mode.
* Left Mouse Button: Click on the grid to toggle a cell between alive and dead.

**Screenshots:**

![alt text](https://github.com/H3xKatana/GameOfLife/blob/main/A.png?raw=true)
![alt text](https://github.com/H3xKatana/GameOfLife/blob/main/B.png?raw=true)

**How the Code Works:**

The core functionality lies in the `adjust_grid` function. It iterates through all cells and their neighbors, applying the following rules:

* A live cell with two or fewer live neighbors dies.
* A live cell with three live neighbors lives.
* A live cell with more than three live neighbors dies.
* A dead cell with exactly three live neighbors becomes alive.


