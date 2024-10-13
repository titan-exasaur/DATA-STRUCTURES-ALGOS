# Calculate Average Temperature

numDays = int(input("Enter the number of days: "))
total = 0

for i in range(1, numDays+1):
    nextDay = float(input("Enter the temperature for day " + str(i) + ": "))
    total += nextDay

average = total / numDays

print("The average temperature was " + str(average))