# Python program to check if the number is an Armstrong number or not

# take input from the user
num = int(input("Enter a number: "))

# initialize sum
sum = 0

# find the sum of the cube of each digit
copy = num

while copy > 0:
    #To access each digit we take the modulus of the number ( mod 10 ) to extract the last digit of the number
    digit = copy % 10
    #updating the result as the sum of the previous result and the digit raised to the power of the number of digits.
    sum += digit ** 3
    copy //= 10

# display the result
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number") 