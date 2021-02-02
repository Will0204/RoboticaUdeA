import numpy as np
from copy import copy
import math

cos=np.cos; sin=np.sin; pi=np.pi


def dh(d, theta, a, alpha):
    #Calcular la matriz de transformacion homogenea asociada con los parametros D-H
    A = np.array([[np.cos(theta), -np.cos(alpha)*np.sin(theta) ,  np.sin(alpha)*np.sin(theta) ,  a*np.cos(theta)],
    		  [np.sin(theta),  np.cos(alpha)*np.cos(theta) , -np.sin(alpha)*np.cos(theta) ,  a*np.sin(theta)],
    		  [0            ,  np.sin(alpha)               ,  np.cos(alpha)               ,  d              ],
    		  [0            ,  0                           ,  0                           ,  1              ]])
    return A
    
    

def fkine_ur5(q):
    #Calcular la cinematica directa del robot UR5 dados 
    #sus valores articulares. 
    T1 = dh(0.0892  , q[0]         , 0     , np.pi/2 )
    T2 = dh(0       , q[1]          ,-0.425 , 0       )
    T3 = dh(0       , q[2]          ,-0.392 , 0       )
    T4 = dh(0.1093  , q[3]          , 0     , np.pi/2 )
    T5 = dh(0.09475 , q[4]          , 0     ,-np.pi/2 )
    T6 = dh(0.0825  , q[5]          , 0     , 0       )

    # Efector final con respecto a la base
    T = T1.dot(T2).dot(T3).dot(T4).dot(T5).dot(T6)
    return T


def jacobian_ur5(q, delta=0.0001):
    #Jacobiano analitico para la posicion. Retorna una matriz de 3x6 y toma como
    #entrada el vector de configuracion articular q=[q1, q2, q3, q4, q5, q6]

    # Alocacion de memoria
    J = np.zeros((3,6))
    # Transformacion homogenea inicial (usando q)
    T = fkine_ur5(q)

    # Iteracion para la derivada de cada columna
    for i in range(6):
        # Copiar la configuracion articular inicial
        dq = copy(q);
        
        # Incrementar la articulacion i-esima usando un delta
        dq[i] += delta

        # Transformacion homogenea luego del incremento (q+dq)
        Td = fkine_ur5(dq)
        # Aproximacion del Jacobiano de posicion usando diferencias finitas

        A=np.array([(Td[0,3]-T[0,3]),(Td[1,3]-T[1,3]),(Td[2,3]-T[2,3])])/delta
        
        J[0,i]=A[0]
        J[1,i]=A[1]
        J[2,i]=A[2]
        
    return J


def ikine_ur5(xdes, q0):
    #    Calcular la cinematica inversa de UR5 numericamente a partir de la configuracion articular inicial de q0. 

    epsilon  = 0.001
    max_iter = 2000
    delta    = 0.00001

    q  = copy(q0)
    
    for i in range(max_iter):
        Tq = fkine_ur5(q)
        Jinv = np.linalg.pinv(jacobian_ur5(q))
        fq = np.array([Tq[0,3],Tq[1,3],Tq[2,3]])
    
        q = q + Jinv.dot(xdes-fq)
        
    	if(np.linalg.norm(xdes-fq) < epsilon):
            break

    return q


