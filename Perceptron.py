import random

class TruthTable:
	def __init__(self, num_of_columns, operation):
		self.rows = pow(2, num_of_columns)
		self.columns = num_of_columns + 1
		self.operation = operation
		self.truth_table = [[False for _ in range(self.columns)] for _ in range(self.rows)]


	def to_binary(self, number_decimal):
		i = self.columns
		binary = str(bin(number_decimal)[2:])

		while(i > 0 and len(binary) < self.columns - 1):
			binary = '0' + binary
			i -= 1
		binary_with_spaces = " ".join(binary)
		return binary_with_spaces
	
	
	def get_letter(self, number):
		ascii = number + 65
		letter = chr(ascii)
		return letter
	

	def fill_truth_table(self):
		for i in range(self.rows):
			index = 0
			input = self.to_binary(i)
			split_input = input.split()
			for j in range(self.columns):
				if index < len(split_input):
					if split_input[index] == "0":
						self.truth_table[i][j] = False
					else:
						self.truth_table[i][j] = True
					index += 1


	def show_truth_table(self, operator, operation):
		print(f"Truth table of the {operation} gate:\n")
		for i in range(self.columns - 1):
			print("|", self.get_letter(i), " "*(1 - len(self.get_letter(i))), end="")
		print(f"| {operator} |")

		for i in range(self.rows):
			print("| ", end="")
			for j in range(self.columns):
				if self.truth_table[i][j] == False:
					print("0 | ", end="")
				else: 
					print("1 | ", end="")
			print()


	def get_row_values(self, row):
		values = []
		for j in range(self.columns - 1):
			values.append(self.truth_table[row][j])
		return values
	

	def all_or(self, values):
		result = False
		for v in values:
			result = result or v
		return result
	

	def all_xor(self, values):
		result = False
		for v in values:
			result = result != v
		return result
	

	def generate_truth_table(self):
		self.fill_truth_table()

		match self.operation:
			case 0:  # And
				for i in range(self.rows):
					values = self.get_row_values(i)  # Get all values from a row
					self.truth_table[i][self.columns - 1] = all(values) # Doing 'and' between all the values
				self.show_truth_table("^", "and")
			case 1:  # Or
				for i in range(self.rows):
					values = self.get_row_values(i)  # Get all values from a row
					self.truth_table[i][self.columns - 1] = self.all_or(values)  # Doing 'or' between all the values
				self.show_truth_table("v", "or")
			case 2:  # Xor
				for i in range(self.rows):
					values = self.get_row_values(i)   # Get all values from a row
					self.truth_table[i][self.columns - 1] = self.all_xor(values)  # Doing 'xor' between all the values
				self.show_truth_table("⊕", "xor")


class Perceptron:
	def __init__(self, number_of_inputs, operation):
		self.truth_table = TruthTable(number_of_inputs, operation)
		self.index_baias = number_of_inputs + 1
		self.weights = []
		self.output = []


	def create_wheights(self):
		for i in range(len(self.weights)):
			rand = random.uniform(-1, 1)
			self.weights.append(rand)

	
	#  def recalculate_weights(self):
	

	def train(self):
		sum_output = 1
		for i in range(len(self.weights)):
			sum_output += self.truth_table[i][j] * self.weights[i]


number_of_inputs = int(input("Enter the number of inputs for your truth table: "))
operation = int(input("Enter the operation that your truth table will perform. Type:\n 0 - For and\n 1 - For or\n 2 - For xor\n-> "))

perceptron = Perceptron(number_of_inputs, operation)
perceptron.create_wheights()