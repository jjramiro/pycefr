yq  = interp1d(x_list, y_list, xq(nn))#interp1(output1(:,1),output1(:,2),xq(nn))
table[nn] = (\'%.2f\' %xq, \'%.2f\' %yq)

print(table)
#This script was written to test how to interpolate after data was created in a loop and stored as a list. Can a list be accessed explicitly like a vector in matlab?
#
from scipy.interpolate import interp1d
from math import *  #for ceil 
from astropy.table import Table #for Table
import numpy as np 
# define the initial conditions
x = 0               # initial x position
y = 0               # initial y position
Rmax = 10           # maxium range

""" initializing variables for plots"""
x_list = [x]
y_list = [y]

""" define functions"""
# not necessary for this MWE

"""create sample data for MWE"""
# x and y data are calculated using functions and appended to their respective lists
h = 1
t = 0
tf = 10
N=ceil(tf/h)

# Examle of interpolation without a loop: https://docs.scipy.org/doc/scipy/tutorial/interpolate.html#d-interpolation-interp1d
#x = np.linspace(0, 10, num=11, endpoint=True)
#y = np.cos(-x**2/9.0)
#f = interp1d(x, y)

for i in range(N):
    x = h*1
    y = cos(-x**2/9.0)

    """ appends selected data for ability to plot"""
    x_list.append(x)
    y_list.append(y)


## Interpolation after x- and y-lists are already created
intervals = 0.5
nfinal = ceil(Rmax/intervals)
NN = nfinal+1 # length of table
dtype = [(\'Range (units?)\', \'f8\'), (\'Drop? (units)\', \'f8\')]
table = Table(data=np.zeros(N, dtype=dtype))
for nn in range(NN):#for nn = 1:NN
    xq  = 0.0 + (nn-1)*intervals    #0.0 + (nn-1)*intervals
    yq  = interp1d(x_list, y_list, xq(nn))#interp1(output1(:,1),output1(:,2),xq(nn))
    table[nn] = (\'%.2f\' %xq, \'%.2f\' %yq)

print(table)
