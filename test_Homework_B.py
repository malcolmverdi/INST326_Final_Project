import pytest
import Homework_B


def test_calculate_tuition():
    assert Homework_B.calculate_tuition(0.0,) == 0.0
    assert Homework_B.calculate_tuition(1, True, False) == 822.00
    assert Homework_B.calculate_tuition(1, True, True) == 940.00
    assert Homework_B.calculate_tuition(1, False, False) == 1911.00
    assert Homework_B.calculate_tuition(1, False, True) == 2029.00
    assert Homework_B.calculate_tuition(8, True, False) == 3391.00
    assert Homework_B.calculate_tuition(8, True, True) == 4335.00
    assert Homework_B.calculate_tuition(8, False, False) == 12103.00
    assert Homework_B.calculate_tuition(8, False, True) == 13047.00
    assert Homework_B.calculate_tuition(9, True, False) == 4280.50
    assert Homework_B.calculate_tuition(9, True, True) == 5342.50
    assert Homework_B.calculate_tuition(9, False, False) == 14081.50
    assert Homework_B.calculate_tuition(9, False, True) == 15143.50
    assert Homework_B.calculate_tuition(11, True, False) == 5014.50
    assert Homework_B.calculate_tuition(11, True, True) == 6312.50
    assert Homework_B.calculate_tuition(11, False, False) == 16993.50
    assert Homework_B.calculate_tuition(11, False, True) == 18291.50
    assert Homework_B.calculate_tuition(12, True, False) == 5389.50
    assert Homework_B.calculate_tuition(12, True, True) == 6817.50
    assert Homework_B.calculate_tuition(12, False, False) == 18445.50
    assert Homework_B.calculate_tuition(12, False, True) == 19873.50
    assert Homework_B.calculate_tuition(15, True, False) == 5389.50
    assert Homework_B.calculate_tuition(15, True, True) == 6817.50
    assert Homework_B.calculate_tuition(15, False, False) == 18445.50
    assert Homework_B.calculate_tuition(15, False, True) == 19873.50

if __name__ == "__main__":
    pytest.main()
