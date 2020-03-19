# Вариант ООП с поддержкой нескольких обьектов (машин)
class CoffeeMachine:

    def __init__(self):
        self.water = 400  # ml of water
        self.milk = 540  # ml of milk
        self.coffee = 120  # g of coffee beans
        self.cups = 9  # disposable cups
        self.money = 550  # $ in cash

    def take(self):
        job = input('Write action (buy, fill, take, remaining, exit): ')
        if job == 'buy':
            act = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
            self.buy_action(act)
        elif job == 'fill':
            self.fill_action()
        elif job == 'take':
            self.take_action()
        elif job == 'remaining':
            self.__repr__()
        elif job == 'exit':
            global tag
            tag = False

    def __repr__(self):
        print('The coffee machine has:')
        print(self.water, 'of water')
        print(self.milk, 'of milk')
        print(self.coffee, 'of coffee beans')
        print(self.cups, 'of disposable cups')
        print(self.money, 'of money')

    def buy_action(self, act):

        if act == 'back':
            self.take()
        if self.cups >= 1:
            if act == '1':
                if self.water < 250:
                    print('Sorry, not enough water!')
                elif self.coffee < 16:
                    print('Sorry, not enough coffee beans!')
                else:
                    print('I have enough resources, making you a coffee!')
                    self.water -= 250
                    self.coffee -= 16
                    self.cups -= 1
                    self.money += 4
            elif act == '2':
                if self.water < 350:
                    print('Sorry, not enough water!')
                elif self.milk < 75:
                    print('Sorry, not enough milk!')
                elif self.coffee < 20:
                    print('Sorry, not enough coffee beans!')
                else:
                    print('I have enough resources, making you a coffee!')
                    self.water -= 350
                    self.milk -= 75
                    self.coffee -= 20
                    self.cups -= 1
                    self.money += 7
            elif act == '3':
                if self.water < 200:
                    print('Sorry, not enough water!')
                elif self.milk < 100:
                    print('Sorry, not enough milk!')
                elif self.coffee < 12:
                    print('Sorry, not enough coffee beans!')
                else:
                    print('I have enough resources, making you a coffee!')
                    self.water -= 200
                    self.milk -= 100
                    self.coffee -= 12
                    self.cups -= 1
                    self.money += 6
        else:
            print('Sorry, not enough disposable cups!')

    def fill_action(self):
        self.water += int(input('Write how many ml of water do you want to add: '))
        self.milk += int(input('Write how many ml of milk do you want to add: '))
        self.coffee += int(input('Write how many grams of coffee beans do you want to add: '))
        self.cups += int(input('Write how many disposable cups of coffee do you want to add: '))

    def take_action(self):
        print('I gave you', self.money)
        self.money = 0


# Main
machine1 = CoffeeMachine()
tag = True

while tag:
    machine1.take()

# Даня помоги
