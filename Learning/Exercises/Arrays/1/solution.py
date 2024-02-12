expenses = [2200, 2350, 2600, 2130, 2190] #, 0, 0, 0, 0, 0, 0 ,0]

# 1. In Feb, how many dollars you spent extra compare to January?
print(1, f"In Feb I spent: {expenses[1] - expenses[0]}")

# 2. Find out your total expense in first quarter (first three months) of the year.
firstQuarter = 0
for i in range(3):
    firstQuarter += expenses[i]
print(2, f"My total expense in the first quarter was: {firstQuarter}")

# 3. Find out if you spent exactly 2000 dollars in any month
for i in range(len(expenses)):
    if expenses[i] == 2000:
        print(3, f"Yes, in: {i}")
    elif i == len(expenses) - 1:
        print(3, "No, there is not one month in which I have spent that amount")

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expenses.insert(5, 1980)
print(4, f"June expense was inserted: {expenses}")

# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to 
# your monthly expense list based on this
expenses[3] -= 200
print(5, f"Refund of purchase in april done: {expenses}")
