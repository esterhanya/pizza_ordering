
class PizzaBase:
    def getDescription(self):
        return self.__class__.__name__
    def getTotalCost(self):
        return self.__class__.cost


class Pizza(PizzaBase):
    def __init__(self, pizzaBase):
        self.component = pizzaBase
    def getTotalCost(self):
        return self.component.getTotalCost() + \
            PizzaBase.getTotalCost(self)
    def getDescription(self):
        return self.component.getDescription() + \
         ' ' + PizzaBase.getDescription(self)


class Dough (PizzaBase):
    cost = 20

class Tomato_sauce (Pizza):
    cost = 10
    def __init__(self, PizzaBase):
        Pizza.__init__(self, PizzaBase)

class Cheese (Pizza):
    cost = 10
    def __init__(self, PizzaBase):
        Pizza.__init__(self, PizzaBase)

class Olives(Pizza):
    cost = 1
    def __init__(self, PizzaBase):
        Pizza.__init__(self,PizzaBase)

class Mushrooms(Pizza):
    cost = 1
    def __init__(self, PizzaBase):
        Pizza.__init__(self, PizzaBase)

class Extra_Cheese(Pizza):
    cost = 2
    def __init__(self, PizzaBase):
        Pizza.__init__(self, PizzaBase)

class Onion(Pizza):
    cost = 1
    def __init__(self, PizzaBase):
        Pizza.__init__(self, PizzaBase)

class Tomatoes(Pizza):
    cost = 1
    def __init__(self, PizzaBase):
        Pizza.__init__(self, PizzaBase)

class Bulgarian_cheese(Pizza):
    cost = 3
    def __init__(self, PizzaBase):
        Pizza.__init__(self, PizzaBase)

class Corn(Pizza):
    cost = 2
    def __init__(self, PizzaBase):
        Pizza.__init__(self, PizzaBase)

class Tuna(Pizza):
    cost = 4
    def __init__(self, PizzaBase):
        Pizza.__init__(self, PizzaBase)

class Pineapple(Pizza):
    cost = 10
    def __init__(self, PizzaBase):
        Pizza.__init__(self, PizzaBase)


pizzaA = Tomato_sauce(Cheese(Corn(Tomatoes(Tuna(Dough())))))
print(pizzaA.getDescription().strip() +
  ": '$'" + str(pizzaA.getTotalCost()))

def main():
    menu = {1:Tomato_sauce,
     2:Cheese,
     3:Olives,
     4:Mushrooms,
     5:Extra_Cheese,
     6:Onion,
     7:Tomatoes,
     8:Bulgarian_cheese,
     9:Corn,
     10:Tuna,
     11:Pineapple}

    order = Dough()
    code = input("enter a number of topping or X to end")
    while code !="x":
        pass

main()