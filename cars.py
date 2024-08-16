"""Finds the best car for the user based on their preferences."""
import sys
import re
import csv



class Car:
    """Initializes the variables that each car will be based off of. Also gives the car descriptions a string 
    format to follow.
    
    Attributes:
        make(str): the brand of the car/company who manufactures it.
        model(str): the specific version of the car under the brand.
        price(int): a measurement for how much the car cost.
        performance(int): a measurement for how the car performs.
        reliability(int): gauges how reliabile and tough a car is.
        luxury(int): a measurement for how comfortable and luxorious a car is.
        fuel_economy(int): tells the user what kind of gas mileage they may get with a car.
        year(int): tells the user when the car was manufactured.
    
    """

    def __init__(self, make, model, year, price, performance, reliabiity, luxury, fuel_economy):

        self.make = str(make)
        self.model = str(model)
        self.price = int(price)
        self.performance = int(performance)
        self.reliability = int(reliabiity)
        self.luxury = int(luxury)
        self.fuel_economy = int(fuel_economy)
        self.year = str(year)
    
    
    def __str__(self):
        """Converts the attributes of a car to a string format for the user to read.

        Returns:
        string: a description of the car lisitng out its make, model, and all other attributes.

        """
        return (f"{self.make} {self.model}, {self.year}, Price rating: {self.price}, Performance: {self.performance}, Reliability: {self.reliability}, Luxury: {self.luxury}, Fuel_Economy: {self.fuel_economy}")
    
def get_cars(filename):
    """Opens a custom csv file and adds the cars within it to a list.
    
    Args:
        fiename(str): a file path
    
    Returns:
        list: a list of the car options based on the data in the file.
    
    """
    
    car_options = []
    
    with open (filename, 'r') as file:
        reader = csv.reader(file)
        next(reader, None)
        for line in file:
            cars = line.strip().split(',')
            if len(cars) == 8:
                make,model,price,performance,reliability,luxury,fuel_economy,year = cars
                make = make.lower()
                model = model.lower()
                year = year.strip()
                price = int(price)
                performance = int(performance)
                reliability = int(reliability)
                luxury = int(luxury)
                fuel_economy = int(fuel_economy)
                car = Car(make, model, year, price, performance, reliability, luxury, fuel_economy)
                car_options.append(car)
        return car_options

class UserPref:
    """Deals with the preferences of the user and the ratings they would like for each attribute of a car.
    
    """

    def __init__(self):

        self.make = None
        self.model = None
        self.price = None
        self.performance = None
        self.reliability = None
        self.luxury = None
        self.fuel_economy = None
    
    def get_rating(self, attribute):
        """Takes an integer input for each attribute between one and five.
            
            Args:
                attribute(str): a specific characteristic of a car.
            
            Returns:
                int: the rating the user entered for an attribute.
        
        """

        while True:
            try:
                rating = input(f"Please enter a rating of 1-5 for {attribute}.").strip()
                if re.match(r'^[1-5]$', rating):
                    return int(rating)
                else:
                    raise ValueError
            except:
                ValueError ("Please enter an integer between 1 and 5 inclusive.")
            
            
    def get_pref(self):
        """Asks for the user's preferences for make and model, and also gets the ratings from get_rating.
        
        """
        
        self.make = str(input("If you have a desired brand, please enter it here: ").strip().lower()) or None
        self.model = str(input("If you have a desired model, please enter it here: ").strip().lower()) or None
        
        self.price = self.get_rating("price ")
        self.performance = self.get_rating("performance ")
        self.reliability = self.get_rating("reliability ")
        self.luxury = self.get_rating("luxury ")
        self.fuel_economy = self.get_rating("fuel_economy ")

    
class CarSearch:
    """Uses the UserPref data to see which cars match their criteria the best.
    
    """

    def __init__(self, cars):

        self.cars = cars
    
    def search (self, pref):
        """Assigns points to each car that matches a piece of the user's preferences.
        
            Args:
                pref(str): used to assign attributes to a user's choices.
            
            Returns:
                list: a list of cars that match the user's criteria the most in decending order.
        
        """
        
        car_matches = []

        for car in self.cars:
            matches = 0

            if pref.make and car.make == pref.make:
                matches += 1
            if pref.model and car.make == pref.model:
                matches += 1
            if pref.price == car.price:
                matches += 1
            if pref.performance == car.performance:
                matches += 1
            if pref.reliability == car.reliability:
                matches += 1
            if pref.luxury == car.luxury:
                matches += 1
            if pref.fuel_economy == car.fuel_economy:
                matches += 1
            if matches >= 2:
                car_matches.append((matches, car))
        
        return [car for _, car in sorted(car_matches, key= lambda x: x[0], reverse=True)]

    def search_results(self, car_matches):
        """Displays the results of the user's search.
            
            Args:
                car_matches(list): a list of cars that matches the user's preferences.
            
        """

        if car_matches:
            print("\nThese cars are the best matches for your preferences: ")
            for car in car_matches:
                print(car)
        else:
            print("Your preferences do not match any cars, please adjust values and try again.")



def main():
   """Takes the user through each step of the car finding process while asking for additional inputs along the way.
   
   """
   
   print("Welcome to CarFinder.")
   cars = get_cars("car_options.csv")
   car_search = CarSearch(cars)
   

   while True:
        pref = UserPref()
        pref.get_pref()
        car_matches = car_search.search(pref)
        car_search.search_results(car_matches) 

        adjust = input("Would you like to adjust your search? (yes/no): ").strip().lower()
        if adjust == "yes":
            continue
        if adjust == "no":

            desired_make = input("Please enter the make of the car you want: ").strip().lower()
            desired_model = input("Please enter the model of the car you want: ").strip().lower()
            
            selected_car = None
            for car in cars:
                if car.make.lower() == desired_make and car.model.lower() == desired_model:
                    selected_car = car
                    break
            
            if selected_car:
                print(f"Congratulations! You have found your dream car: {selected_car.make} {selected_car.model}, {selected_car.year}")
            else:
                print(f"Please try again. {selected_car.make} {selected_car.model} is not a valid option.")
            break

        else:
            if adjust != "yes" and adjust != "no":
                print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()





        
        



    