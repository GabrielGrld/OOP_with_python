#from file shirt.py we import the class Shirt
from shirt import Shirt  

shirt_one = Shirt('blue', 'L', 'short-sleeve', 45)
shirt_two = Shirt('red', 'S', 'long-sleeve', 70)

print (shirt_one.price)
print (shirt_two.color)

shirt_two.change_price(45)
print(f"Shirt two price is {shirt_two.price}")
