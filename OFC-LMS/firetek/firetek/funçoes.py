count = print

class printTest(object):
	def test (self):
		a = 5
		count(a)

pt = printTest()

pt.test()



#def contar(A):
#	return [len(x) for x in A]


lst = ['teste de python']

#print (contar(lst))

print ('Com lambda')
contar = lambda lst: [len(x) for x in lst]

print (contar(lst))

teste = list(map(lambda x: x**2, lst))