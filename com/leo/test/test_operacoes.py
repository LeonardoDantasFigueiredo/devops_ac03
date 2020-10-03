def func(k):
	return k + 11

def test_positivo():
	assert func(99) == 110

def test_negativo():
	assert func(-110) == -99

def test_zero():
	assert func(-11) == 0