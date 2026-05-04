import Lab2

print("Test_Lab2")


def test_find_min_max():
    result = []
    input_data = [1,2,3,4,5,6,7,8,9]

    result = Lab2.find_min_max(input_data)
    
    assert result == [1.0, 9.0]

def test_calc_average():
    result = []
    input_data = [1,2,3,4,5,6,7,8,9]

    result = Lab2.calc_average(input_data)

    assert result == 5.0

def test_calc_median_temperature():
    result = []
    input_data = [1,2,3,4,5,6,7,8,9]

    result = Lab2.calc_median_temperature(input_data)

    assert result == 5.0