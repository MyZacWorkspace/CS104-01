#Zaccery Tarver - CS104 01 - 9.29.2022
#Average.py
howManyEntered = 0
total = 0

howMany = int(input("How many test scores would you like to average?\n"))

while(howManyEntered < howMany):
    testScore = float(input("Enter test score: "))
    total += testScore
    howManyEntered += 1

average = total / howMany
print("The average for the test scores you entered is: " + str(average))

#end of program


