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
