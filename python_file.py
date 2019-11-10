import numpy as np 

x = [1,2,3,4,5]
y = [5,6,7,8,9]

#numpy dot product (multiply each element in both arrays then sum the products)
z_dot = np.dot(x,y)

#same function without numpy
z_test = sum(map((lambda x,y: x*y),x,y))

print(z_dot)
print(z_test)