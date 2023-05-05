
import numpy as np
import matplotlib.pyplot as plt

mu= 0
x= np.linspace(0,2,200)
pdf_of_x= (5/32)*x**4
pdf_of_x= np.where(np.logical_and(x>0, x<=2), pdf_of_x,0)
cdf_of_x = np.cumsum(pdf_of_x)
plt.plot(x, cdf_of_x, label='CDF of X',color= '#ffa54f')
plt.title('Density Function')
plt.legend()
plt.xlabel('x axes')

y= np.linspace(0,2,200)
pdf_of_y= x**2 + mu
X= np.sqrt(y - mu) 
pdf_of_y= np.where(np.logical_and(X>0, X<=2),pdf_of_y,0)
cdf_of_y= np.interp(x**2 + mu, x, cdf_of_x)
plt.plot(y, cdf_of_y, label='CDF of Y',color='#68228b')
plt.legend()
plt.ylabel('y axes')
plt.show()
