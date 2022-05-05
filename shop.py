Products = [
    ["Black_Tshirt (number 1)", 105, 75],
    ["White_Tshirt (number 2)", 105, 85],
    ["Gray_Tshirt (number 3)", 105, 80]
    ]

for productName, price, quantity in Products:
    print("Product name:", productName)
    print("Price:", price)
    print("Quantity:", quantity)
    print("\n")

decision = True
while decision == True:
    choice = input("T-Shirt number: ")
    if (choice == "1"):
        print("The price is:", Products[0][1], "zł/net", "In stock: ", Products[0][2])
        if (choice == "1"):
            HowMany = int(input("How many pieces?: "))
            print("The price is: ", Products[0][1] * HowMany)
            print("And then in stock: ", Products[0][2] - HowMany)
    if (choice == "2"):
        print("The price is:", Products[1][1], "zł/net", "In stock: ", Products[1][2])
        if (choice == "2"):
            HowMany2 = int(input("How many pieces?: "))
            print("The price is: ", Products[1][1] * HowMany2)
            print("And then in stock: ", Products[1][2] - HowMany2)
    if (choice == "3"):
        print("The price is:", Products[2][1], "zł/net", "In stock: ", Products[2][2])
        if (choice == "3"):
            HowMany3 = int(input("How many pieces?: "))
            print("The price is: ", Products[2][1] * HowMany3)
            print("And then in stock: ", Products[2][2] - HowMany3)

    decision = input("Do you want to continue (Yes/No): ")
    if decision == "Yes":
        decision = True
    elif decision == "No":
        decision = False
        break
    else:
        print('Wrong Comment!')
        decision = input("Do you want to continue (Yes/No): ")

TB1_price = Products[0][1] * HowMany
TB2_price = Products[1][1] * HowMany2
TB3_price = Products[2][1] * HowMany3

print ("The price is: ", TB1_price + TB2_price + TB3_price, "zl/net")





____________________________________________________________

Products = [
    ["Black_Tshirt (number 1)", 105, 75],
    ["White_Tshirt (number 2)", 105, 85],
    ["Gray_Tshirt (number 3)", 105, 80]
    ]

for productName, price, quantity in Products:
    print("Product name:", productName)
    print("Price:", price)
    print("Quantity:", quantity)
    print("\n")

HowMany = 0
HowMany2 = 0
HowMany3 = 0

decision = True
while decision == True:
    choice = input("T-Shirt number: ")
    if (choice == "1"):
        print("The price is:", Products[0][1], "PLN/net", "In stock: ", Products[0][2])
        if (choice == "1"):
            HowMany = int(input("How many pieces?: "))
            print("The price is: ", Products[0][1] * HowMany)
            print("And then in stock: ", Products[0][2] - HowMany)
    if (choice == "2"):
        print("The price is:", Products[1][1], "PLN/net", "In stock: ", Products[1][2])
        if (choice == "2"):
            HowMany2 = int(input("How many pieces?: "))
            print("The price is: ", Products[1][1] * HowMany2)
            print("And then in stock: ", Products[1][2] - HowMany2)
    if (choice == "3"):
        print("The price is:", Products[2][1], "PLN/net", "In stock: ", Products[2][2])
        if (choice == "3"):
            HowMany3 = int(input("How many pieces?: "))
            print("The price is: ", Products[2][1] * HowMany3)
            print("And then in stock: ", Products[2][2] - HowMany3)

    decision = input("Do you want to continue (yes/no): ")
    if decision == "yes":
        decision = True
    elif decision == "no":
        decision = False
        break
    else:
        print('Wrong Comment!')
        decision = input("Do you want to continue (Yes/No): ")

print("Great job!")

ActualPrice = Products[0][1] * HowMany
ActualPrice2 = Products[1][1] * HowMany2
ActualPrice3 = Products[2][1] * HowMany3

ActualQuantity = Products[0][2] - HowMany
ActualQuantity2 = Products[1][2] - HowMany2
ActualQuantity3 = Products[2][2] - HowMany3

HowManyR = 0
HowManyR2 = 0
HowManyR3 = 0

decision2 = input ("Do you want to remove something? yes/no: ")
if decision2 == "yes":
    decision2 = True
elif decision2 == "no":
    decision2 = False

#decision2 = True
while decision2 == True:
    choice2 = input("T-Shirt number: ")
    if (choice2 == "1"):
        print("The price is:", Products[0][1], "PLN/net", "In stock: ", ActualQuantity)
        if (choice2 == "1"):
            HowManyR = int(input("How many pieces?: "))
            print("The price is: ", int(ActualPrice) - (Products[0][1] * HowManyR))
            print("And then in stock: ", ActualQuantity + HowManyR)
    if (choice2 == "2"):
        print("The price is:", Products[1][1], "PLN/net", "In stock: ", ActualQuantity2)
        if (choice2 == "2"):
            HowManyR2 = int(input("How many pieces?: "))
            print("The price is: ",  int(ActualPrice2) - (Products[0][1] * HowManyR2))
            print("And then in stock: ", ActualQuantity2 + HowManyR2)
    if (choice2 == "3"):
        print("The price is:", Products[2][1], "PLN/net", "In stock: ",ActualQuantity3)
        if (choice2 == "3"):
            HowManyR3 = int(input("How many pieces?: "))
            print("The price is: ",  int(ActualPrice3) - (Products[0][1] * HowManyR3))
            print("And then in stock: ", ActualQuantity3 + HowManyR3)

    decision2 = input("Do you want to remove something? yes/no: ")
    if decision2 == "yes":
        decision2 = True
    elif decision2 == "no":
        decision2 = False
        break


#TBR1_price = Products[0][1] * HowManyR
#TBR2_price = Products[1][1] * HowManyR2
#TBR3_price = Products[2][1] * HowManyR3

TB1_price = Products[0][1] * (HowMany - HowManyR)
TB2_price = Products[1][1] * (HowMany2 - HowManyR2)
TB3_price = Products[2][1] * (HowMany3 - HowManyR3)

VAT = 23
VAT2 = (1 + VAT / 100)
full_price = TB1_price + TB2_price + TB3_price
full_price_VAT = full_price * VAT2

print
print ("The price is: ", full_price_VAT, "PLN/gross")

print ("Now, please enter your shipping details. ")
name = input(str ("Name: "))
surname = input(str("Surname: "))
email = input(str("e-mail: "))
mobile = input("mobile: ")
address = input("address: ")

print ("Summary of your order", "\nCost: ", full_price_VAT, "PLN/gross", "\nAddress details:",  name.capitalize(), surname.capitalize(), email,  mobile, address)










