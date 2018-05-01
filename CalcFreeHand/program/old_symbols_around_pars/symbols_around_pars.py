"""This module helps me Condense all 4 chech around pars funtions to 1 function"""

#the method add_str_digits is used  to append all the digits from 0 to 9 into a list
def add_str_digits(alist):
	for x in range(0, 10):
		alist.append(str(x))

"""THE FOLLOWING FOUR ARE THE BASE FUNCTIONS FOR FINDING ERRORS AROUND PARENTHESIS IN THE CALCULATOR PROGRAM"""
# Symbols around pars
#1
def check_s_bef_open_par(expression):
	""" The 'BEFORE' functions have to have:
	the statement i > 0 is to prevent decrementing to the last symbol. in python alist[-1] means the last item in the list"""
	allowed_symbols = ['+', '-', '*', '/', '(', ' '] # has an open par in the list
	errors = []
	for i, s in enumerate(expression, start = 0):
		if i > 0 and s is '(' and expression[i - 1] not in allowed_symbols:
			errors.append(expression[i - 1])
	print('before open pars errors size: ', len(errors), '\nbefore open pars errors size list: ', errors)
	if len(errors) > 0:
		return False
	else:
		return True
#2 
def check_s_bef_closed_par(expression):
	""" The 'BEFORE' functions have to have:
	the statement i > 0 is to prevent decrementing to the last symbol. in python alist[-1] means the last item in the list"""
	asb = [' ', ')'] # allowed symbols before
	add_str_digits(asb)
	errors = []
	for i, s in enumerate(expression, start = 0): 
		if i > 1 and s is ')' and expression[i - 1] not in asb: 
			errors.append(expression[i - 1])
	print('before closed pars errors size: ', len(errors), '\nbefore closed pars errors size list: ', errors)
	if len(errors) > 0:
		return False
	else:
		return True
#3
def check_s_after_open_par(expression):
	""" That's why since now its after we have the last symbol of the expression excluded from the loop"""
	asb = [' ', '('] # allowed symbols before
	add_str_digits(asb)
	errors = []
	for i, s in enumerate(expression, start = 0):
		if i < len(expression) - 1 and s is '(' and expression[i + 1] not in asb:
			errors.append(expression[i + 1])
	print('After open pars errors size: ', len(errors), '\nAfter open pars errors size list: ', errors)
	if len(errors) > 0:
		return False
	else:
		return True
#4
def check_s_after_closed_par(expression):
	""" That's why since now its after we have the last symbol of the expression excluded from the loop"""
	allowed_symbols = ['+', '-', '*', '/', ')', ' '] # has a closed par in
	errors = []
	for i, s in enumerate(expression, start = 0):
		if i < len(expression) - 1  and s is ')' and expression[i + 1] not in allowed_symbols:
			errors.append(expression[i + 1])
	print('After closed pars errors size: ', len(errors), '\nAfter closed pars errors size list: ', errors)
	if len(errors) > 0:
		return False
	else:
		return True 

def check_symbols_around_asymbol(expression_string, symbol_char, before_bool):
	# PART 1 - APPENDING THE ALLOWED CHARACTERS
	operators = ['+', '-', '*', '/'] # list of operators
	allowed_symbols = [' ']
	if symbol_char is '(':
		allowed_symbols.insert(0, '(') # goes on index 0
		#print('- ( appended to allowed_symbols')
		if before_bool:
			for s in operators:
				allowed_symbols.append(s) 
			#print('- Operators appended to allowed_symbols')
		else:
			add_str_digits(allowed_symbols)
			#print('- Digits appended to allowed_symbols')
	elif symbol_char is ')':
		allowed_symbols.insert(0, ')') # goes on index 0
		#print('- ) appended to allowed_symbols')
		if before_bool:
			add_str_digits(allowed_symbols)
			#print('- Operators appended to allowed_symbols')
		else:
			for s in operators:
				allowed_symbols.append(s) 
			#print('- Digits appended to allowed_symbols')
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
	print('Errors list size: ' + str(len(errors)))
	print('allowed_symbols: ', str(allowed_symbols))
	if len(errors) > 0: # if list1 = [0, 1] then len(list1) = 2
		return False
	else:
		return True





while True:
	inp = input('give expression: ')
	#print('Before (')
	#check_s_bef_open_par(inp)
	#print('Before )')
	#check_s_bef_closed_par(inp)
	print('- Before opened par')
	if check_symbols_around_asymbol(inp,'(', True):
		print("CORRECT")
		print()
	else:
		print("THERE IS AN ERROR")
		print()		
	print('- Before closed par')
	if check_symbols_around_asymbol(inp,')', True):
		print("CORRECT")
		print()
	else:
		print("THERE IS AN ERROR")
		print()
	print('- After opened par')
	if check_symbols_around_asymbol(inp,'(', False):
		print("CORRECT")
		print()
	else:
		print("THERE IS AN ERROR")
		print()
	print('- After closed par')
	if check_symbols_around_asymbol(inp,')', False):
		print("CORRECT")
		print()
	else:
		print("THERE IS AN ERROR")
		print()
	input('Enter to exit')

# TODO: THE REFRACTORED function check_errors_after_symbol(inp, not_chars , ')' ) not working properly when the closed par case
# the logic with after and before is wrong.