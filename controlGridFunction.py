from etc_function import solve4eqaultion


def controlGrid(disgrid, grid, image, row, col):
    x_dist = [0]*4
    y_dist = [0]*4
    x = [0]*4
    y = [0]*4
    w = [0]*8
    xy = []
    inverse = []
    w_1to4 = []
    w_5to8 = []
    for i in range(len(grid)-1):
        for j in range(len(grid[i])-1):
            x[0] = grid[i][j][0]
            x[1] = grid[i][j+1][0]
            x[2] = grid[i+1][j][0]
            x[3] = grid[i+1][j+1][0]

            y[0] = grid[i][j][1]
            y[1] = grid[i][j+1][1]
            y[2] = grid[i+1][j][1]
            y[3] = grid[i+1][j+1][1]

            w_1to4 = solve4eqaultion(x_dist, w_1to4)
            w_5to8 = solve4eqaultion(y_dist, w_5to8)
