import pytest
from cars import Car, get_cars, UserPref, CarSearch
import sys



def test_Car():
    """Test that the car class is initializing the car attributes correctly.
    
    """

    car_example = Car("nissan", "altima", 3, 3, 4, 3, 4, 2017)
    assert car_example.make == "nissan"
    assert car_example.model == "altima"
    assert car_example.year == 2017
    assert car_example.price == 3
    assert car_example.performance == 3
    assert car_example.reliability == 4
    assert car_example.luxury == 3
    assert car_example.fuel_economy == 4

def test_get_cars(example_cars):
    """Tests that the car data is being extracted correctly from the csv file.
    
    """

    assert len(example_cars) == 3
    assert isinstance(example_cars[0], Car)
    assert example_cars[0].make == "honda"

def test_UserPref():
    """Ensures that UserPref acurately stores user input.
    
    """
    pref = UserPref()
    pref.make = "honda"
    pref.model = "civic"
    pref.price = 3
    pref.performance = 3
    pref.reliability = 4
    pref.luxury = 3
    pref.fuel_economy = 4
    
    assert pref.make == "honda"
    assert pref.model == "civic"
    assert pref.price == 3
    assert pref.performance == 3
    assert pref.reliability == 4
    assert pref.luxury == 3
    assert pref.fuel_economy == 4

def test_CarSearch(example_cars):
    """Makes sure that cars are being matched correctly after a search occurs.
    
    """

    pref = UserPref()
    pref.make = "honda"
    pref.model = "civic"
    pref.price = 3
    pref.performance = 3
    pref.reliability = 4
    pref.luxury = 3
    pref.fuel_economy = 4
    
    car_search = CarSearch(example_cars)
    car_match = car_search.search(pref)

    assert len(car_match ) == 1
    assert car_match[0].make == "honda"
    assert car_match[0].model == "civic"



