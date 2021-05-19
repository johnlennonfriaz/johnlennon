my_name = input("Enter your name: ")
my_grade = input("Enter your Grade: ")
my_grade = int(my_grade)
if my_grade >= 98 and my_grade <= 100:
    print("1.00 " +my_name)
elif my_grade >= 96 and my_grade <= 97:
    print("1.25 " +my_name)
else:
    print("invalid")