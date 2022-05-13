print('\n', "Welcome to the T-shirt shop. Everything here is oversize and unisex. I invite you to choose products :)\n")

class Products:
    color = ""
    price = 0
    in_stock = 0

    def t_shirts(self):
        print('\n', "color: ", self.color, '\n', "price: ", self.price, '\n', "in_stock: ", self.in_stock)


tshirt1, tshirt2, tshirt3 = Products(), Products(), Products()

tshirt1.color, tshirt1.price, tshirt1.in_stock = "black (nr 1)", 105, 75
tshirt2.color, tshirt2.price, tshirt2.in_stock = "white (nr 2)", 105, 85
tshirt3.color, tshirt3.price, tshirt3.in_stock = "gray (nr 3)", 105, 80

how_many, how_many2, how_many3 = 0, 0, 0

tshirt1.t_shirts(), tshirt2.t_shirts(), tshirt3.t_shirts()

decision = True
while decision == True:
    choice = input("T-Shirt number: ")
    if choice == "1":
        print("The price is:", tshirt1.price, "PLN/net", "In stock: ", tshirt1.in_stock)
        if choice == "1":
            how_many = int(input("How many pieces?: "))
            print("The price is: ", tshirt1.price * how_many)
            print("And then in stock: ", tshirt1.in_stock - how_many)
    if choice == "2":
        print("The price is:", tshirt2.price, "PLN/net", "In stock: ", tshirt1.in_stock)
        if choice == "2":
            how_many2 = int(input("How many pieces?: "))
            print("The price is: ", tshirt2.price * how_many2)
            print("And then in stock: ", tshirt2.in_stock - how_many2)
    if choice == "3":
        print("The price is:", tshirt3.price, "PLN/net", "In stock: ", tshirt3.in_stock)
        if choice == "3":
            how_many3 = int(input("How many pieces?: "))
            print("The price is: ", tshirt3.price * how_many3)
            print("And then in stock: ", tshirt3.in_stock - how_many3)

    decision = input("Do you want to continue (yes/no): ")
    if decision == "yes":
        decision = True
    elif decision == "no":
        decision = False
        break
    else:
        print('Wrong answer!')
        decision = input("Do you want to continue (Yes/No): ")

actual_price, actual_price2, actual_price3 = tshirt1.price * how_many, tshirt2.price * how_many2, tshirt3.price * how_many3
actual_quantity, actual_quantity2, actual_quantity3 = tshirt1.in_stock - how_many, tshirt2.in_stock - how_many2, tshirt3.in_stock - how_many3

how_many_r, how_many_r2, how_many_r3 = 0, 0, 0

decision2 = input("Do you want to remove something? yes/no: ")
if decision2 == "yes":
    decision2 = True
elif decision2 == "no":
    decision2 = False
else:
    print("Wrong answer!")
    decision2 = input("Do you want to remove something? yes/no: ")

while decision2 == True:
    choice2 = input("T-Shirt number: ")
    if choice2 == "1":
        print("The price is:", tshirt1.price, "PLN/net", "In stock: ", actual_quantity)
        if choice2 == "1":
            how_many_r = int(input("How many pieces?: "))
            print("The price is: ", int(actual_price) - (tshirt1.price * how_many_r))
            print("And then in stock: ", actual_quantity + how_many_r)
    if choice2 == "2":
        print("The price is:", tshirt2.price, "PLN/net", "In stock: ", actual_quantity2)
        if choice2 == "2":
            how_many_r2 = int(input("How many pieces?: "))
            print("The price is: ", int(actual_price2) - (tshirt2.price * how_many_r2))
            print("And then in stock: ", actual_quantity2 + how_many_r2)
    if choice2 == "3":
        print("The price is:", tshirt3.price, "PLN/net", "In stock: ", actual_quantity3)
        if choice2 == "3":
            how_many_r3 = int(input("How many pieces?: "))
            print("The price is: ", int(actual_price3) - (tshirt3.price * how_many_r3))
            print("And then in stock: ", actual_quantity3 + how_many_r3)

    decision2 = input("Do you want to remove something? yes/no: ")
    if decision2 == "yes":
        decision2 = True
    elif decision2 == "no":
        decision2 = False
        break

tb1_price, tb2_price, tb3_price = tshirt1.price * (how_many - how_many_r), tshirt2.price * (
        how_many2 - how_many_r2), tshirt3.price * (how_many3 - how_many_r3)

total_quantity = actual_quantity + actual_quantity2 + actual_quantity3

VAT = 23
VAT2 = (1 + VAT / 100)
full_price = tb1_price + tb2_price + tb3_price
full_price_VAT = full_price * VAT2

print("The price is: ", full_price, "PLN/net", "that is", full_price_VAT,
      "PLN/gross. To complete the purchase, please provide your details")

import re

regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def check(email_address):
    if (re.fullmatch(regex, email)):
        print("Ok")
    else:
        print("Invalid")


while __name__ == '__main__':
    email = input("email: ")
    check(email)
    if (re.fullmatch(regex, email)):
        print("Next")
        break
    else:
        print("Wrong answer, write again!")
        continue

name = input("Name: ")
surname = input("Surname: ")
address = input("address: ")
mobile = input("mobile: ")

print("Summary of your order", "\nCost: ", full_price, "PLN/net", "that is", full_price_VAT, "PLN/gross", "\nAddress details:", '\n', name.capitalize(), surname.capitalize(), '\n', email, '\n', mobile, '\n', address)
