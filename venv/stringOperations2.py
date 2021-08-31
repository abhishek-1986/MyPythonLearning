#String comparision operators =,!=,>,<,<=,>=

print("time"=="tie")
print("Abhishek" >"ramesh")
print("Sanjith" != "Ram")
print("Ramesh" >= "Amitha")
print("ramesh" == "")


#String iterations

str="Python"
for i in str:
    print(str) #prints the whole string
    print(i) #prints each character

#String functions
str1="welcome to python"
print(str1.isalnum())
print(str1.islower())
print("2012".isdigit())
print("first number".isidentifier())
print("WELCOME".isupper())
print(" ".isspace())
print(str1.isalpha())


#subString find functions
s="Welcome to Python"
print(s.endswith("thon"))
print(s.startswith("Belcome"))
print(s.find("come to Py"))
print(s.find("come 2"))
print(s.rfind("come"))
print(s.count("o"))\

#String conversion functions
s="Welcome to python"
print(s.capitalize()) # capitalizes first character of string
print(s.title()) # Capitalizes first character of each word
print(s.lower()) #Converts all characters to lower
print(s.upper()) #Converts all characters to upper
print(s.swapcase()) #Swaps the case of all chars
print(s.replace("come to ","come 2")) #replaces old string with new string
