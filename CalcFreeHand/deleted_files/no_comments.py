import operations_module as oper
from stack import Stack

allowed_chars = []

def add_str_digits(alist):
	for x in range(0, 10):
		alist.append(str(x))
def add_non_numeric_symbols(alist):
	non_numeric_chars = ['(', ')', '+' ,'-' ,'*' ,'/' ,'.']
	for char in non_numeric_chars:
		alist.append(char)

def char_correc(given_string):
	for char in given_string:
		print (char)
		if char not in allowed_chars:
			print('char ', char, ' not allowed')
			return False 
		else:
			continue
	return True

def check_bal_parenthesis(expression):
	par_stack = Stack()
	for symbol in expression:
		if symbol is'(':
			par_stack.push(symbol)
		elif symbol is ')':
			if par_stack.isEmpty():
				return False
			elif par_stack.peek() is '(':
				par_stack.pop()
	if par_stack.isEmpty():
		return True
	else:
		print('stack is not empty')
		print(par_stack.toString())
		return False

add_str_digits(allowed_chars)
add_non_numeric_symbols(allowed_chars)


while True:
	user_input = input('Enter your equasion: ') 
	if char_correc(user_input):
		print ('Correct characters')
	else:
		print('not Correct characters')
	if check_bal_parenthesis(user_input):
		print('Balanced')
	else:
		print('Unbalanced')
	input('Press enter: ')