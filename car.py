class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self. mileage = mileage
        #self.tax = tax
        
    def display_all(self):
        print "Price: $" + str(self.price)       
        print "Speed: " + str(self.speed)
        print "Fuel: " + str(self.fuel)
        print "Mileage: " + string(self.mileage)
        if price > 10000:
                price = price * .15
        else:
            price = price * .12
        return self

car1 = Car(5000, "60mph", "Full", "15mpg")
car2 = Car(3000, "50mph", "Not Full", "20mpg")
car3 = Car(9000, "80mph", "Full", "25mpg")
car4 = Car(2500, "50mph", "Not Full", "20mpg")
car5 = Car(1000, "35mph", "Not Full", "13mpg")
car6 = Car(3000, "50mph", "Full", "30mpg")
print car1.speed

