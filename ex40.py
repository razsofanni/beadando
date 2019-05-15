import numpy as np

alsok = 10
felsok = 20


def get_matrix(also, felso):
    (a, b, c, d) = np.random.randint(0, 100, 4)
    det = (a * d) - (b * c)
    if det >= also and det <= felso:
        return (a, b, c, d)
    else:
        # cnt = 0
        while True:


            (a, b, c, d) = np.random.randint(0, 100, 4)
            det = (a * d) - (b * c)
            if det >= also and det <= felso:
                return (a, b, c, d)


def main():
    m = get_matrix(alsok, felsok)

    #print(m)
    a, b, c, d = m

    eredmeny = [ [a, b],
               [c, d] ]

    det = (a * d) - (b * c)
    #print(a, b, c, d)
    print(det)

    print(eredmeny)





main()
