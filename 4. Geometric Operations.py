from readpgm import read_pgm, list_to_2D_list, copy
from etc_function import solve4eqaultion, Bilinear
from dist_list import disgrid, grid
from writepgm import writepgm
filename = "./image/4./distlenna.pgm"
# filename = "./image/4./distgrid.pgm"

col = 0
row = 0
mattrix_img = []
listimg, col, row = read_pgm(filename, col, row)
mattrix_img = list_to_2D_list(listimg, mattrix_img, col, row)

grid = grid()
dist = disgrid()

x = [0]*4
y = [0]*4
w1_to_4 = [0]*4
w5_to_8 = [0]*4
w = [0]*8
x_dist = [0]*4
y_dist = [0]*4
xy = []
Am = []
x_vertor_dist = [0]*4
for i in range(4):
    xy_in_loop = []
    Am_in_loop = []
    for j in range(4):
        xy_in_loop.append(0)
        Am_in_loop.append(0)
    xy.append(xy_in_loop)
    Am.append(Am_in_loop)
image_new = []
for i in range(row):
    image_new_in_loop = []
    for j in range(col):
        image_new_in_loop.append(0)
    image_new.append(image_new_in_loop)
count = 0
for i in range(len(grid)-1):
    for j in range(len(grid)-1):
        x[0] = grid[i][j][0]
        x[1] = grid[i][j+1][0]
        x[2] = grid[i+1][j][0]
        x[3] = grid[i+1][j+1][0]

        y[0] = grid[i][j][1]
        y[1] = grid[i][j+1][1]
        y[2] = grid[i+1][j][1]
        y[3] = grid[i+1][j+1][1]
        for k in range(4):
            xy[k][0] = x[k]
            xy[k][1] = y[k]
            xy[k][2] = x[k]*y[k]
            xy[k][3] = 1
        x_dist[0] = dist[i][j][0]
        x_dist[1] = dist[i][j+1][0]
        x_dist[2] = dist[i+1][j][0]
        x_dist[3] = dist[i+1][j+1][0]

        y_dist[0] = dist[i][j][1]
        y_dist[1] = dist[i][j+1][1]
        y_dist[2] = dist[i+1][j][1]
        y_dist[3] = dist[i+1][j+1][1]
        xy_new1 = copy(xy)
        xy_new2 = copy(xy)
        w1_to_4 = solve4eqaultion(xy_new1, x_dist)
        w5_to_8 = solve4eqaultion(xy_new2, y_dist)
        for k in range(len(w1_to_4)):
            w[k] = w1_to_4[k]
        for k in range(len(w5_to_8)):
            w[k+4] = w5_to_8[k]

        for k in range(y[0], y[2]):
            for l in range(x[0], x[1]):
                xp = (w[0]*l + w[1]*k + w[2]*l*k + w[3])
                yp = (w[4]*l + w[5]*k + w[6]*l*k + w[7])
                image_new[k][l] = Bilinear(mattrix_img, yp, xp)
writepgm("new_lenna.pgm", image_new, col, row)
