import pytest

from calc import soma, sub, mult, div

def test_soma():
	
	assert soma(2, 2) == 4
	assert soma(-4, 8) == 4
	assert soma(-4, '8') == 4


def test_sub():

	assert sub(5, 2) == 3
	assert sub(2, 2) == 0


def test_mult():
	
	assert mult(5, 5) == 25
	assert mult(3, 3) == 9


def test_div():
	assert div(6, 2) == 3
	assert div(4, 1) == 4

