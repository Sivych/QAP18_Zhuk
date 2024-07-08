from functions import generate_natural_cubes

def test_0():
    assert generate_natural_cubes(2) == [1, 8]

def test_1():
    assert generate_natural_cubes(0) == [0]

def test_2():
    assert generate_natural_cubes(-1) == False

def test_3():
    assert generate_natural_cubes(2) == [1, 9]

def test_4():
    assert generate_natural_cubes(3) == [1, 8, 27]
