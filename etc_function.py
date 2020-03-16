def createHistogram(converted_img):
    gray_level = []
    frequency = []
    histogram = {}
    for i in range(len(converted_img)):
        if converted_img[i] not in gray_level:
            gray_level.append(converted_img[i])
    gray_level.sort()
    for i in range(len(gray_level)):
        frequency.append(converted_img.count(gray_level[i]))
    histogram = dict(zip(gray_level, frequency))
    return histogram


def solve4eqaultion(A, b):
    n = len(A)
    M = A

    i = 0
    for x in M:
        x.append(b[i])
        i += 1

    for k in range(n):
        for i in range(k, n):
            if abs(M[i][k]) > abs(M[k][k]):
                M[k], M[i] = M[i], M[k]
            else:
                pass

        for j in range(k+1, n):
            q = float(M[j][k]) / M[k][k]
            for m in range(k, n+1):
                M[j][m] -= q * M[k][m]

    x = [0 for i in range(n)]

    x[n-1] = float(M[n-1][n])/M[n-1][n-1]
    for i in range(n-1, -1, -1):
        z = 0
        for j in range(i+1, n):
            z = z + float(M[i][j])*x[j]
        x[i] = float(M[i][n] - z)/M[i][i]
    return x


def Bilinear(old_image, pixelXP, pixelYP):
    # point
    x = int(pixelXP//1)
    xplus = int((pixelXP+1)//1)

    y = int(pixelYP//1)
    yplus = int((pixelYP+1)//1)

    xScale = pixelXP - x
    yscale = pixelYP - y
    # read color from old image
    a = old_image[xplus][y] - old_image[x][y]
    b = old_image[x][yplus] - old_image[x][y]
    c = old_image[xplus][yplus] + old_image[x][y] - \
        old_image[x][yplus] - old_image[xplus][y]
    d = old_image[x][y]
    # caculate
    color = (a * xScale) + (b * yscale) + (c * xScale * yscale) + d

    color = int(round(color))
    return color
