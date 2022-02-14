print("Bienvenido a su libreria de computación cuántica parte 2")
print("Realizado por Thomas Feris Riaño")

#Suma de vectores complejos
def suma(a,b):
    imaginario1 = a[0] , b[0] ,c[0]
    imaginario2 = a[1] , b[1] ,c[1]
    suma = a[0]+ a[1] , b[0] +b[1] , c[0] + c[1]
    return (suma)

#Inverso (aditivo) de un vector complejo.

def inverso(a,b):
    imaginario = a[0] + b[0]
    inverso_imaginario =  -a[0] - b[0]
    return (inverso_imaginario)

#Multiplicación de un escalar por un vector complejo.

def escalar(a,b):
    vector = a[0] , b[0] 
    escalar = d[0]
    escalar_mult = d[0]*a[0] + d[0]*b[0] 
    return ( escalar_mult)

#Adición de matrices complejas.
def suma_matrices(a,b):
    matriz_1 = [[a[1,1] , a[1,2] , a[1,3]] , [a[2,1] , a[2,2] , a[2,3]]]
    matriz_2 = [[b[1,1] , b[1,2] , b[1,3]] , [b[2,1] , b[2,2] , b[2,3]]]
    suma_mat = [[a[1,1] + b[1,1] , a[1,2] + b[1,2] , a[1,3]+ b[1,3] ] , [a[2,1] + b[2,1] , a[2,2] + b[2,2] , a[2,3]+ b[2,3] ]]
    return (suma_mat)


#Multiplicación de un escalar por una matriz compleja.
def suma_matrices(a,b):
    matriz_1 = [[a[1,1] , a[1,2] , a[1,3]] , [a[2,1] , a[2,2] , a[2,3]]]
    escalar = d[0]
    multu_escala =  [[d[0]*a[1,1] , d[0]*a[1,2] , d[0]*a[1,3]] , [d[0]*a[2,1] , d[0]*a[2,2] , d[0]*a[2,3]]]
    return ( multu_escala)

#Transpuesta de una matriz/vector
def transpuesta(a,b):
    matriz_1 = [[a[1,1] , a[1,2] , a[1,3]] , [a[2,1] , a[2,2] , a[2,3]]]
    matriz_tansp = ([a[1,1] , a[2,1]] , [a[1,2] , a[2,2]] , [a[1,3] , a[2,3]])
    return (  matriz_tansp)



#Adjunta (daga) de una matriz/vector
def daga(a,b):
    matriz_1 = [[a[1,1] , a[1,2] , a[1,3]] , [a[2,1] , a[2,2] , a[2,3]], , [a[3,1] , a[3,2] , a[3,3]]]
    determinante1=  [[a[2,2] * a[3,3]] - [a[2,3]*a[3,2]]]
    determinante2=  [[a[2,1] * a[3,3]] - [a[3,1]*a[2,3]]]
    determinante3=  [[a[2,1] * a[3,2]] - [a[3,1]*a[2,2]]]
    determinante4=  [[a[1,2] * a[3,3]] - [a[3,2]*a[1,3]]]
    determinante5=  [[a[1,1] * a[3,3]] - [a[3,1]*a[1,3]]]
    determinante6=  [[a[1,1] * a[3,2]] - [a[3,1]*a[1,2]]]
    determinante7=  [[a[1,2] * a[2,3]] - [a[2,2]*a[1,3]]]
    determinante8=  [[a[1,1] * a[2,3]] - [a[2,1]*a[1,3]]]
    determinante9=  [[a[1,1] * a[2,2]] - [a[2,1]*a[1,2]]]
    matriz_daga = [determinante1 , determinante2 , determinante3] , [determinante4 , determinante5 , determinante6] , [determinante7 , determinante8 , determinante9]
    return (matriz_daga)

#Productor interno de dos vectores
def producto_interno(a,b):
    vector1 = a[0] , b[0] 
    vector2 = a[1] , b[1] 
    producto = a[0]*a[1] + a[0]*b[1] , b[0]*a[1] +b[0]*b[1] 
    return (producto)

#Norma de un vector
def norma(a,b):
    vector1 = a[0] , b[0] 
    norma =   (a[0]**2 + b[0]**2)**(1/2)
    return (norma)


#Revisar si una matriz es unitaria
def unitaria(a,b):

 matriz_1 = [[a[1,1] , a[1,2] , a[1,3]] , [a[2,1] , a[2,2] , a[2,3]], , [a[3,1] , a[3,2] , a[3,3]]]

  if (a[1,1] and a[2,2] and a[3,3]) = 1 and ([1,2] and  a[1,3] and  a[2,1] and  a[2,3] and  a[3,1] and a[3,2]) = 0:
    print("La matriz es unitaria ")
  else :
    print("La matriz no es unitaria")




