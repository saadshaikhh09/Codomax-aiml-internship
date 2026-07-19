# Program 1 : Check Even or Odd
num = int(input("Enter a Number : "))
if num % 2 == 0:
    print(f"{num} is Even.")
else : 
    print(f"{num} is Odd.")

# Program 2 : Sum of first n natural numbers : 
n=10
total = 0
for i in range(1,n+1):
    total += i
print(f"Sum of the first {n} numbers is {total}") 