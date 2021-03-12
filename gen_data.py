""" 			  		 			     			  	   		   	  			  	
template for generating data to fool learners (c) 2016 Tucker Balch 			  		 			     			  	   		   	  			  	
Copyright 2018, Georgia Institute of Technology (Georgia Tech) 			  		 			     			  	   		   	  			  	
Atlanta, Georgia 30332 			  		 			     			  	   		   	  			  	
All Rights Reserved 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
Template code for CS 4646/7646 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
Georgia Tech asserts copyright ownership of this template and all derivative 			  		 			     			  	   		   	  			  	
works, including solutions to the projects assigned in this course. Students 			  		 			     			  	   		   	  			  	
and other users of this template code are advised not to share it with others 			  		 			     			  	   		   	  			  	
or to make it available on publicly viewable websites including repositories 			  		 			     			  	   		   	  			  	
such as github and gitlab.  This copyright statement should not be removed 			  		 			     			  	   		   	  			  	
or edited. 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
We do grant permission to share solutions privately with non-students such 			  		 			     			  	   		   	  			  	
as potential employers. However, sharing with other current or future 			  		 			     			  	   		   	  			  	
students of CS 7646 is prohibited and subject to being investigated as a 			  		 			     			  	   		   	  			  	
GT honor code violation. 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
-----do not edit anything above this line--- 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
Student Name: Sarah Hernandez			  		 			     			  	   		   	  			  	
GT User ID: shernandez43	 			     			  	   		   	  			  	
GT ID: 903458532  		 			     			  	   		   	  			  	
""" 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
import numpy as np 			  		 			     			  	   		   	  			  	
import math 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
# this function should return a dataset (X and Y) that will work 			  		 			     			  	   		   	  			  	
# better for linear regression than decision trees 			  		 			     			  	   		   	  			  	
def best4LinReg(seed=1489683273): 			  		 			     			  	   		   	  			  	
    np.random.seed(seed) 

    X = np.random.rand(100,4)
    Y = X[:, 0] + X[:,1]*3 + X[:,2]**2 - X[:,3]*4

    return X, Y 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
def best4DT(seed=1489683273): 			  		 			     			  	   		   	  			  	
    np.random.seed(seed) 
    X = np.random.rand(100,4)
    x1 = X[:,0]
    x2 = X[:,1]
    x3 = X[:,2]
    x4 = X[:,3]

    index = 0
    for i in x1:
        if i < x1.mean():
            x2[index] = i*5
        else:
            x2[index] = i*-5
        index += 1


    x3 = x1*x2+.2 

    index = 0
    for i in x1:
        if i > x1.mean() * 1.5:
            x4[index] = -1.5*i
        elif i > x1.mean():
            x4[index] = -i*.75
        elif i > x1.mean()/2:
            x4[index] = i*.5
        else:
            x4[index] = i*.25
        index += 1


    X[:,0] = x1
    X[:,1] = x2
    X[:,2] = x3
    X[:,3] = x4

    Y = X[:,0]*X[:,1]*X[:,2]*X[:,3]
      		 			     			  	   		   	  			  	
    return X, Y 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
def author(): 			  		 			     			  	   		   	  			  	
    return 'shernandez43' #Change this to your user ID 			  		 			     			  	   		   	  			  	
 			  		 			     			  	   		   	  			  	
if __name__=="__main__": 			  		 			     			  	   		   	  			  	
    print "they call me Tim." 			  		 			     			  	   		   	  			  	
