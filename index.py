#Python Program to Display calendar.
import calendar  
# Enter the month and year  
yy = int(input("Enter year: "))  
mm = int(input("Enter month: "))  
print(calendar.month(yy,mm))  


#Simple Calculator by Making Functions
def add(x, y):
    return x + y
def subtract(x, y):
 return x - y
def multiply(x, y):
 return x * y
def divide(x, y):
 return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
choice = input("Enter choice(1/2/3/4): ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if choice == '1':
 print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
 print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
 print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
 print(num1,"/",num2,"=", divide(num1,num2))
else:
 print("Invalid input")




 #Python Program to Display the multiplication Table 
 num = int(input(" Enter the number : "))    
# using for loop to iterate multiplication 10 times     
print("Multiplication Table of : ")  
for i in range(1,11):    
   print(num,'x',i,'=',num*i)  



 