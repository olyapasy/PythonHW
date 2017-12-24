
class Godzilla:
    BOUND_PERCENT = 90
    FULL_STOMACH_PERCENT = 100

    def __init__(self, space, weight):
        self.space = space
        self.weight = weight

    def eat(self):
        print('-----------------------------------------------------------------------')
        print('Space:                 %d' % self.space)
        print('Human weight:          %d' % self.weight)
        print('-----------------------------------------------------------------------')
        if self.is_full():
                print('I am full')
        else:
                self.weight += int(input("Enter the value of weight of new human : "))

    def is_full(self):
        return (self.weight * self.FULL_STOMACH_PERCENT) / self.space >= self.BOUND_PERCENT




