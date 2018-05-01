# DEVELOPER : grishak
# PROJECT STARTED ON 18/4/2018
import operations_module as oper

"""Globals"""
allowed_chars = [] # list of allowed chars
"""Methods"""
# adds digits to a list
def add_str_digits(alist):
	for x in range(0, 10):
		alist.append(str(x))
# adds the non numeric symbols to a list
def add_non_numeric_symbols(alist):
	non_numeric_chars = ['(', ')', '+' ,'-' ,'*' ,'/' ,'.']
	for char in non_numeric_chars:
		alist.append(char)

# 1/ - Determining whether all symbols are within the list of allowed characters 
# returns - True if all are within the legal character list, False if even 1 is not legal
# - works as planned
# - TODO - perform refractor:
# make a list with incorect chars - for each incorrect - add it to the list
# at the end - if list > 0 return false else return true
def char_correc(given_string):
	for char in given_string:
		print (char)
		if char not in allowed_chars:
			print('char ', char, ' not allowed')
			return False # it returns when it finds the first symbol- can be improved so it acknoledges all of the illegal symbols
		else:
			continue
	return True
# 2/ - Equasion builder function 
# - this function will assume that the string given contains only the legal characters found in the allowed_chars list
#def eqbuild(given_string):

# PROGRAM FLOW
#-------------------------------------------------------
# prepping accepted symbols, values
add_str_digits(allowed_chars)
add_non_numeric_symbols(allowed_chars)
# getting the user inputted equasion:
# user_input = input('Enter your equasion: ')
#END PROGRAM FLOW
#-------------------------------------------------------
"""Testing"""
while True:
	user_input = input('Enter your equasion: ') #needs to go in program flow
# user input here for the testing purposes
	if char_correc(user_input):
		print ('Correct')
	else:
		print('not Correct')

	print('allowed_chars[]: ','\n', allowed_chars)
#for char in user_input:
#	print(char)
	input('Press enter: ')

#TODO
# - correc function status: 
# appears that the only the first symbol determines correctness !!! 
# Problem found - we use tge return statement too early

#not urgent TODO
# functionallity of the 'correc(given_string)' func can be upgraded so it showes all the not correct symbols