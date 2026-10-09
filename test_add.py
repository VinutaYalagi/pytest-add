from add import add

def test_pos():
    assert add(10,20) == 30
def test_zero():
    assert add(10,0) == 10
def test_neg():
    assert add(-10,-20) == -30

