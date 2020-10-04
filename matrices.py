

def det2(m2: list) -> int:
    return m2[0][0]*m2[1][1] - m2[0][1]*m2[1][0]


def mr3(ij: tuple, m3: list) -> list:

    m2, s = [[], []], 0
    for i in range(len(m3)):
        if i != ij[0]:
            for j in range(len(m3)):
                if j != ij[1]:
                    m2[s].append(m3[i][j])
            s += 1

    return det2(m2)


def det3(m3: list) -> int:
    return m3[0][0]*mr3((0, 0), m3) - m3[0][1]*mr3((0, 1), m3) + m3[0][2]*mr3((0, 2), m3)


def t(m: list) -> list:

    tm, s = list(), -1
    for i in range(len(m)):
        tm.append([])
        s += 1
        for j in range(len(m[0])):
            tm[s].append(m[j][i])

    return tm


def a3(ij: tuple, m3: list) -> int:
    if (ij[0] + ij[1]) % 2 == 0:
        return mr3((ij[0], ij[1]), m3)
    else:
        return -mr3((ij[0], ij[1]), m3)


def i3(m3: list) -> tuple:

    im3 = t(m3)
    for i in range(len(im3)):
        for j in range(len(im3)):
            im3[i][j] = a3((i, j), m3)

    return (im3, det3(m3))


def il3(m3: list, v13: list) -> list:

    _i3 = i3(m3)
    im3 = _i3[0]

    x = list()
    for n in (im3[0][0], im3[0][1], im3[0][2]):
        x.append(v13[0]*n)

    y = list()
    for n in (im3[1][0], im3[1][1], im3[1][2]):
        y.append(v13[1]*n)

    z = list()
    for n in (im3[2][0], im3[2][1], im3[2][2]):
        z.append(v13[2]*n)

    return [(x[0]+y[0]+z[0])/_i3[1], (x[1]+y[1]+z[1])/_i3[1], (x[2]+y[2]+z[2])/_i3[1]]
