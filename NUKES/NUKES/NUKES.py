#!/usr/bin/python

# value, limit, numOfChamber
def readInputs():
    readline = raw_input()
    splitted = readline.split()
    input = []
    for item in splitted:
        input.append(int(item))
    return input

class Nukes:
    def representValueIn(self, value, system):
        result = []
        if system < 2:
            return result
        while value > 0:
            result.append(value % system)
            value = value / system
        return result

    def getChanbersStatus(self, atoms, limit, numOfChambers):
        filledChambers = Nukes().representValueIn(atoms, limit + 1)
        result = ''
        for i in range(numOfChambers):
            if i >= len(filledChambers):
                result += str(0) + ' '
            else:
                result += str(filledChambers[i]) + ' '
        return result

input = readInputs()
print Nukes().getChanbersStatus(input[0], input[1], input[2])


