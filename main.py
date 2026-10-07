total_coins = 0
change = 0
# 0-cereal bar, 1-crisps, 2-chocolate_bar, 3-bottled_water
item_price = [["cereal bar", "50"], ["crisps", "60"], ["chocalate bar", "80"], ["bottled water", "90"]]
print("cereal bar-50p, crisps-60p, chocolate  bar-80p, bottled water-90p")



def accept_coins(): #accepts and counts coins
    total = total_coins

    coin = int(input("Enter a coin (10, 20, 50, 100): "))

    while coin != 0:
        if not(coin == 10 or coin == 20 or coin == 50 or coin == 100):
            print("Coin not accepted")

        else:
            total += coin
            if total >= 100:
                print(f"Total amount entered = £{float(total)/100}")
            else:
                print(f"Total amount entered = {total}p") 
        coin = int(input("Enter a coin (10, 20, 50, 100) or type 0 to stop entering coins: "))

    return total



def give_change(cost, total_entered): #Works out the amount of change owed
    change = 0
    if total_entered > cost:
        change = total_entered - cost

        if change >= 100:
            print(f"Your change is £{float(change)/100}")
        else:
            print(f"Your change is {change}p")

    elif total_entered < cost:

        if total_entered > 100:
            print(f"Not enough money entered. Refunded £{float(total_entered)/100}")
        else:
            print(f"Not enough money entered. Refunded {total_entered}p")

    else:
        print("No change")
    return change


def convert_change_to_coins(change): #Works out the changed owed in coins

    #Count of how many of each coin is given as change
    pounds = 0
    fifties = 0
    twenties = 0
    tens = 0

    pounds = change // 100
    change %= 100

    fifties = change // 50
    change %= 50

    twenties = change // 20
    change %= 20

    tens = change // 10
    change %= 10

    print(f"Your change is {pounds} £1 coins, {fifties} 50p coins, {twenties} 20p coins, {tens} 10p coins")





total_price = accept_coins()

item = int(input("Select an item (0-cereal bar, 1-crisps, 2-chocolate_bar, 3-bottled_water): "))

while not(item == 0 or item == 1 or item == 2 or item == 3):
    print("Not a button")
    item = int(input("Select an item (0-cereal bar, 1-crisps, 2-chocolate_bar, 3-bottled_water): "))


price = int(item_price[item][1])

print(f"Item costs {price}p")
  
change = give_change(price, total_price)


if change > 0:
    convert_change_to_coins(change)