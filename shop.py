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


TB1_price = Products[0][1] * HowMany
TB2_price = Products[1][1] * HowMany2
TB3_price = Products[2][1] * HowMany3

VAT = 23
VAT2 = (1 + VAT / 100)
full_price = TB1_price + TB2_price + TB3_price
full_price_VAT = full_price * VAT2


print ("The price is: ", full_price_VAT, "PLN/gross")


