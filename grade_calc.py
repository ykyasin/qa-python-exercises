print("Welcome to the grade calculator")
mathMark = float(input("Please enter your maths mark: "))
chemMark = float(input("Please enter your chemistry mark: "))
phyMark = float(input("Please enter your physics mark: "))

ave = (mathMark + chemMark + phyMark) / 3

if ave < 40: 
    p = "You failed"
elif 40 <= ave < 50:
    p = "D"
elif 50 <= ave < 60:
    p = "C"
elif 60 <= ave < 70:
    p = "B"
elif ave >= 70:
    p = "A"

print("Your percentage score is: " + str(ave) + "%")
if ave < 40: 
    print(p)
else:
    print("You scored a grade of:", p)