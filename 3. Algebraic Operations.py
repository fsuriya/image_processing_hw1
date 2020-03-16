from readpgm import read_pgm, list_to_2D_list, copy
from writepgm import writepgm


def checklimit(gray_level):
    if gray_level > 255:
        gray_level = 255
    if gray_level < 0:
        gray_level = 0
    return gray_level


def formula1(mattrix_img_blue, mattrix_img_red, mattrix_img_green, col, row):
    mattrix_img_new = copy(mattrix_img_blue)
    for i in range(row):
        for j in range(col):
            mattrix_img_new[i][j] = 2*mattrix_img_green[i][j] - \
                mattrix_img_red[i][j] - mattrix_img_blue[i][j]
            mattrix_img_new[i][j] = checklimit(mattrix_img_new[i][j])
    return mattrix_img_new


def formula2(mattrix_img_blue, mattrix_img_red, mattrix_img_green, col, row):
    mattrix_img_new = copy(mattrix_img_blue)
    for i in range(row):
        for j in range(col):
            mattrix_img_new[i][j] = mattrix_img_red[i][j] - \
                mattrix_img_blue[i][j]
            mattrix_img_new[i][j] = checklimit(mattrix_img_new[i][j])
    return mattrix_img_new


def formula3(mattrix_img_blue, mattrix_img_red, mattrix_img_green, col, row):
    mattrix_img_new = copy(mattrix_img_blue)
    for i in range(row):
        for j in range(col):
            mattrix_img_new[i][j] = int((
                mattrix_img_green[i][j] + mattrix_img_red[i][j] + mattrix_img_blue[i][j])/3)
            mattrix_img_new[i][j] = checklimit(mattrix_img_new[i][j])
    return mattrix_img_new


filename_blue = "./image/3./SanFranPeak_blue.pgm"
filename_red = "./image/3./SanFranPeak_red.pgm"
filename_green = "./image/3./SanFranPeak_green.pgm"
col = 0
row = 0
mattrix_img_red = []
mattrix_img_green = []
mattrix_img_blue = []
listimg_red, col, row = read_pgm(filename_red, col, row)
listimg_green, col, row = read_pgm(filename_blue, col, row)
listimg_blue, col, row = read_pgm(filename_green, col, row)

mattrix_img_red = list_to_2D_list(listimg_red, mattrix_img_red, col, row)
mattrix_img_blue = list_to_2D_list(listimg_blue, mattrix_img_blue, col, row)
mattrix_img_green = list_to_2D_list(listimg_green, mattrix_img_green, col, row)

exceedgreen = formula1(mattrix_img_blue, mattrix_img_red,
                       mattrix_img_green, col, row)
red_blue_diff = formula2(
    mattrix_img_blue, mattrix_img_red, mattrix_img_green, col, row)

intensity = formula3(mattrix_img_blue, mattrix_img_red,
                     mattrix_img_green, col, row)


exceedgreen_filename = "exceedgreen.pgm"
red_blue_diff_filename = "red-blue-differentce.pgm"
intensity_filename = "intensity.pgm"

# writepgm(exceedgreen_filename, exceedgreen, col, row)
# writepgm(red_blue_diff_filename, red_blue_diff, col, row)
# writepgm(intensity_filename, intensity, col, row)
print(mattrix_img_blue)
