# DEVELOPER : Grishak
# START DATE 18/4/2018
from correct_chars import correct_chars
from bal_parenthesis import check_bal_parenthesis
from symbols_repeated import check_repeated_symbols
from symbols_around_pars import check_symbols_around_asymbol
# imports are in the order of which functions were created

#TEST 1
"""while True:
	user_input = input('\nEnter your equasion: ') 
	# Are all characters are legal?
	print()
	if correct_chars(user_input):
		print ('correct_chars - True')
	else:
		print ('correct_chars - False')
	# Are parenthesis balanced?
	print()
	if check_bal_parenthesis(user_input):
		print('Balanced parenthesis - True')
	else:
		print('Balanced parenthesis - False')
	# Operator symbol repetition
	print()
	if check_repeated_symbols(user_input):
		print('Symbol repetition - Legal')
	else:
		print('Symbol repetition - Illegal')
	# Symbols around pars
	print()
	print('Case before (')
	check_symbols_around_asymbol(user_input, '(', True)
	print()
	print('Case before )')
	check_symbols_around_asymbol(user_input, ')', True)
	print()
	print('Case after (')
	check_symbols_around_asymbol(user_input, '(', False)
	print()
	print('Case after )')
	check_symbols_around_asymbol(user_input, ')', False)
	input('Press enter: ')"""
# TEST 2
while True:
	user_input = ''
	user_input = input('\nEnter your equasion: ')
	if correct_chars(user_input) and check_bal_parenthesis(user_input) and check_repeated_symbols(user_input) and check_symbols_around_asymbol(user_input, '(', True) and check_symbols_around_asymbol(user_input, ')', True) and check_symbols_around_asymbol(user_input, '(', False) and check_symbols_around_asymbol(user_input, ')', False):
		if len(user_input) > 1 :
			result = eval(user_input)
			print('Answer: ' + str(result))
		else:
			print('\nInput not a mathematical expression\nTry again\n')
	else:
		print('\nInput not a mathematical expression\nTry again\n')

	
