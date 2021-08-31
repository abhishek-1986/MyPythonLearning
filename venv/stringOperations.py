#Strings
'''
#Approach 1
name="John"
name1='Doe'
print(name)
print(name1)

#Approach 2
name3=str("Abhishek")
print(name3)
'''

'''
#String immutability
str1="welcome"
str2="welcome"
print(id(str1)) #2062901219696
print(id(str2)) #2062901219696

str2=str2+"to Python"
print(id(str2))
'''

#String concatenation and recursion
str1="welcome"
print(str1+"to programming")
print((str1+"\n")*5)

#String Length
str3="AbhishekRamesh"
print(len(str3))

# String Slicing/substring chars of the string
str2="AbhishekRamesh"
print(str2[1:3]) #bh
print(str2[:6]) #Abhish
print(str2[4:]) #shekRamesh

#String in and not in operator
str4="WElcome"
print("come" in str4) #True
print("WEl" not in str4) #False
print("WEL" not in str4) #True

# ord and char function
print(ord('Z'))
print(chr(83))

