#11. Print Prime Numbers Less Than 20
print("Prime numbers less than 20 are:")

for num in range(2, 20):
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print(num)
        
        
        
#12. Factorial Using Recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number: "))

print("Factorial =", factorial(num))

#13. Check Right Triangle

a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

sides = sorted([a, b, c])

if sides[2]**2 == sides[0]**2 + sides[1]**2:
    print("It is a Right Triangle.")
else:
    print("It is NOT a Right Triangle.")
    
#14 Implement pow(x, n)
class Power:

    def power(self, x, n):
        return x ** n

obj = Power()

x = int(input("Enter base: "))
n = int(input("Enter exponent: "))

print("Answer =", obj.power(x, n))