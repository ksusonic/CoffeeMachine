# Initial supplies: (Начальные запасы:)
water = 400  # ml of water
milk = 540  # ml of milk
coffee = 120  # g of coffee beans
cups = 9  # disposable cups
money = 550  # $ in cash

# Recipes (supply_ ...  1 - espresso, 2 - latte, 3 - cappuccino
water_1 = 250
coffee_1 = 16
money_1 = 4
water_2 = 350
milk_2 = 75
coffee_2 = 20
money_2 = 7
water_3 = 200
milk_3 = 100
coffee_3 = 12
money_3 = 6


def status():
    print('The coffee machine has:')
    print(water, 'of water')
    print(milk, 'of milk')
    print(coffee, 'of coffee beans')
    print(cups, 'of disposable cups')
    print(money, 'of money')


def buy_action():
    act = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ')
    global water
    global coffee
    global milk
    global coffee
    global money
    global cups

    if act == 'back':
        return 0
    if cups >= 1:
        if act == '1':
            if water < water_1:
                print('Sorry, not enough water!')
            elif coffee < coffee_1:
                print('Sorry, not enough coffee beans!')
            else:
                print('I have enough resources, making you a coffee!')
                water -= water_1
                coffee -= coffee_1
                cups -= 1
                money += money_1
        elif act == '2':
            if water < water_2:
                print('Sorry, not enough water!')
            elif milk < milk_2:
                print('Sorry, not enough milk!')
            elif coffee < coffee_2:
                print('Sorry, not enough coffee beans!')
            else:
                print('I have enough resources, making you a coffee!')
                water -= water_2
                milk -= milk_2
                coffee -= coffee_2
                cups -= 1
                money += money_2
        elif act == '3':
            if water < water_3:
                print('Sorry, not enough water!')
            elif milk < milk_3:
                print('Sorry, not enough milk!')
            elif coffee < coffee_3:
                print('Sorry, not enough coffee beans!')
            else:
                print('I have enough resources, making you a coffee!')
                water -= water_3
                milk -= milk_3
                coffee -= coffee_3
                cups -= 1
                money += money_3
    else:
        print('Sorry, not enough disposable cups!')


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


action = ''
# Beginning the program:
while action != 'exit':
    action = input('Write action (buy, fill, take, remaining, exit): ')
    if action == 'buy':
        buy_action()
    elif action == 'fill':
        fill_action()
    elif action == 'take':
        take_action()
    elif action == 'remaining':
        status()
