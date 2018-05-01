from stack import Stack
def check_bal_parenthesis(expression):
	"""
		TODO - 
		
		Args-
			arg1 - the string examined
		
		Assumes - arg1 is string which is a mathematical expression
		
		Description - Checks whether all the parenthesis in a math expression are balanced.
					eg. You can have : (()()) but you can't have ()) or )(
					- Mechanism 
						Makes sure: 1 - opening parenthesis' number is the same as closing parenthesis
									2 - opening par should find its counter part to the right of it and vise versa
									3 - last unclosed parenthesis should be the first closed
						...
					
		Returns - True if no errors found, False if an error found

		Idea from - A video in youtube. (can't remember the name atm)
	"""
	unbal_par = Stack()
	for symbol in expression:
		if symbol is'(':
			unbal_par.push(symbol)
		elif symbol is ')':
			if unbal_par.isEmpty():
				return False
			elif unbal_par.peek() is '(':
				unbal_par.pop()
	if unbal_par.isEmpty():
		return True
	else:
		print('bal_par stack is not empty')
		print(unbal_par.toString())
		return False
	
	# PSEUDO CODE 
	# create STACK 
	# SCAN the expression from left to right
	# if expresion[index i] is opening par:
	#	push[i] to the STACK
	# elif expresion[index i] is closing par:
	# 	if STACK is empty OR TOP not pair with expression[index i] <- this is when we have different types of parenthesis
	#		return False
	# else POP
	# when scanning is over if stack empty - return True, else return False