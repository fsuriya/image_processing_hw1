
def read_pgm(filename, converted_img, col, row):
    f = open(filename, encoding="ISO-8859-1")
    img = ""
    list_img = []
    # matirx_img = []
    for i, line in enumerate(f):
        if i == 2:
            col = int(line[0:3])
            row = int(line[4:])
        if i >= 4:
            img = img+line
    f.close()
    for i in range(len(img)):
        list_img.append((ord(img[i])))
    return list_img, col, row


def list_to_2D_list(lists, list_2D, col, row):
    for i in range(row):
        inner_list = []
        for j in range(col):
            inner_list.append(lists[i*(col)+j])
        list_2D.append(inner_list)
    return list_2D


def copy(lists):
    copy_list = []
    for i in range(len(lists)):
        inner_list = []
        for j in range(len(lists[i])):
            inner_list.append(lists[i][j])
        copy_list.append(inner_list)
    return copy_list
