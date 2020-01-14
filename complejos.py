from sys import stdin

def sumacomplex(z1,z2):
    a=z1[0]+z2[0]
    b=z1[1]+z2[1]
    c=a,b
    #print("("+str(c[0])+","+str(c[1])+"i"+")")
    return c
 
def restacomplex(z1,z2):
    a=z1[0]-z2[0]
    b=z1[1]-z2[1]
    c=a,b
    return c

def multicomplex(z1,z2):
    a=z1[0]*z2[0]-z1[1]*z2[1]
    b=z1[0]*z2[1]+z1[1]*z2[0]
    c=a,b
    return c

def divcomplex(z1,z2):
    a=(z1[0]*z2[0]+z1[1]*z2[1])/(z2[0]**2+z2[1]**2)
    b=(z1[1]*z2[0]-z1[0]*z2[1])/(z2[0]**2+z2[1]**2)
    c=a,b
    return c

def modcomplex(z1):
    c=(z1[0]**2+z1[1]**2)**(1/2)
    return c

def conjcomplex(z1):
    c=z1[0],z1[1]*(-1)
    return c

import math

def polarcomplex(z1):
    c=modcomplex(z1),math.atan(z1[1]/z1[0])
    return c

def pP(op,z):
    c =z[0], str(z[1])+"i"
    print(str(op),c)
    
##def main():  
##    z1=(0,-3)
##    z2=(3,-10)
##    pP("Suma",sumacomplex(z1,z2))
##    pP("Resta",restacomplex(z1,z2))
##    pP("Multiplicacion",multicomplex(z1,z2))
##    pP("Division",divcomplex(z1,z2))
##    print("Modulo "+str(modcomplex(z1)))
##    pP("Conjugada",conjcomplex(z1))
##    pP("Cartesiano a Polar",polarcomplex(z1))
##main()
