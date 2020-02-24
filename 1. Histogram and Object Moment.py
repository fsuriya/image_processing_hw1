from readpgm import read_pgm, list_to_2D_list, copy
from momentFunction import pqmoment, pqN, pqHu
from etc_function import createHistogram
filename = "./image/1./scaled_shapes.pgm"
converted_img = []
mattrix_img = []
col = 0
row = 0

converted_img, col, row = read_pgm(filename, col, row)
mattrix_img = list_to_2D_list(converted_img, mattrix_img, col, row)


object_dict = {}
count = 0

histogram = createHistogram(converted_img)
# count object
for key in histogram:
    if histogram[key] > 1500 and key != 255:
        object_dict[key] = histogram.get(key)
        count = count+1

print("Histogram of image :")
print(histogram)
print("Number of Object : " + str(count))
print("Gray level of each object")
print(object_dict)

maskesOb_img = copy(mattrix_img)

check = []
countcheck = 0

for key in object_dict:

    for i in range(row):
        for j in range(col):
            if mattrix_img[i][j] == key:
                maskesOb_img[i][j] = 1
                countcheck += 1
            else:
                maskesOb_img[i][j] = 0
    # check.append(countcheck)
    # print(countcheck)
    countcheck = 0
    U20 = pqHu(2, 0, maskesOb_img, row, col)
    U02 = pqHu(0, 2, maskesOb_img, row, col)
    N20 = pqN(2, 0, maskesOb_img, row, col)
    N02 = pqN(0, 2, maskesOb_img, row, col)
    theata = N20 + N02

    print("Central moment of an Object on gray level(" +
          str(key) + ") : U20 = " + str(U20) + ", U02 =" + str(U02) + ", Theata = " + str(theata))
    maskesOb_img = copy(mattrix_img)
# print(check)
