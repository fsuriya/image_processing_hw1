def writepgm(filename, mattriximg, col, row):
    string = ""
    filename = "./output_img/"+filename
    for i in range(len(mattriximg)):
        for j in range(len(mattriximg[i])):
            mattriximg[i][j] = chr(int(mattriximg[i][j]))
            string += mattriximg[i][j]
    f = open(filename, "a", encoding="ISO-8859-1")

    f.write("P5 \r")
    f.write(str(col) + " " + str(row) + "\r")
    f.write("255 \r")
    f.write(string)
    f.close
