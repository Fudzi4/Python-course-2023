import simple_math

def test_simple_math():
	assert simple_math.simple_add(1,5) == 6
	assert simple_math.simple_sub(5,2) == 3
	assert simple_math.simple_mult(4,2) == 8
	assert simple_math.simple_div(4,2) == 2
	assert simple_math.poly_first(2, 1, 4) == 9
	assert simple_math.poly_second(2, 1, 4, 2) == 17