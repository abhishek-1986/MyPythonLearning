a=33

if a>20: # condtion statement
    print("True Condition")
else:
    print("False condition")

if True: #True or false
    print("True Condition")
else:
    print("False condition")


if 0: #1 or 0
    print("True Condition")
else:
    print("False condition")

if a%2==0:
    print("Even Number")
else:
    print("Odd Number")

#Multiple statements under if else block
if False:
    print("statement1")
    print("statement2")
    print("statement3")
else:
    print("statement4")
    print("statement5")

print("this is not a part of if or else block")

# Single statements in single line
print("Welcome") if True else print("Python")
print("Welcome") if 10<20 else print("Python")
print("Welcome") if 10>20 else print("Python")


# Multiple statements in single line
{print("Welcome1"),print("python1")} if True else {print("Python2"),prin("Welcome2")}
{print("Welcome1"),print("python1")} if False else {print("Python2"),print("Welcome2")}


# if elif else

a=430

if a==100:
    print("Hundred")
elif a==200:
    print("Two Hundred")
elif a==300:
    print("Three Hundred")
elif a==400:
    print("Four Hundred")
'''else:
    print("None of the number matches")
'''