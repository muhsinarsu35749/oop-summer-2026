class Toy:
    def __init__(self, size, color):
        self.size = size
        self.color = color

toy1 = Toy("large", "Red")
toy2 = Toy("Medium", "Blue")

print(f"Size Of Toy 1 is {toy1.size}")
print(f"Color Of Toy 2 is {toy2.color}")