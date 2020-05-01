class converter():
	
	a = int( input ('Enter the number you want to convert in binary: '))
	
	def cnvt():
		b = []
		while (converter.a > 0):
			b.append(int(converter.a % 2))
			converter.a = int(converter.a / 2)
		return b
		
print ('')
c = converter.cnvt()

print (*c[: : - 1])