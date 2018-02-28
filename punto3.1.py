import numpy as np
import math
from sympy import *
from scipy.misc import derivative



    
def newton(x2):
    x = symbols('x', real=True)
    f1=ln(x+2)-sin(x)
    f2=diff(f1,x)
    error= 1
    x1=x2
   
    while (error>1.e-5):
        x2=x1
        x1=x2-((N(f1.subs({x:x2}))*N(f2.subs({x:x2})))/(N(f2.subs({x:x2}))**2-(N(f1.subs({x:x2})))*N(diff(f2,x).subs({x:x2}))))
        if(N(f1.subs({x:x1}))==0 ):break
        error=abs(x1-x2)/abs(x1)
        
    print('la raiz es: '+str(x1))
    
    
def main():
    newton(-1)
    
if __name__ == "__main__":
    main()