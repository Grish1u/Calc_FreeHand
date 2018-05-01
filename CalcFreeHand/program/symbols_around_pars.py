from tools import add_str_digits
def check_symbols_around_asymbol(expression_string, symbol_char, before_bool):
	"""
		Args-
			arg1 - the string examined
			arg2 - can be either '(' or ')'
			arg3 - boolean - if True we examine the Before case, if False we examine the After case

		Throws - ValueError if arguments not correct
		
		Assumes - arg1 is string which is a mathematical expression
		
		Description - First it examines whether arguments are correct. Then it adds the allowed symbols inside a list. 
					Iterates through arg1. When it finds a same symbol as arg2, depending on arg3 it examines either
					the symbol before or the symbol after. If it finds the wrong symbol next to ( or ) it adds it to 
					the list of errors
		
		Returns - True if size of errors list is 0, False if size > 0
	"""
	#ARGUMENT ERROR HANDLING - TODO handle error for arg1
	if symbol_char != '(' and symbol_char != ')':
		print ('arg2 not ( nor )')
		raise ValueError
	if not isinstance(before_bool, bool):
		print ('arg3 not a boolean')
		raise ValueError
	# PART 1 - APPENDING THE ALLOWED CHARACTERS
	operators = ['+', '-', '*', '/'] # list of operators
	allowed_symbols = [' ']
	if symbol_char is '(':
		allowed_symbols.insert(0, '(') # goes on index 0
		if before_bool:
			for s in operators:
				allowed_symbols.append(s) 
		else:
			add_str_digits(allowed_symbols)
			allowed_symbols.append(operators[1]) # we can have something like (8*(-1)) thats why we enable the minus sign after open par
	elif symbol_char is ')':
		allowed_symbols.insert(0, ')') # goes on index 0
		if before_bool:
			add_str_digits(allowed_symbols)
		else:
			for s in operators:
				allowed_symbols.append(s) 
	else:
		print("ERROR - The symbol examined is neither '(' nor ')'")

	# PART 2 - EXAMINING FOR NOT ALLOWED CHARACTERS
	errors = []
	if before_bool: # examining the 'before' case here
		for i, s in enumerate(expression_string, start = 0):
			if i > 0 and s is allowed_symbols[0] and expression_string[i - 1] not in allowed_symbols:
				errors.append(expression_string[i - 1])
				print('-- Error with symbol ', str(expression_string[i - 1]), ' in position ', str(i-1))
	elif before_bool == False: # examining the 'after' case here
		for i, s in enumerate(expression_string, start = 0):
			if i < len(expression_string) - 1 and s is allowed_symbols[0] and expression_string[i + 1] not in allowed_symbols:
				errors.append(expression_string[i + 1])
				print('-- Error with symbol ', str(expression_string[i + 1]), ' in position ', str(i+1))
	else: 
		print("ERROR - Error with the given boolean argument")
	# Returning result based errors list
	# print('Errors: ' + str(len(errors)), ' errors found') # To support the programmer
	# print('allowed_symbols: ', str(allowed_symbols)) # To support the programmer
	if len(errors) > 0: # if list1 = [0, 1] then len(list1) = 2
		return False
	else:
		return True

# TESTING
"""while True:
	inp = input('examine: ')
	print()
	print('Case before (')
	check_symbols_around_asymbol(inp, '(', True)
	print()
	print('Case before )')
	check_symbols_around_asymbol(inp, ')', True)
	print()
	print('Case after (')
	check_symbols_around_asymbol(inp, '(', False)
	print()
	print('Case after )')
	check_symbols_around_asymbol(inp, ')', False)
	input()
"""