'''
Zaccery Tarver
12.1.2022
CS104
PythonQueueBankSimulation
'''

names = []

for x in range(10):
    names.append(input('Enter name: '))

print(names)

for x in range(len(names)):
    print(names.pop(0))

print(names)

    
