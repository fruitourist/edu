

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


def T(m: list) -> list:
    Tm, s = list(), -1
    for i in range(len(m)):
        Tm.append([])
        s += 1
        for j in range(len(m[0])):
            Tm[s].append(m[j][i])

    return Tm


def adj3(ij: tuple, m3: list) -> int:
    if (ij[0] + ij[1]) % 2 == 0:
        return mr3((ij[0], ij[1]), m3)
    else:
        return -1*mr3((ij[0], ij[1]), m3)


def I3(m3: list) -> tuple:
    Im3 = T(m3)
    for i in range(len(Im3)):
        for j in range(len(Im3)):
            Im3[i][j] = adj3((i, j), m3)

    return (Im3, det3(m3))
