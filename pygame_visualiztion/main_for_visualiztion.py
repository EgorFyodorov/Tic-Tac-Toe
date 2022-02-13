import numpy as np 

def sigmoid(x):
	return 1 / (1 + 2.71828 ** x)

def dx_sigmoid(x):
	return x * (1 - x)

def primary_education(layer_0, layer_2):
	layer_2_error = np.zeros((1, 9))
	layer_2_delta = np.zeros((1, 9))

	for i in range(9):
		if layer_0[0][i] != 0:
			layer_2_error[0][i] = layer_2[0][i] * layer_2[0][i]
			layer_2_delta[0][i] = layer_2[0][i]
	return layer_2_error, layer_2_delta

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


np.random.seed(1)
field = np.zeros((3, 3))

alpha = 0.2
hidden_size = 12
weights_0_1 = 2 * np.random.random((9, hidden_size)) - 1
weights_1_2 = 2 * np.random.random((hidden_size, 9)) - 1
current_player = -1
game_number = 0
move_number = 0

def main_part():
	global field, current_player, weights_1_2, weights_0_1, game_number, move_number
	field_zeroing = False
	current_player *= -1
	field = field * (-1)
	layer_0 = np.array([field.flatten()])
	layer_1 = sigmoid(np.dot(layer_0, weights_0_1))
	layer_2 = np.dot(layer_1, weights_1_2)
	layer_2_error, layer_2_delta = primary_education(layer_0, layer_2)

	if is_end(layer_0):
		field_zeroing = True
		#print('standoff')
	else:
		destination = move_coordinates(layer_0, layer_2)
		field[destination // 3][destination % 3] = 1
		move_number += 1
		if win_checking(np.array([field.flatten()])): #layer_0 current = np.array([field.flatten()])
			layer_2_error[0][destination] = (layer_2[0][destination] - 1) ** 2
			layer_2_delta[0][destination] = layer_2[0][destination] - 1
			field_zeroing = True
			#print('win')

	layer_1_delta = layer_2_delta.dot(weights_1_2.T) * dx_sigmoid(layer_1)

	weights_1_2 -= alpha * layer_1.T.dot(layer_2_delta)
	weights_0_1 -= alpha * layer_0.T.dot(layer_1_delta)
	#print('current_player', current_player)
	#print(field)
	#print()
	if field_zeroing:
		field = np.zeros((3, 3))
		game_number += 1
	return field * (current_player), move_number, game_number, np.around(layer_2_error, decimals = 1)