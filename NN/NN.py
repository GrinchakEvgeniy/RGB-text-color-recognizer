import numpy as np


class NeuNet():

	def __init__(self, input_neural, hidden_neural, output_neural):

		np.random.seed(1)
		self.sinoptic_w1 = np.random.randn(input_neural, hidden_neural)
		self.sinoptic_w2 = np.random.randn(hidden_neural, output_neural)
		


	def __sigmoid(self, x):
		return 1 / (1 + np.exp(-x))


	def __relu(self, x):
		return np.maximum(x, 0)


	def forward(self, X):
		self.mult_weight1 = np.dot(X, self.sinoptic_w1) # multiplication input data and weight
		self.out_hidden = self.__sigmoid(self.mult_weight1) # activation function hidden layer

		self.mult_weight2 = np.dot(self.out_hidden, self.sinoptic_w2) # multiplication hidden data and weight
		predict = self.__sigmoid(self.mult_weight2) # final activation function output layer

		return predict


	def sigmoidPrime(self, s):
		#derivative of sigmoid
		return (s) * (1 - (s))


	def backward(self, input_data, predict_data, out_predict):
		# backward propagate through the network
		self.error_1 = predict_data - out_predict # error in output
		self.delta_1 = self.error_1*self.sigmoidPrime(out_predict) # applying derivative of sigmoid to error1

		self.error_2 = self.delta_1.dot(self.sinoptic_w2.T) #  how much our hidden layer weights contributed to output error
		self.delta_2 = self.error_2*self.sigmoidPrime(self.out_hidden) # applying derivative of sigmoid to error2

		self.sinoptic_w1 += input_data.T.dot(self.delta_2) # adjusting first set (input --> hidden) weights
		self.sinoptic_w2 += self.out_hidden.T.dot(self.delta_1) # adjusting second set (hidden --> output) weights

	def train(self, input_data, predict_data):
		out_predict = self.forward(input_data)
		self.backward(input_data, predict_data, out_predict)


	def test(self, X, y):
		out = self.forward(X)
		print('out result: ', out)
		print('actionally result: ', y)

	def save(self):
		np.savetxt("w1.txt", self.sinoptic_w1, fmt="%s")
		np.savetxt("w2.txt", self.sinoptic_w2, fmt="%s")