class Pizza:
    def __init__(self, starting_size='M', starting_toppings=set()):
        self.topping_set = set(starting_toppings)
        self.current_size = starting_size

    def __repr__(self):
        return f"Pizza('{self.current_size}',{self.topping_set})"

    def __eq__(self, p2):
        if self.current_size == p2.current_size and self.topping_set == p2.topping_set:
            return True
        else:
            return False

    def setSize(self, new_size):
        self.current_size = new_size

    def getSize(self) -> object:
        return self.current_size

    def addTopping(self, new_topping):
        self.topping_set.add(new_topping)

    def removeTopping(self, removed_topping):
        self.topping_set.discard(removed_topping)

    def price(self):
        if self.current_size == 'L':
            self.current_price = 12.95 + (1.85 * (len(self.topping_set)))
        elif self.current_size == 'M':
            self.current_price = 9.95 + (1.45 * (len(self.topping_set)))
        else:
            self.current_price = 6.25 + (.70 * (len(self.topping_set)))
        return self.current_price





def orderPizza():
    print('Welcome to Python Pizza!')
    current_size = input('What size pizza would you like (S,M,L): ')
    pie_toppings = set()
    x = True
    while x == True:
        new_topping = input('Type topping to add (or Enter to quit): ')
        if new_topping == '':
            break
        else:
            pie_toppings.add(new_topping)
    order = Pizza(current_size,pie_toppings)
    price = order.price()
    print("Thanks for ordering!")
    print("Your pizza costs ${}".format(price))
    return order





if __name__ == '__main__':
     import doctest

     print(doctest.testfile('hw8TEST.py'))
