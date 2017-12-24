from godzilla import Godzilla


running = True

def main():
        while running:
                print('-----------------------------------------------------------------------')
                space = int(input("Enter the value of space of Gorilla`s stomach: "))
                weight = int(input("Enter the value of weight of human: "))
                godzilla = Godzilla(space, weight)
                godzilla.eat()


if __name__ == '__main__':
    main()