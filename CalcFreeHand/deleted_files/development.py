# DEVELOPER : grishak
# PROJECT STARTED ON 18/4/2018
import operations_module as oper
from stack import Stack

"""Globals"""
"""Methods"""
# adds digits to a list
def add_str_digits(alist):
	for x in range(0, 10):
		alist.append(str(x))
# adds the non numeric symbols to a list
def add_non_numeric_symbols(alist):
	non_numeric_chars = ['(', ')', '+' ,'-' ,'*' ,'/' ,'.', ' '] # last character is interval
	for char in non_numeric_chars:
		alist.append(char)

# 1/ - Determining whether all symbols are within the list of allowed characters 
# returns - True if all are within the legal character list, False if even 1 is not legal
# - works as planned
# - TODO - perform refractor:
# make a list with incorect chars - for each incorrect - add it to the list
# at the end - if list > 0 return false else return true
def correct_chars(given_string):
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
# 2/ - Check whether parenthesis are balanced
# - this function will assume that the string given contains only the legal characters found in the allowed_chars list,
# - thus it will asume the given string has passed correct_chars() as True
def check_bal_parenthesis(expression):
	""" Has 3 things to aknowledge:
	1 - opening parenthesis' number is the same as closing parenthesis
	2 - opening par should find its counter part to the right of it and vise versa
	3 - last unclosed parenthesis should be the first closed """
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
# 3/ - Checks whether two symbols from the range of +, -, *, /, ., interval repeat one after another
# seems its working but have a better look next time
# seen it from here: https://stackoverflow.com/questions/28867222/python-3-check-letters-in-string-with-the-next-letter
def check_repeated_symbols(expression):
	symbols = ['+', '-', '*', '/', '.', ' ']
	prev = ''
	for char in expression:
		if char in symbols:
			if char == prev:
				print('char ' , char, ' repeated')
				return False
		prev = char
	return True

# 4/ Check if the symbols around parenthesis are correct

# PROGRAM FLOW
#-------------------------------------------------------
#END PROGRAM FLOW
#-------------------------------------------------------
"""Testing"""
while True:
	user_input = input('Enter your equasion: ') #needs to go in program flow
# user input here for the testing purposes
	if correct_chars(user_input):
		print ('Correct characters')
	else:
		print('not Correct characters')
	if check_bal_parenthesis(user_input):
		print('Balanced parenthesis')
	else:
		print('Unbalanced parenthesis')
	if check_repeated_symbols(user_input):
		print('No repetition errors found')
	else:
		print('Uncorrect repetition found')

	input('Press enter: ')

#TODO
# To refractor functions check_s_bef_open_par() and heck_s_bef_closed_par(). Also they might be diagonally the sam with their opposite functions - afterstere


#not urgent TODO
# functionallity of the 'correc(given_string)' func can be upgraded so it showes all the not correct symbols