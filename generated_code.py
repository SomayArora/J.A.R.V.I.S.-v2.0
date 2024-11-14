
n = int(input("Enter the number of numbers: "))
sum = 0
for i in range(n):
  num = int(input("Enter number {}: ".format(i+1)))
  sum += num
print("The sum of the numbers is:", sum)
