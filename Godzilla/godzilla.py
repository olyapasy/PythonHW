class Godzilla:
    def __init__(self, space, weight):
        self.space = space
        self.weight = weight

    def eat(self):
        print('----------------------------------------------------------------------')
        print('Space:                 %d' % self.space)
        print('Human weight:          %d' % self.weight)
        print('----------------------------------------------------------------------')
        percent = (self.weight * 100) / self.space
        if percent > 90:
            self.isFull(percent)
        else:
            while percent < 90:
                print("Godzilla wants more humans! His stomach full on %.2f percent. Feed him!" % percent)
                self.weight = self.weight + int(input("Enter the value of weight of new human : "))
                percent = (self.weight * 100) / self.space
                self.isFull(percent)

    def isFull(self, percent):
        is_full_stomatch = False
        if percent >= 90 and percent <= 100:
            print("Godzilla can`t eat humans anymore! His stomach is full on %.2f percent." % percent)
            is_full_stomatch = True
            return print(is_full_stomatch)
        elif percent < 90:
            print("Godzilla`s stomach is full on %.2f percent" % percent)
        else:
            print("Error! Godzilla can`t eat more than he have space in his stomach")
