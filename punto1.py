from numpy import *
import time
def numop(i):
    
    return  i*(i+1)/2

def suma(mat,i):
    
    resul=0
    for p in range(i):
        for r in range(p,i):
            resul=mat[p][r]
                
    return resul
    
def main():
    
    for i in range(4,12):
        
        mat=range(i**2) 
        mat=reshape(mat,(i,i))
        start=time.clock()
        print("la suma de la matriz superior es:"+str(suma(mat,i))+'\n')
        print("el tiempo de ejcucion es de "+str(time.clock()-start)+"  segundos\n")
        print("la cantidad de operaciones es: "+str(numop(i))+'\n\n')
        
if __name__ == "__main__":
    main()