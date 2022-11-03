from times import compute_overlap_time, time_range
import pytest
def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_time_not_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 10:20:01",2,120)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 120)
    result = compute_overlap_time(large, short)
    expected = []
    assert result == expected

def test_several_ranges_overlap():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 10:20:00",3,120)
    short = time_range("2010-01-12 10:10:00", "2010-01-12 10:20:00", 3, 120)
    result = compute_overlap_time(large, short)
    expected = [('2010-01-12 10:10:00', '2010-01-12 10:12:00'), ('2010-01-12 10:14:40', '2010-01-12 10:16:00'), ('2010-01-12 10:18:00', '2010-01-12 10:20:00')]
    assert result == expected

def test_right_start():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 10:20:00")
    short = time_range("2010-01-12 10:20:00", "2010-01-12 10:45:00")
    result = compute_overlap_time(large, short)
    expected = []
    assert result == expected

def test_backwards_time_range():
    with pytest.raises(ValueError) as err:
        backwards_time = time_range("2010-01-12 10:30:00", "2010-01-12 10:20:00")
