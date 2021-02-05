
from grades import compute_hw_average


def test_zero_grades():
    grades = []
    assert compute_hw_average(grades) == 0

def test_single_grade():
    grades = [42]
    assert compute_hw_average(grades) == 42

def test_two_grades():
    grades = [41,43]
    assert compute_hw_average(grades) == 42

def test_three_grades():
	# Test for 3 grades
	grades = [2,4,6]
	assert compute_hw_average(grades) == 4

def test_floating_point():
	# Test for 3 grades
	grades = [1.0,2.0,3.0]
	assert compute_hw_average(grades) == 2.0
