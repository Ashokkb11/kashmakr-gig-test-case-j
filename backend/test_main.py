import main

def test_price():
    res = main.calculate_price(100.0)
    assert res is not None
