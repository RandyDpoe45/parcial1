from numpy import *
import math


def aitken(x0,x1,x2):
    return x2-((x2-x1)**2)/(x2-2*x1+x0)
"""serie de taylor para e^x """
def taylorE(x,k):
    return sum((x**i)/math.factorial(i) for i in range(k+1))
    
def main():
    """valor a evaluar x=1"""
    y=1
    """valores iniciales para aitken"""
    x0=taylorE(y,0)
    x1=taylorE(y,1)
    x2=taylorE(y,2)
    err=1
    i=3
    p0=aitken(x0,x1,x2)
    while(err>1.e-5):
        p1=p0
        print(p0)
        x0=taylorE(y,i-2)
        x1=taylorE(y,i-1)
        x2=taylorE(y,i)
        i+=1
        p0=aitken(x0,x1,x2)
        err=abs(p0-p1)/abs(p0)
        # err+=1
    
if __name__ == "__main__":
    main()
