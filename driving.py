country = input('where are you from?')
age = input('what is your age?')
age = int(age)
if country == 'Taiwan':
	if age >= 18:
		print('you can drive in Taiwan')
	else:
		print('you cannot drive in Taiwan')
elif country == 'USA':
	if age >= 16:
		print('you can drive in USA')
	else:
		print('you cannot drive in USA')
elif country == 'UK':
	if age >= 17:
		print('you can drive in UK')
	else:
		print('you cannot drive in UK')
else:
	print("I don't know")