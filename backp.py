

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#sigmoid function
def nlinear(x,deriv=False):
  if(deriv==True):
    return x*(1-x)
  return 1/(1+np.exp(-x))

#input
X=np.array([[1,1,0],[0,1,1],[0,0,1],[1,1,0]])
#output
y=np.array([[1,0,0,1]]).T
#seed for random number distribution
#np.random.seed(1)
#wts initialization
synapse0=2*np.random.random((3,1))-1

for i in range(1000):
  #forward propagation
  layer0=X
  layer1=nlinear(np.dot(layer0,synapse0))
  #error
  layer1_error=y-layer1
  #multiply with error backpropagated
  layer1_delta=layer1_error*nlinear(layer1,True)
  #update wts
  synapse0+=np.dot(layer0.T,layer1_delta)

print("op:")
print(layer1)
print("ao:")
print(y)

df=[y,layer1]
df

plt.plot(y,layer1)













"""
Steps of Backpropagation
Step 1: Inputs X, arrive through the preconnected path.
Step 2: The input is modeled using true weights W. Weights are usually chosen randomly.
Step 3: Calculate the output of each neuron from the input layer to the hidden layer to the output layer.
Step 4: Calculate the error in the outputs Backpropagation Error= Actual Output – Desired Output
Step 5: From the output layer, go back to the hidden layer to adjust the weights to reduce the error.
Step 6: Repeat the process until the desired output is achieved.
"""

