import random as rand

def to_binary(number_decimal, number_of_inputs):
	i = number_of_inputs
	binary = str(bin(number_decimal)[2:])

	while(i > 0 and len(binary) < number_of_inputs):
		binary = '0' + binary
		i -= 1
	binary_with_spaces = " ".join(binary)
	return binary_with_spaces

def fill_truth_table(rows, columns):
	truth_table = [[False for _ in range(columns + 1)] for _ in range(rows)]

	for i in range(rows):
		index = 0
		input = to_binary(i, columns)
		split_input = input.split()
		for j in range(columns):
			if index < len(split_input):
				if split_input[index] == "0":
					truth_table[i][j] = False
				else:
					truth_table[i][j] = True
				index += 1
	return truth_table

def show_truth_table(rows, columns, operator, operation, truth_table):
	print(f"Truth table of the {operation} gate:\n")
	for i in range(columns - 1):
		print("|", get_letter(i), " "*(1 - len(get_letter(i))), end="")
	print(f"| {operator} |")

	for i in range(rows):
		print("| ", end="")
		for j in range(columns):
			if truth_table[i][j] == False:
				print("0 | ", end="")
			else: 
				print("1 | ", end="")
		print()

def get_row_values(row, columns, truth_table):
	values = []
	for j in range(columns):
		values.append(truth_table[row][j])
	return values

def all_or(values):
	result = False
	for v in values:
		result = result or v
	return result

def all_xor(values):
	result = False
	for v in values:
		result = result != v
	return result

def get_letter(number):
	ascii = number + 65
	letter = chr(ascii)
	return letter

def generate_truth_table(operator, number_of_inputs):
	number_of_rows = pow(2, number_of_inputs)
	truth_table = fill_truth_table(number_of_rows, number_of_inputs)

	match operator:
		case 0:  # And
			for i in range(number_of_rows):
				values = get_row_values(i, number_of_inputs, truth_table)  # Get all values from a row
				truth_table[i][number_of_inputs] = all(values) # Doing 'and' between all the values
			show_truth_table(number_of_rows, number_of_inputs + 1, "^", "and", truth_table)
		case 1:  # Or
			for i in range(number_of_rows):
				values = get_row_values(i, number_of_inputs, truth_table)  # Get all values from a row
				truth_table[i][number_of_inputs] = all_or(values)  # Doing 'or' between all the values
			show_truth_table(number_of_rows, number_of_inputs + 1, "v", "or", truth_table)
		case 3:  # Xor
			for i in range(number_of_rows):
				values = get_row_values(i, number_of_inputs, truth_table)   # Get all values from a row
				truth_table[i][number_of_inputs] = all_xor(values)  # Doing 'xor' between all the values
			show_truth_table(number_of_rows, number_of_inputs + 1, "⊕", "xor", truth_table)

generate_truth_table(0, 4)
