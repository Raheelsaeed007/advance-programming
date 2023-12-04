a = float(input("Enter the length of the first side of triangle:"))
b = float(input("Enter the length of the second side of triangle:"))
c = float(input("Enter the length of the third side of triangle:"))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral Triangle")
    elif a == b or a == c or b == c:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Not a valid triangle")