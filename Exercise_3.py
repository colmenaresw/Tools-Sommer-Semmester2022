# Wilfredo Colmenares
# 2130541
# Tools
# implementation of game of life
import random, copy, time, os
from signal import pause

def create_grid(width, height):
    """
        a function to initialize a grid with random values
        width: the width of the grid
        height: the height of the grid
    """
    grid = []
    for i in range(width):
        grid.append([])
        for j in range(height):
            cell = 1 if random.random() <= 0.2 else 0  # determine the value of the cell randomly
            grid[i].append(cell)
    
    return grid

def check_neighbours(grid, x, y, width_s, height_s):
    """
        a function to check how many living cell are around one specific cell
    """
    
    living_cells = 0  # we initialize a counter of living cells

    for i in range(-1,2,1):
        for j in range(-1,2,1):
            x_pos = x+i
            y_pos = y+j

            if i == 0 and j == 0:  # we skip the cell itself
                continue

            if y_pos > width_s - 1:
                y_pos = 0
            
            if x_pos > height_s - 1:
                x_pos = 0

            living_cells += grid[x_pos][y_pos]

    return living_cells

def generate_next_generation(grid):
    new_grid = copy.deepcopy(grid)  # we create a new array exactly like the old one
    width_s = len(grid[0])  # we obtain the size of the rows
    height_s = len(grid)  # we obtain the size of the columns

    for i in range(height_s):
        for j in range(width_s):
            living_neigh = check_neighbours(grid,i,j, width_s, height_s)
            if grid[i][j] == 1:  # rules for living cells
                if living_neigh < 2 or living_neigh > 3:  # less than two or bigger than three neighbours die
                    new_grid[i][j] = 0            
                elif living_neigh == 2 or living_neigh == 3:
                    new_grid[i][j] = 1 
            else:  # rule for death cells
                if living_neigh == 3:  # if exactly 3 neighbours live, the cell becomes alive
                    new_grid[i][j] = 1
    
    return new_grid


            


if __name__ == "__main__":
    red = "\033[0;47m \033[0m"
    white = "\033[0;41m \033[0m"
    g = create_grid(10,10)
    for n in range(100):
        for row in range(len(g)):  # printing new row
            print("\n")
            for cell in g[row]:
                print(" ", end='')
                print(red if cell == 1 else white, end='')
        g = generate_next_generation(g)
        time.sleep(0.5)
        os.system('clear')
        
    
