"""
Flow Control - If Else Elif
"""

x = 2

if x == 1:
    print("x is 1")
print("Outside of If statement")



x==2
if x > 1:
    print("x is greater than 1")
else:
    print("x is not greater than 1")
print("Outside of If statement")


hour = 13
if hour <15:
    print("Good morning!")
else:
    print("Good afternoon!")


hour = 18
if hour <15:
    print("Good morning!")
elif hour <20 :
    print("Good afternoon!")
else:
    print("Good night!")


# If-else assignment

grade = 81

if grade >= 90:
    print("A")
elif 80<=grade<90:
    print("B")
elif 70<=grade<80:
    print("C")
elif 60<=grade<70:
    print("D")
else:
    print("F")