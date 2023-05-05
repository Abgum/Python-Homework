
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss

StudentId="010200606"

mean_mu=6
mean_sigma=1
bins =10

y= np.random.normal (mean_mu, mean_sigma, 5000)
x= np.random.normal (mean_mu, mean_sigma, 50)

plt.figure(figsize=(12,6))
histogram_for_x= plt.hist(x, bins, density=True, label="X",color='#c08081')
plt.title("Histogram of X")
plt.xlabel("X Values")
plt.ylabel(" Probability")
plt.legend(fontsize= 'xx-large', edgecolor="r")
plt.show()

plt.figure(figsize=(12,6))
histogram_for_y= plt.hist(y, bins, density=True, label="Y", color='#7bc2c5')
plt.title("Histogram of Y")
plt.xlabel("Y Values")
plt.ylabel("Probability")
plt.legend(fontsize= 'xx-large',edgecolor="r")
plt.show()

plt.figure(figsize=(12,6))
histogram_x= plt.hist(x, bins, density=True, alpha=0.6, label=u"X",edgecolor='None', color= 'b')
histogram_y= plt.hist(y, bins, density=True, alpha=0.6, label=u"Y",edgecolor='None', color= 'r')
plt.title("Histogram of X and Y")
plt.xlabel("Samples Mean")
plt.ylabel("Probability")
plt.legend(["X","Y"],fontsize= 'xx-large', edgecolor="pink")
plt.show()

plt.figure(figsize=(12,6))
x.sort()
pdf_for_x= ss.norm.pdf(x, mean_mu, mean_sigma)
cdf_for_x= ss.norm.cdf(x, mean_mu, mean_sigma)
cdf_pdf_histogram_x= plt.hist(x, bins, density=True, alpha=0.6 , label="X")
plt.plot (x, pdf_for_x, label="PDF X")
plt.plot (x, cdf_for_x, label="CDF X")
plt.title("Histogram, PDF and CDF of Random Variables")
plt.xlabel("Samples")
plt.ylabel("Probability")
plt.legend(fontsize= 'xx-large',edgecolor="pink")
plt.show()

plt.figure(figsize=(12,6))
y.sort()
cdf_for_y= ss.norm.cdf(y, mean_mu, mean_sigma)
pdf_for_y= ss.norm.pdf(y, mean_mu, mean_sigma)
cdf_pdf_histogram_y= plt.hist(y, bins, density=True, alpha=0.4, label="Y")
plt.plot (y, pdf_for_y, label="PDF Y", color='yellow')
plt.plot (y, cdf_for_y, label="CDF Y", color='green')
plt.title("Histogram, PDF and CDF of Random Variables")
plt.xlabel("Samples")
plt.ylabel("Probability")
plt.legend(fontsize= 'xx-large',edgecolor="pink")
plt.show()

mean_for_x= x.mean()
mean_for_y= y.mean()
std_for_x= x.std()
std_for_y= y.std()
print("Sample Mean and Standard Deviation of Variable X:", format(mean_for_x, ".3f"),"|", format(std_for_x, ".3f"))
print("Sample Mean and Standard Deviation of Variable Y:", format(mean_for_y, ".3f"),"|", format(std_for_y, ".3f"))



