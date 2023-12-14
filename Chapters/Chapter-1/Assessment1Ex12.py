#Area and circumfrence of Circle
choice = int(input("Which shape do you want to calculate: \n 1.Circle \n 2.rectangle \n 3.triangle \n"))
if choice == 1:
  choice2 = int(input("what do you want to calculate: \n1.Area \n2.Circumference \n"))
  if choice2 == 1:
    r = float(input("Enter the radius"))
    Area = 3.14*r**2
    print("The area of Circle is:",Area)
  elif choice2 == 2:
    r = float(input("Enter the radius"))

    Circumference=2*3.14*r
    print("The circumference of circle  is:",Circumference)
  else:
    print("Invalid")

#Area and Circumference of rectangle
if choice == 2:
  choice2 = int(input("what do you want to calculate: \n1.Area \n2.Circumference \n"))
  if choice2 == 1:
    r = float(input("Enter the radius"))
    Area = 4*3.14*r**2
    print("The area of rectangle is:",Area)
  elif choice2 == 2:

    L = float(input("Enter the value of L \n"))
    w = float(input("Enter the value of w \n"))
    Circumference = 2*L+2*w
    print("The circumference of rectangle  is:",Circumference)

  else:
    print("Invalid")

#Area and Circumference of triangle
if choice == 3:
  choice2 = int(input("what do you want to calculate: \n1.Area \n2.Circumference \n"))
  if choice2 == 1:

    b = float(input("Enter the value of b \n"))
    h = float(input("Enter the value of h \n"))
    Area = 1/2*b*h
    print("The area of triangle is:", Area)
  elif choice2 == 2:

    #Asking user to input
    A = float(input("Enter the value of A \n"))
    B = float(input("Enter the value of B \n"))
    C = float(input("Enter the value of C \n"))
    Circumference = A+B+C
    print("The circumference of triangle  is:", Circumference)
  else:
    print("Invalid")
