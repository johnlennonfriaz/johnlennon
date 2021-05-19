my_name = input("Enter your name: ")
my_age = input("Enter your age: ")
my_age = int(my_age)
if my_age >= 99:
    print("You are eligible to vote" +my_name)
else:
    print("Your are not eligible to vote " +my_name)