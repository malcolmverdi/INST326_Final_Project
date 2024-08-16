import pytest
import Homework_C

def test_get_fret():
    assert Homework_C.get_fret('D', 'D') == 0
    assert Homework_C.get_fret('A', 'C') == 9
    assert Homework_C.get_fret('C', 'A') == 3
    assert Homework_C.get_fret('G#', 'Ab') == 0


def test_get_frets():
    assert Homework_C.get_frets('A', ['G']) == 2
    assert len(Homework_C.get_frets('A', ['G'])) == 1
    get_frets_test = Homework_C.get_frets('A', ['E', 'D', 'A'])
    assert get_frets_test ('A', ['E']) == 5
    assert get_frets_test ('A', ['D']) == 7
    assert get_frets_test ('A', ['A']) == 0
    assert len(Homework_C.get_frets('A', ['G#', 'D', 'A'])) == 3

if __name__ == "__main__":
    pytest.main()



