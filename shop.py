Products = [
    ["Black T-shirt (number 1)", 105, 75],
    ["White T-shirt (number 2)", 105, 85],
    ["Gray T-shirt (number 3)", 105, 80]
    ]

print ("Welcome to the T-shirt shop. Everything here is oversize and unisex. I invite you to choose products :)\n")

for productName, price, quantity in Products:
    print("Product name:", productName)
    print("Price:", price)
    print("In stock:", quantity)
    print("\n")

how_many = 0
how_many2 = 0
how_many3 = 0

decision = True
while decision == True:
    choice = input("T-Shirt number: ")
    if choice == "1":
        print("The price is:", Products[0][1], "PLN/net", "In stock: ", Products[0][2])
        if choice == "1":
            how_many = int(input("How many pieces?: "))
            print("The price is: ", Products[0][1] * how_many)
            print("And then in stock: ", Products[0][2] - how_many)
    if choice == "2":
        print("The price is:", Products[1][1], "PLN/net", "In stock: ", Products[1][2])
        if choice == "2":
            how_many2 = int(input("How many pieces?: "))
            print("The price is: ", Products[1][1] * how_many2)
            print("And then in stock: ", Products[1][2] - how_many2)
    if choice == "3":
        print("The price is:", Products[2][1], "PLN/net", "In stock: ", Products[2][2])
        if choice == "3":
            how_many3 = int(input("How many pieces?: "))
            print("The price is: ", Products[2][1] * how_many3)
            print("And then in stock: ", Products[2][2] - how_many3)

    decision = input("Do you want to continue (yes/no): ")
    if decision == "yes":
        decision = True
    elif decision == "no":
        decision = False
        break
    else:
        print('Wrong answer!')
        decision = input("Do you want to continue (Yes/No): ")

print("Ok!")

actual_price = Products[0][1] * how_many
actual_price2 = Products[1][1] * how_many2
actual_price3 = Products[2][1] * how_many3

actual_quantity = Products[0][2] - how_many
actual_quantity2 = Products[1][2] - how_many2
actual_quantity3 = Products[2][2] - how_many3

how_many_r = 0
how_many_r2 = 0
how_many_r3 = 0

decision2 = input ("Do you want to remove something? yes/no: ")
if decision2 == "yes":
    decision2 = True
elif decision2 == "no":
    decision2 = False
else:
    print ("Wrong answer!")
    decision2 = input("Do you want to remove something? yes/no: ")

while decision2 == True:
    choice2 = input("T-Shirt number: ")
    if choice2 == "1":
        print("The price is:", Products[0][1], "PLN/net", "In stock: ", actual_quantity)
        if choice2 == "1":
            how_many_r = int(input("How many pieces?: "))
            print("The price is: ", int(actual_price) - (Products[0][1] * how_many_r))
            print("And then in stock: ", actual_quantity + how_many_r)
    if choice2 == "2":
        print("The price is:", Products[1][1], "PLN/net", "In stock: ", actual_quantity2)
        if choice2 == "2":
            how_many_r2 = int(input("How many pieces?: "))
            print("The price is: ",  int(actual_price2) - (Products[0][1] * how_many_r2))
            print("And then in stock: ", actual_quantity2 + how_many_r2)
    if choice2 == "3":
        print("The price is:", Products[2][1], "PLN/net", "In stock: ",ActualQuantity3)
        if choice2 == "3":
            how_many_r3 = int(input("How many pieces?: "))
            print("The price is: ",  int(actual_price3) - (Products[0][1] * how_many_r3))
            print("And then in stock: ", actual_quantity3 + how_many_r3)

    decision2 = input("Do you want to remove something? yes/no: ")
    if decision2 == "yes":
        decision2 = True
    elif decision2 == "no":
        decision2 = False
        break

tb1_price = Products[0][1] * (how_many - how_many_r)
tb2_price = Products[1][1] * (how_many2 - how_many_r2)
tb3_price = Products[2][1] * (how_many3 - how_many_r3)

VAT = 23
VAT2 = (1 + VAT / 100)
full_price = tb1_price + tb2_price + tb13_price
full_price_VAT = full_price * VAT2

print ("The price is: ", full_price, "PLN/net", "that is", full_price_VAT, "PLN/gross")

print ("Now, please enter your shipping details. ")
name = input(str ("Name: "))
surname = input(str("Surname: "))
email = input(str("e-mail: "))
mobile = input("mobile: ")
address = input("address: ")

print ("Summary of your order", "\nCost: ", full_price, "PLN/net", "that is", full_price_VAT, "PLN/gross", "\nAddress details:",  name.capitalize(), surname.capitalize(), email,  mobile, address)

