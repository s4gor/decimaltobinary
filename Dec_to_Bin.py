class converter():
	
	a = int( input ('Enter the number you want to convert in binary: '))
	
	print('\nDecimal: {}'.format(a))
	
	def cnvt():
		b = []
		while (converter.a > 0):
			b.append(int(converter.a % 2))
			converter.a = int(converter.a / 2)
		return b
		
print('')

c = ("".join(map(str, converter.cnvt())))

print('Binary: ', end = '')

print(c[ : : - 1])