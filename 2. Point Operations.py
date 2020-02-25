from readpgm import read_pgm, list_to_2D_list, copy
from writepgm import writepgm
from etc_function import createHistogram
# filename = "./image/2./Cameraman.pgm"
filename = "./image/2./SEM256_256.pgm"

converted_img = []
mattrix_img = []
col = 0
row = 0

converted_img, col, row = read_pgm(filename, col, row)
mattrix_img = list_to_2D_list(converted_img, mattrix_img, col, row)
histogram_old = createHistogram(converted_img)
current_D = []
miss_frequency = []
miss_update = {}
for i in range(256):  # find miss colour
    if i not in histogram_old:
        miss_frequency.append(i)
# complete with colore frequenct = 0
miss_update = {i: 0 for i in miss_frequency}
for key in miss_update:
    histogram_old.update({key: miss_update[key]})

histogram_old = {key: histogram_old[key]
                 for key in sorted(histogram_old.keys())}  # sorted to dict
# print(histogram_old)
histogram_db = histogram_old.copy()
area = col*row

for D in histogram_db:
    histogram_db[D] = histogram_db[D] / area  # H(D) / area
Pcxy = 0
for D in histogram_db:
    Pcxy += histogram_db[D]
    histogram_db[D] = Pcxy  # convert to PMF
for D in histogram_db:
    histogram_db[D] = histogram_db[D]*255  # convert to CMF
for D in histogram_db:
    histogram_db[D] = int(histogram_db[D] // 1)  # floor number
# convert from {DA : DB} to {DB : DA}
histogram_db = dict((y, x) for x, y in histogram_db.items())
# current dict is {DB : DA }
test_array = []
test = 0
for i in range(len(mattrix_img)):
    for j in range(len(mattrix_img[i])):
        for key in histogram_db:
            if mattrix_img[i][j] == histogram_db[key]:
                mattrix_img[i][j] = key

# print(mattrix_img)
# referred https://stackoverflow.com/questions/29244286/how-to-flatten-a-2d-list-to-1d-without-using-numpy/29244327
new_histogram_list = [i for subarray in mattrix_img for i in subarray]
new_histogram = createHistogram(new_histogram_list)
print("Before " + str(histogram_old))
print("--------------------")
print(histogram_db)

print("-------------")
print("After " + str(new_histogram))
filename_new = "test.pgm"
writepgm(filename_new, mattrix_img, col, row)
