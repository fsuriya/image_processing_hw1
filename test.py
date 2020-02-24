
def read_pgm(filename):
    f = open(filename, encoding="ISO-8859-1")
    list_img = []
    img = []
    comment = False
    # matirx_img = []
    for i, line in enumerate(f):
        if i >= 3:
            for j in range(len(line)):
                img.append(line[j])
    f.close()
    print(len(img))
    # for i in range(len(img)):
    #     list_img.append((ord(img[i])))
    return img


# converted = read_pgm("./image/2./SEM256_256.pgm")
# converted = read_pgm("./image/4./distgrid.pgm")
# converted = read_pgm("./image/4./distlenna.pgm")
# converted = read_pgm("./image/4./grid.pgm")
# converted = read_pgm("./image/3./SanFranPeak_green.pgm")
# print(converted)

# unknown bug 2.SEM 3.
# converted = read_pgm("./image/2./SEM256_256.pgm", col, row)  # bug
# converted = read_pgm("./image/4./distgrid.pgm", col, row)
# converted = read_pgm("./image/4./distlenna.pgm", col, row)  # bug
# converted = read_pgm("./image/4./grid.pgm", col, row)
# converted = read_pgm("./image/3./SanFranPeak_red.pgm", col, row)
# converted = read_pgm("./image/3./SanFranPeak_blue.pgm", col, row)  # bug
# converted = read_pgm("./image/3./SanFranPeak_green.pgm", col, row)
