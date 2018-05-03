def check_repeated_symbols(expression):
	"""
		TODO -
		
		Args-
			arg1 - the string examined
		
		Assumes - arg1 is string which is a mathematical expression
		
		Description - Checks for errors in symbol repeatition eg. ++ or -/ or *+ etc.
					eg. Cannot have this in a math expression: (1+*/2)
		Returns - True if no errors found, False if an error found

		Idea from - https://stackoverflow.com/questions/28867222/python-3-check-letters-in-string-with-the-next-letter
	"""
	symbols = ['+', '-', '*', '/', '.']
	prev = ''
	for char in expression:
		if char in symbols:
			if prev in symbols:
				print('char ' , char, ' repeated after ', prev)
				return False
		if char != ' ':
			prev = char
	return True
