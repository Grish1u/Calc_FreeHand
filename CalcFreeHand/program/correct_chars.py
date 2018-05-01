from tools import add_str_digits, add_non_numeric_symbols

def correct_chars(given_string):
	"""
		TODO - perform refractor:
			make a list with incorect chars - for each incorrect - add it to the list
			at the end - if list > 0 return false else return true
		
		Args-
			arg1 - the string examined 
		
		Assumes - arg1 - a string which is math expression
		
		Description - Checks whether the all symbols used in arg1 are allowed in a math expression
					- so it checks there is a symbol that's not in the list of allowed characters
		Returns - True if no errors found, False if an error found

	"""
	allowed_chars = [] # list of allowed chars
	add_str_digits(allowed_chars)
	add_non_numeric_symbols(allowed_chars)
	for char in given_string:
		#print (char)
		if char not in allowed_chars:
			print('char ', char, ' not allowed')
			return False # it returns when it finds the first symbol- can be improved so it acknoledges all of the illegal symbols
		else:
			continue
	return True
# 2/ - Check whethe