from numpy import *

def numop(i):
    
    return  sum(range(i+1))

def suma(mat,i):
    
    resul=0
    for p in range(i):
        for r in range(p,i):
            resul=mat[p][r]
                
    return resul
    
def main():
    
    for i in range(4,12):
        print(i)
        print("la cantidad de operaciones es: "+str(numop(i)))
        mat=range(i**2) 
        mat=reshape(mat,(i,i))
        print("la suma de la matriz superior es:"+str(suma(mat,i)))
if __name__ == "__main__":
    main()