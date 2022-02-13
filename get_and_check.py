def move_coordinates(layer_0, layer_2):
	maximum = float("-inf")
	result = 0
	for i in range(9):
		if layer_0[0][i] != 0:
			continue
		if layer_2[0][i] > maximum:
			maximum = layer_2[0][i]
			result = i
	return result

def sigmoid(x):
	return 1 / (1 + 2.71828 ** (-x))

def is_end(layer_0):
	if 0 in layer_0[0]:
		return False
	return True

def win_checking(a):
	a = a[0]
	for i in range(3):
		if (a[0 + 3 * i] == 1) and (a[1 + 3 * i] == 1) and (a[2 + 3 * i] == 1):
			return True
		if (a[0 + i] == 1) and (a[3 + i] == 1) and (a[6 + i] == 1):
			return True 
	if (a[0] == 1) and (a[4] == 1) and (a[8] == 1):
		return True
	if (a[2] == 1) and (a[4] == 1) and (a[6] == 1):
		return True
	return False

import numpy as np

opener = np.load('weights.npz')
print(opener.files)
weights_0_1 = opener['w01']
weights_1_2 = opener['w12']

field = np.array([[1, 0, 1], [0, 0, 0], [-1, 0, -1]])
layer_0 = np.array([field.flatten()])
layer_1 = sigmoid(np.dot(layer_0, weights_0_1))
layer_2 = sigmoid(np.dot(layer_1, weights_1_2))

if is_end(layer_0):
	print('standoff')
else:
	destination = move_coordinates(layer_0, layer_2)
	field[destination // 3][destination % 3] = 1
	if win_checking(np.array([field.flatten()])): #layer_0 current = np.array([field.flatten()])
		field_zeroing = True
		print('win')
print(field)
print(layer_2)