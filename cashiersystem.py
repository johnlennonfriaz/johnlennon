amount = input("Enter Amount: ")
quantity = input("Enter Quantity: ")
total = int(amount) * int(quantity)
cashonhand = input("Enter Cash on Hand: ")
change = int(cashonhand) - int(total)
print("Total Price: " +str(total))
print("Your change is: " +str(change)) 