#   DYNAMICALLY GENERATED APPROXIMATE POLYNOMIAL BY GIVEN SAMPLE POINTS
#   ------------------------------------------------------------------
#   Name : Md. Azmal
#   Regno : 1741012060
#   Branch : CSE 'F'
#   Semester : 5th


from matsolve import GaussSolver

pointS = []


def getPoly(pointS):
    solN = []
    coeffMatt = []
    np = len(pointS)
    i=0

    for i in range(np):

        solN.append(pointS[i][1])
        rowMat = []

        for j in range(np):
            rowMat.append(pow(pointS[i][0],j))

        coeffMatt.append(rowMat)

    appPolyCoeff = GaussSolver(coeffMatt,solN,np).solve()

    return appPolyCoeff

while True:
    try:
        print('>>',end='')
        inp = input()

        if inp.split(' ')[0] == 'add':
            pointS.append((float(inp.split(' ')[1]),float(inp.split(' ')[2])))

        elif inp.split(' ')[0] == 'print':
            print(pointS)

        elif inp.split(' ')[0] == 'get' and len(pointS) > 0:
            approxPoly = getPoly(pointS)
            print(approxPoly)
        elif inp.split(' ')[0] == 'pol' and len(pointS) > 0:
            approxPoly = getPoly(pointS)

            t = 0
            poly = ""
            for i in approxPoly:
                if t == 0:
                    poly = "{}".format(i)
                elif t == 1 : 
                    poly = "{} + ({:.4})x ".format(poly,i)
                else :
                    poly = "{} + ({:.4f})x^{} ".format(poly,i,t)
                t = t + 1

            print(poly)

        elif inp.split(' ')[0] == 'clear':
            pointS = []


    except KeyboardInterrupt:
        print('Exiting...')
        break