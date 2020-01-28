from sys import stdin

#---------------------------NUMEROS COMPLEJOS-----------------------------------#

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

#---------------------------VECTORES COMPLEJOS-----------------------------------#

def sumavector(v1,v2):
    c=[]
    for i in range(len(v1)):
        a=sumacomplex(v1[i],v2[i])
        c.append(a)
    return c

def inversovector(v1):
    c=[]
    for i in range(len(v1)):
        c.append((v1[i][0]*(-1),v1[i][1]*(-1)))
    return c

def multescalarvector(z1,v1):
    c=[]
    for i in range(len(v1)):
        c.append(multicomplex(z1,v1[i]))
    return camatrices(m1,m2):
##    c=m1
##    m2=multescalarmatrices((-1,0),m2)
##    c=adicionmatrices(m1,m2)
##    norma(c) #Toca hacer la multiplicacion de matrices
    

#-----------------------ACCION DE UNA MATRIZ SOBRE UN VECTOR-----------------------------------#
       
def sumacompvector(v1):
    if len(v1) < 2 :
        return v1[0]
    elif len(v1) == 2:
        s = sumacomplex(v1[0],v1[1])
        return s
    else:
        s = sumacomplex(v1[0],v1[1])
        for i in range (2,len(v1)):
            s = sumacomplex(s,v1[i])
        return s
    
def accionmatrizvector(m1,v1):
    c = []
    d = []
    for i in range (len(m1)):
        c.append([])
        for j in range (len(m1)):
            c[i].append(multicomplex(m1[i][j],v1[j]))
    for i in range (len(c)):
        d.append(sumacompvector(c[i]))        
    return d


def main():
    z1=[(1,1),(2,1)]
    print(multicomplex())
main()

##    m1=[[(3,2),(3,1)],[(0,2),(1,2)]]
##    for i in range(len(m1)):
##        print(m1[i])
##    print(".")
##    for j in range(len(m1)):
##        print(matriztranspuesta(m1)[j])
##    m1=[[(3,2),(3,1)],[(0,2),(1,2)]] m2=[[(1,3),(0,2)],[(1,1),(1,0)]]
##    print(adicionmatrices(m1,m2)) z1=(3,2)
##    v1=[(6,3),(0,0),(5,1),(4,0)]
##    print(multescalar(z1,v1))
##    v1=[(6,-4),(7,3),(4.2,-8.1),(0,-3)]
##    v2=[(16,2.3),(0,-7),(6,0),(0,-4)] print(sumavector(v1,v2))
##    z1=(0,-3) z2=(3,-10) pP("Suma",sumacomplex(z1,z2))
##    pP("Resta",restacomplex(z1,z2))
##    pP("Multiplicacion",multicomplex(z1,z2))
##    pP("Division",divcomplex(z1,z2)) print("Modulo
##    "+str(modcomplex(z1))) pP("Conjugada",conjcomplex(z1))
##    pP("Cartesiano a Polar",polarcomplex(z1))


#---------------------------MATRICES COMPLEJAS-----------------------------------#

def adicionmatrices(m1,m2):
    c=[]
    for i in range(len(m1)):
        c.append([])
        for j in range(len(m1[0])):
            a=sumacomplex(m1[i][j],m2[i][j])
            c[i].append(a)
    return c

def inversamatriz(m1):
    c=[]
    for i in range(len(m1)):
        c.append(inversovector(m1[i]))
    return c

def multescalarmatrices(z1,m1):
    c=[]
    for i in range(len(m1)):
        c.append(multescalarvector(z1,m1[i]))
    return c

def matriztranspuesta(m1):
    c=[]
    for i in range(len(m1)):
        c.append([])
        for j in range(len(m1[0])):
            c[i].append(m1[j][i])
    return c 

def conjmatriz(m1):
    c=[]
    for i in range(len(m1)):
        c.append([])
        for j in range(len(m1[0])):
            c[i].append(conjcomplex(m1[j][i]))
    return c

def adjmatriz(m1):
    return conjmatriz(matriztranspuesta(m1))

def innervector(v1,v2):
    s = multiplicacion(v1[0],v2[0])
    for i in range(1, len(v1)):
        s  = sumacomplex(s,multicomplex(v1[i],v2[i]))
    return s

def conjugadavector(v1):
    c = []
    for i in range (len(v1)):
        c.append(conjcomplex(v1[i]))
    return c

def norma(v1):
    if tuple == type(a[0]):
        return ((innervector(v1,conjugadavector(v1)))[0])**(1/2)
    
##def distanciamatrices(m1,m2):
##    c=m1
##    m2=multescalarmatrices((-1,0),m2)
##    c=adicionmatrices(m1,m2)
##    norma(c) #Toca hacer la multiplicacion de matrices
    

#-----------------------ACCION DE UNA MATRIZ SOBRE UN VECTOR-----------------------------------#
       
def sumacompvector(v1):
    if len(v1) < 2 :
        return v1[0]
    elif len(v1) == 2:
        s = suma(v1[0],v1[1])
        return s
    else:
        s = suma(v1[0],v1[1])
        for i in range (2,len(v1)):
            s = suma(s,v1[i])
        return s
    
def accionmatrizvector(m1,v1):
    c = []
    d = []
    for i in range (len(m1)):
        c.append([])
        for j in range (len(m1)):
            c[i].append(multicomplex(m1[i][j],v1[j]))
    for i in range (len(c)):
        d.append(sumacompvector(c[i]))        
    return d


def main():
    z1=[(1,1),(2,1)]
    print(multicomplex())
main()

##    m1=[[(3,2),(3,1)],[(0,2),(1,2)]]
##    for i in range(len(m1)):
##        print(m1[i])
##    print(".")
##    for j in range(len(m1)):
##        print(matriztranspuesta(m1)[j])
##    m1=[[(3,2),(3,1)],[(0,2),(1,2)]] m2=[[(1,3),(0,2)],[(1,1),(1,0)]]
##    print(adicionmatrices(m1,m2)) z1=(3,2)
##    v1=[(6,3),(0,0),(5,1),(4,0)]
##    print(multescalar(z1,v1))
##    v1=[(6,-4),(7,3),(4.2,-8.1),(0,-3)]
##    v2=[(16,2.3),(0,-7),(6,0),(0,-4)] print(sumavector(v1,v2))
##    z1=(0,-3) z2=(3,-10) pP("Suma",sumacomplex(z1,z2))
##    pP("Resta",restacomplex(z1,z2))
##    pP("Multiplicacion",multicomplex(z1,z2))
##    pP("Division",divcomplex(z1,z2)) print("Modulo
##    "+str(modcomplex(z1))) pP("Conjugada",conjcomplex(z1))
##    pP("Cartesiano a Polar",polarcomplex(z1))
