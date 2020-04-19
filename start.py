from pandas import read_csv 
import numpy as np
from NN.NN import NeuNet

data = read_csv('train_data.csv')
epochs = data.shape[0]
# Create an empty list 
list_input = [] 
list_output = []
# Iterate over each row 
for index, rows in data.iterrows(): 
	# Create list for the current row 
	list_i = [rows.red/255, rows.green/255, rows.blue/255] 
	list_o = [rows.textColor] 
	# append the list to the final list 
	list_input.append(list_i)
	list_output.append(list_o)

list_input = np.array((list_input), dtype=float)
list_output = np.array((list_output),dtype=float)

model = NeuNet(3, 10, 1)

for i in range(10):
	model.train(list_input, list_output)
model.save()
model.test(np.array(([25/255, 65/255, 40/255]), dtype=float), [1])