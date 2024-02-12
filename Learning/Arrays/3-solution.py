# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

maxNumber = int(input('Enter the max number: '))

oddNumbers = [num for num in range(0, maxNumber + 1) if num % 2 != 0]

print(f"Odd numbers from 0 until {maxNumber}: {oddNumbers}")
