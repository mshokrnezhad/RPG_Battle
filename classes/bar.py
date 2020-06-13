class bar:
	def __init__(self, current_value, max_value, number_of_blocks):
		self.current_value = current_value
		self.max_value = max_value
		self.max_number = number_of_blocks

	def get_bar(self):

		black_blocks = ""
		white_blocks = ""

		number_of_current_blocks = round((self.current_value/self.max_value)*self.max_number)

		for i in range(number_of_current_blocks):
			black_blocks += "█"

		for i in range(self.max_number-number_of_current_blocks):
			white_blocks += " "

		return black_blocks+white_blocks