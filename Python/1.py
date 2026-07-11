
from datetime import datetime
#1. Different Number Data Types in Python
a = 10 ; 
b = 20.5;
c = 3 + 4j;

print("Integer:",type(a));
print("float:",type(b));
print("complex:",type(c));  

#2. Arithmetic Operations
print("Addition:",a+b);
print("Subtraction:",a-b);
print("Multiplication:",a*b);
print("Division:",a/b);

#3. String Creation, Concatenation, and Substring
str1 = "Hello"
str2  = "world"
str3 = str1 + " " + str2
print("Concatenated String:",str3)
print("Substring:",str3[0:5])
print("Particular string",str3[3])

#4. Print Current Date in Given Format
current_date = datetime.now()
print("current date:", current_date)
print(current_date.strftime("%a %b %d %H:%M:%S %Y"))

#5. Create, Append, and Remove Lists
fruits = ["Apple", "Banana", "Mango"]
print("Original list:", fruits);
fruits.append("Orange");
print("List after appending:", fruits);
fruits.remove("Banana");
print("List after removing:", fruits);

#6. Working with Tuples
fruits = ("apple", "banana", "orange")
print(fruits)
person = ("Alice", 25, 5.6, True)
print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[-1])  # orange

#7. Working with Dictionaries
students = {
    "name":"Tanish Jain",
    "age":20,
    "gender":"Male"
}

print(students)
print("name:",students["name"])
students["age"]=21
print("Updated Dictionary:", students)

#8. Largest of Three Numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

largest = max(num1, num2, num3)
print("The largest number is:", largest)

#9. Celsius ↔ Fahrenheit Conversion

choice = input("Enter C to convert Celsius to Fahrenheit or F for Fahrenheit to Celsius: ")

if choice.upper() == "C":
    c = float(input("Enter Celsius: "))
    f = (9/5) * c + 32
    print("Fahrenheit =", f)

elif choice.upper() == "F":
    f = float(input("Enter Fahrenheit: "))
    c = (5/9) * (f - 32)
    print("Celsius =", c)

else:
    print("Invalid Choice")

#10. Pattern Using Nested For Loop

rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()
    