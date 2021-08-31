name="Abhishek"
age=35
salary=2000000.0

#Approach 1
print(name,age,salary)

#Approach 2
print("Name is :",name)
print("Age is :",35)
print("Salary is :",salary)

#Approach 3
#What type of the data is important "type of variable"
print("Name : %s Age is: %d Salary: %f "%(name,age,salary))

#Approach 4
print("Name : {} Age : {} Salary : {}".format(age,name,salary))

#Approach 5
print("Name : {1} Age : {2} Salary : {0}".format(age,name,salary))