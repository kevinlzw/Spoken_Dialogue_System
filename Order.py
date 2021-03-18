class Order:

    def __init__(self, pizza=None, crust=None, size=None):
        self.pizza = pizza
        self.crust = crust
        self.size = size
        self.topping = []
        self.phone = None
        self.delivery_type = None

    def fillAttribute(self, value):
        for key in value:
            if key == 'pizza':
                if value[key] == 'hawaiian':
                    self.topping.append('pineapple')
                    self.topping.append('ham')
                    self.topping.append('mozzarella')
                elif value[key] == 'meat lovers':
                    self.topping.append('pepperoni')
                    self.topping.append('ham')
                    self.topping.append('bacon')
                    self.topping.append('sausage')
                    self.topping.append('mozzarella')
                elif value[key] == '4 cheese':
                    self.topping.append('mozzarella')
                    self.topping.append('cheddar')
                    self.topping.append('swiss')
                    self.topping.append('provolone')
                elif value[key] == 'veggie supreme':
                    self.topping.append('mozzarella')
                    self.topping.append('green peppers')
                    self.topping.append('red onions')
                    self.topping.append('mushrooms')
                    self.topping.append('black olives')
                elif value[key] == 'vegan':
                    self.topping.append('green peppers')
                    self.topping.append('red onions')
                    self.topping.append('mushrooms')
                    self.topping.append('black olives')
            else:
                setattr(self, key, value[key])

    def __str__(self):
        if self.pizza:
            return '{} {} pizza with {} crust and {} toppings.'.format(self.size, self.pizza, self.crust, ','.join(self.topping))
        else:
            return '{} pizza with {} crust and {} toppings.'.format(self.size, self.crust, ','.join(self.topping))

    def ifOrderStarted(self):
        return not (
                not self.pizza and not self.crust and not self.size and not self.topping and not self.phone and not self.delivery_type and not self.address)

    def ifOnlyPhone(self):
        return self.phone and (
                not self.pizza and not self.crust and not self.size and not self.topping and not self.delivery_type and not self.address)

    def ifPhoneFilled(self):
        return self.phone is not None

    def NotFilledAttribute(self):
        if not self.topping:
            return 'topping'
        elif not self.crust:
            return 'crust'
        elif not self.size:
            return 'size'
        elif not self.delivery_type:
            return 'delivery_type'
        elif not self.phone:
            return 'phone'
        return
