from matsolve import GaussSolver

solN = []
coeffMatt = []

np = int(input('Enter no of points : '))

i=0

for i in range(np):
    
    xi = float(input('Enter x{} :'.format(i)))
    yi = float(input('Enter y{} :'.format(i)))
    print()

    solN.append(yi)
    rowMat = []

    for j in range(np):
        rowMat.append(pow(xi,j))
    
    coeffMatt.append(rowMat)

appPolyCoeff = GaussSolver(coeffMatt,solN,np).solve()

print(solN)
print()
print()
print(coeffMatt)
print()
print()
print(appPolyCoeff)





