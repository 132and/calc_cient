from calculadora.__init__ import * #ou usar from python import* e depois do from colocar nome da pasta

def test_sum():
    assert sum(1, 2) == 3

def test_sum_chain():
    num1 = sum(1, 1)
    num2 = sum(2, 2)
    assert sum(num1, num2) == 6

def test_sub():
    assert sub(6, 3) == 3

def test_sub_chain():
    num1 = sub(2, -1)
    num2 = sub(5, 2)
    assert sub(num1, num2) == 0

def test_times():
    assert times(4, 3) == 12

def test_times_chain():
    num1 = times(1, 1)
    num2 = times(4, -3)
    assert times(num1, num2) == -12

def test_div():
    assert div(4, 2) == 2

def test_div_chain():
    num1 = div(18, 1)
    num2 = div(6, 2)
    assert div(num1, num2) == 6

def test_exp():
    assert exp(2, 2) == 4

def test_pi():
    assert pi(2) == 6.28

def test_pi_area():
    assert pi_area(6) == 113.04

def test_fac():
    assert fac(8) == 40320
   
def tes_log():
    assert log(3, 81) == 4

def tes_log_chain():
    assert log(81, 3) == 4


