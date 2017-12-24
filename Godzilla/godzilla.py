BOUND_PERCENT = 90
FULL_STOMACH_PERCENT = 100
class Godzilla:

    def __init__(self, space, weight):
        self.space = space
        self.weight = weight

    def eat(self):
        print('-----------------------------------------------------------------------')
        print('Space:                 %d' % self.space)
        print('Human weight:          %d' % self.weight)
        print('-----------------------------------------------------------------------')
        percent = (self.weight * FULL_STOMACH_PERCENT) / self.space
        if percent > BOUND_PERCENT:
            self.is_full(percent)
        else:
            while percent < BOUND_PERCENT:
                print("Godzilla wants more humans! His stomach full on %.2f percent. Feed him!" % percent)
                self.weight = self.weight + int(input("Enter the value of weight of new human : "))
                percent = (self.weight * FULL_STOMACH_PERCENT) / self.space
                self.is_full(percent)

    def is_full(self, percent):
        is_full_stomach = False
        if percent >= BOUND_PERCENT and percent <= FULL_STOMACH_PERCENT:
            print("Godzilla can`t eat humans anymore! His stomach is full on %.2f percent." % percent)
            is_full_stomach = True
            return print(is_full_stomach)
        elif percent < BOUND_PERCENT:
            print("Godzilla`s stomach is full on %.2f percent" % percent)
        else:
            print("Error! Godzilla can`t eat more than he have space in his stomach")
