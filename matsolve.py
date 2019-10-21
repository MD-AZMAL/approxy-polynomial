
class GaussSolver:

    def __init__(self,mat,sol,n):
        self.mat = mat
        self.n = n
        
        for i in range(n):
            mat[i].append(sol[i])


    def pivot(self):
        for i in range(self.n):
            max_v = self.mat[i][i]
            max_r = i
            for k in range((i+1),self.n):
                if self.mat[k][i] > max_v:
                    max_v = self.mat[k][i]
                    max_r = k

            for j in range(self.n+1):
                tmp = self.mat[i][j]
                self.mat[i][j] = self.mat[max_r][j]
                self.mat[max_r][j] = tmp
    
            
    def upper(self):
        for i in range(self.n-1):
            for k in range((i+1),self.n):
                off = self.mat[k][i] / self.mat[i][i]
                for j in range(i,self.n+1):
                    self.mat[k][j] -= off*self.mat[i][j]
    
    def solve(self):
        self.upper()
        sol = []
        for i in range(self.n-1,-1,-1):
            coeff = self.mat[i][self.n]/self.mat[i][i]
            for j in range(i-1,-1,-1):
                self.mat[j][self.n]-= coeff * self.mat[j][i]
            sol.insert(0,coeff)
        
        return sol




if __name__ == '__main__':
    mat = [[1,2,4],[4,5,6],[7,8,9]]

    sol = [9,11,56]

    G = GaussSolver(mat,sol,3)

    print(G.mat)
    print(G.n)
    G.pivot()
    print(G.mat)
    # G.upper()
    print(G.mat)
    print(G.solve())
