
#Input function default accepts string and u need to type cast the value to either integer or float
'''
num1=int(input("Enter the first number:")) #10
num2=int(input("Enter the second number:")) #20
print(num1+num2) #1020 is output


num1=float(input("Enter the first decimal number:")) #10
num2=float(input("Enter the second decimal number:")) #20
print(num1+num2) #10.5 is output
'''

num1=input("Enter the first decimal number:") #10.5
num2=input("Enter the second integer number:") #20.5
#print(float(num1)+int(num2)) #float variable can hold integer value but Integer cannot hold value hence typcasting of
                              # #ValueError: invalid literal for int() with base 10: '10.5'
print(float(num1)+float(num2))