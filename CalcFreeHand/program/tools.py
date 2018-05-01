def add_str_digits(alist):
	"""
		TODO: This function can be made private because it will be used only internally
			(In python I believe privates are written with undescore before its name - eg. _add_str_digits())
		
		Args -
			arg1 - a list

		Throws - ValueError if argument not a list

		Description - Adds the digits from 0 to 9 to a list as strings

	"""
	if not isinstance(alist, list):
		print ('arg not a list')
		raise ValueError

	for x in range(0, 10):
		alist.append(str(x))

# adds the non numeric symbols to a list
def add_non_numeric_symbols(alist):
	"""
		Args -
			arg1 - the list to which the non numeric characters will be added

		Assumes - The list contains all the characters allowed in a mathematical expression

		Throws - ValueError if argument not a list

		Description - Adds the non numeric symbols to a list

	"""
	if not isinstance(alist, list):
		print ('arg not a list')
		raise ValueError
	
	non_numeric_chars = ['(', ')', '+' ,'-' ,'*' ,'/' ,'.', ' '] # last character is interval
	for char in non_numeric_chars:
		alist.append(char)