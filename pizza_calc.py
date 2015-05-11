import math

class Pizza:

    def find_area(self):
        diameter = input("What was the diameter?, aka the size >>>")
        diameter = float(diameter)
        area = math.pi * ((diameter / 2) * (diameter / 2))
        return area

    def find_price(self):
        price = input("Okay, so how much did you pay for your pizza? >>>")
        price = float(price)
        if price > 25:
            print("Are you stupid?")
        elif price < 10:
            print("That's some cheap ass pizza.")
        price_inch = price / self.find_area()
        price_inch = round(price_inch, 2)
        print("You paid %s bucks an inch!" % (price_inch))

print("Hello! Let's figure out what you're paying for pizza, per square inch.")
pizza = Pizza()
pizza.find_price()
