#!/usr/bin/python

readline = raw_input()
splitted = readline.split()
input = []
for item in splitted:
	input.append(int(item))

# value, limit, numOfChamber

#input = [6,4,17]

def representValueIn(value, system):
    result = []
    if system < 2:
        return result
    while value > 0:
        result.append(value % system)
        value = value / system
    return result


filledChambers = representValueIn(input[0], input[1]+1)

result = ''
for i in range(input[2]):
    if i >= len(filledChambers):
        result += str(0) + ' '
    else:
        result += str(filledChambers[i]) + ' '

print result

