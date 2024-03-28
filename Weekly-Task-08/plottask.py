#plot that displays
#a histogram of a normal distribution of a 1000 values
#with a mean of 5 and standard deviation of 2
#and a plot of the function  h(x)=x3 in the range 0 to 10

#https://www.w3schools.com/python/matplotlib_histograms.asp
import numpy as np 
import matplotlib.pyplot as plt

#Make sure random numbers are the same each time and create histogram
np.random.seed(1)
random_histogram = np.random.normal(5, 2, 1000)

#Function and range from description
#https://www.w3schools.com/python/matplotlib_plotting.asp
xpoints = np.array(range(0,10))
h_of_x = xpoints * xpoints * xpoints

# Plot both on same graph
plt.hist(random_histogram, color='r', label='Normal Distrubution')
plt.plot(xpoints, h_of_x, color='g', label='H(x)=x^3')

# Fonts to be used at the heading and axis
#https://www.w3schools.com/python/matplotlib_labels.asp
font1 = {'family':'serif','color':'green','size':20}
font2 = {'family':'serif','color':'lightgreen','size':15}

plt.title('Week 08 - Plot Task', fontdict = font1)
plt.xlabel('X', fontdict = font2)
plt.ylabel('Y', fontdict = font2)
plt.legend()

plt.show()


