# Start amount of supplies: (Начальные запасы:)
water = 1200
milk = 540
coffee = 120
cups = 9
money = 550


def status():
    print('The coffee machine has:')
    print(water, 'of water')
    print(milk, 'of milk')
    print(coffee, 'of coffee beans')
    print(cups, 'of disposable cups')
    print(money, 'of money')


def buy_action():
    act = int(input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: '))
    global water
    global milk
    global coffee
    global cups
    global money
    if act == 1:
        water -= 250
        coffee -= 16
        money += 4
    elif act == 2:
        water -= 350
        milk -= 75
        coffee -= 20
        money += 7
    elif act == 3:
        water -= 200
        milk -= 100
        coffee -= 12
        money += 6
    cups -= 1


def fill_action():
    global water
    global milk
    global coffee
    global cups
    water += int(input('Write how many ml of water do you want to add: '))
    milk += int(input('Write how many ml of milk do you want to add: '))
    coffee += int(input('Write how many grams of coffee beans do you want to add: '))
    cups += int(input('Write how many disposable cups of coffee do you want to add: '))


def take_action():
    global money
    print('I gave you', money)
    money = 0


# Beginning the program:

status()
action = input('Write action (buy, fill, take): ')
if action == 'buy':
    buy_action()
elif action == 'fill':
    fill_action()
elif action == 'take':
    take_action()
status()
