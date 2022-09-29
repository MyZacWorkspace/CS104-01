#Zaccery Tarver - CS104 01 - 9.29.2022
#conditions.py

temp = input("Please enter the current temperature: ")
#print(type(temp))
temp = int(temp)
#print(type(temp))

if(temp > 90):
    print("Wear Shorts")
elif(temp > 70):
    print("Short sleeves are fine")
elif(temp > 50):
    print("Wear a jacket")
elif(temp > 32):
    print("Wear a heavy coat")
else:
    print("Stay Inside")

#end of program
    
