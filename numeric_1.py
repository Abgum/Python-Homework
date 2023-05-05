
import numpy as np
from numpy.linalg import eig


StudentId="010200606"

print('GEO 221E – Numerical Methods for Geomatics Engineering, 2022 – 2023 Fall Term')

#A list is a one-dimensional data structure. Two-dimensional lists are known as matrices.

#Question_1  

#The product of a matrix from the right or left by its inverse is equal to the unit matrix. In order for a matrix to be inverted, it must be a square matrix.
#I got the inverse by calling the inv() function from the numpy library


Q_1_1 = np.array([[2, -17, 11],[-1, 11, -7],[0, 3, -2]])
print('\n\n\n',np.linalg.inv(Q_1_1 ), "\n\n is the inverse of \n\n", Q_1_1)

print("\n + + + + + + + + + + + + + + + + + + + + + + + +")

Q_1_2 = np.array([[1, 0, 0],[3, 4, 0],[2, 5, 5]])
print("\n", np.linalg.inv(Q_1_2 ), "\n\n" "is the inverse of" ,"\n\n", Q_1_2)

print("- - - - - - - - - - - - - - - - - - - - ")


#Question_2

#Determinant: It is the product of the diagonal elements with each other and the product of the remaining elements with each other.
#For sizes more than 2, you can use the np.linalg.inv() command directly in python. I also used it.

Q_2_1 = np.array([[4, 3, -2],[5, 4, 1],[-2, 3, 4]])
print("\n {:.4f} is the determinant of \n\n".format(np.linalg.det(Q_2_1)), Q_2_1 )

print("\n + + + + + + + + + + + + + + + + + + + + + + + +")

Q_2_2 = np.array([[1/2, 1, -5 ],[4, -1/4, -4], [3, 2, -2]])
print("\n {:.4f} is the determinant of \n\n".format(np.linalg.det(Q_2_2)) , Q_2_2 )

print("- - - - - - - - - - - - - - - - - - - - ")


#Question_3 

#The main built-in function in Python to solve the eigenvalue/eigenvector problem for a square array is the eig function in numpy.linalg


a = np.array([[-2,2,-3],[2,1,-6],[-1,-2,0]])
w,v=eig(a)

print('Eigenvalue:', w)

print("\n + + + + + + + + + + + + + + + + + + + + + + + +")


print('\nEigenvector', v)  

print("- - - - - - - - - - - - - - - - - - - - ")



#Question_4


print('Equations for iteration:')
print('x1 = (27 - 2x2 + x3) / 10') 
print('x2 = (-61.5 + 3x1 + 2x3)/ -6')
print('x3 = (-21.5 - x1 - x2) / 5')

x1 = 0.0
x2 = 0.0
x3 = 0.0
k = 0

#I defined our values as matrix in python with nested list method
matrix_0 = np.array([[x1],[x2],[x3]])
print('Inicial parameter: matrix')
print(matrix_0)


err_x1 = 1
err_x2 = 1
err_x3 = 1

#  I checked the number of digits after the comma of the values that come out with the while loop
while(err_x1 >= 0.00001 and err_x2 >= 0.00001 and err_x3 >= 0.00001):
    k1 = k + 1
    x1_1 = (27- 2*x2+ x3)/10
    x2_1 = ((-61.5 + 3*x1_1 + 2*x3)/(-6))
    x3_1 = (-21.5 - x1_1 - x2_1) / 5
    
    # Updating the errors' values
    err_x1 = abs((x1_1-x1))    
    err_x2 = abs((x2_1-x2))
    err_x3 = abs((x3_1-x3))
       
    # Updating variable's values
    k=k1
    x1=x1_1
    x2=x2_1
    x3=x3_1
    
    # Each iteration results:
    print('k=', k)
    print("x1={0} --> (err_x1={1:.4f})".format(x1,err_x1))
    print("x2={0} --> (err_x2={1:.4f})".format(x2,err_x2))
    print("x3={0} --> (err_x3={1:.4f})".format(x3,err_x3))
    
    print("\n + + + + + + + + + + + + + + + + + + + + + + + + \n")

    
    
# I got it to exit the loop when the condition is satisfied
    
else:
    
    print("The last iteration results: ", k)
    matrix_R = np.array(([x1],[x2],[x3]))
    print('Result: matrix ')
    print(matrix_R)




#Abdurrahim Gider
#010200606

  







