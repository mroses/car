class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self. mileage = mileage
        if price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        self.display_all()

    def display_all(self):
        print "Price: " + str(self.price) 
        print "Speed: " + str(self.speed)
        print "Fuel: " + str(self.fuel)
        print "Mileage: " + str(self.mileage)
        print "Tax: " + str(self.tax)

car1 = Car(5000, "60mph", "Full", "15mpg")
car2 = Car(3000, "50mph", "Not Full", "20mpg")
car3 = Car(11000, "80mph", "Full", "25mpg")
car4 = Car(2500, "50mph", "Not Full", "20mpg")
car5 = Car(1000, "35mph", "Not Full", "13mpg")
car6 = Car(3000, "50mph", "Full", "30mpg")



