import numpy as np
import math

def Fx(x):
   
    return np.log(x+2)-np.sin(x)
    
def F1x(x):
    return 1-np.exp(-x)

def secante(x0,x1):
    error=1
    x=(Fx(x1)*x0-Fx(x0)*x1)/(Fx(x1)-Fx(x0))
    while(error>1.e-7):
        x0=x1
        x1=x
        x=(Fx(x1)*x0-Fx(x0)*x1)/(Fx(x1)-Fx(x0))
        
        if (Fx(x) == 0):break
        
        error=abs(Fx(x)/F1x(x))
    print('la raiz es: '+str(x))

                
def main():
    secante(-1.6,-1)
if __name__ == "__main__":
    main()
