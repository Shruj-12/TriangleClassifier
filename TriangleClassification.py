a = int(input("What is the length of the first leg? "))
b = int(input("What is the length of the second leg? "))
c = int(input("What is the length of the third leg? "))

sides = [a, b, c]
sides.sort()

aSq = sides[0] ** 2
bSq = sides[1] ** 2
cSq = sides[2] ** 2

if sides[2] < sides[0] + sides[1]: # Proves triangle
    if cSq > aSq + bSq:
        print("The given legs form an obtuse triangle.")
    elif cSq < aSq + bSq:
        print("The given legs form an acute triangle.")
    else:
        print("The given legs form a right triangle.")
else:
    print("The given legs do not form a triangle.")
