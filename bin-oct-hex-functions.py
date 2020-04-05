def getNegativeBinaryValue(binArray):
    for i in range(32 - len(binArray)):
        binArray.insert(0, 0)
    for i in range(len(binArray)):
        binArray[i] = 1 - binArray[i]
    digitIndex = len(binArray) - 1
    while True:
        if binArray[digitIndex] == 0:
            binArray[digitIndex] = 1
            break
        else:
            binArray[digitIndex] = 0
            digitIndex -= 1
    return binArray


def getBinaryValue(decimalNumber):
    decimalNumber = int(decimalNumber)
    binValue = []
    while decimalNumber != 0:
        binValue.append(decimalNumber % 2)
        decimalNumber = decimalNumber // 2
    binValue.reverse()
    return binValue


def fromDecToBin(number):
    if isinstance(number, float):
        number = int(number)
    isNegative = False
    if number < 0:
        isNegative = True
        number = abs(number)
    binValue = getBinaryValue(number)
    if isNegative:
       binValue = getNegativeBinaryValue(binValue)
    resultBinValueString = "b" + ''.join(str(e) for e in binValue)
    return resultBinValueString


def fromBinToDec(binaryNumberString):
    if(binaryNumberString[0] != 'b'):
        return
    binaryNumberString = binaryNumberString.replace('b', '')
    binaryNumberArray = []
    for number in binaryNumberString:
        binaryNumberArray.append(int(number))
    decimalNumber = 0
    for i in range(len(binaryNumberArray)):
        decimalNumber += binaryNumberArray[i] * (2 ** (len(binaryNumberArray) - 1 - i))
    return decimalNumber


def fromDecToHex(decNumber):
    if isinstance(decNumber, float):
        decNumber = int(decNumber)
    isNegative = False
    if decNumber < 0:
        isNegative = True
        decNumber = abs(decNumber)
    hexValue = []
    if not isNegative:
        while decNumber != 0:
            remainder = decNumber % 16
            if remainder < 10:
                hexValue.append(remainder)
            if remainder == 10:
                hexValue.append('A')
            if remainder == 11:
                hexValue.append('B')
            if remainder == 12:
                hexValue.append('C')
            if remainder == 13:
                hexValue.append('D')
            if remainder == 14:
                hexValue.append('E')
            if remainder == 15:
                hexValue.append('F')
            decNumber = decNumber // 16
        hexValue.reverse()
    else:
        binValue = getBinaryValue(decNumber)
        binValue = getNegativeBinaryValue(binValue)
        fromBinToDecValues = []
        for i in range(0, len(binValue), 4):
            fromBinToDecValues.append(fromBinToDec('b' + str(binValue[i]) + str(binValue[i + 1]) + str(binValue[i + 2]) + str(binValue[i + 3])))
        for number in fromBinToDecValues:
            if number < 10:
                hexValue.append(number)
            if number == 10:
                hexValue.append('A')
            if number == 11:
                hexValue.append('B')
            if number == 12:
                hexValue.append('C')
            if number == 13:
                hexValue.append('D')
            if number == 14:
                hexValue.append('E')
            if number == 15:
                hexValue.append('F')
    resultHexValueString = 'h' + ''.join(str(e) for e in hexValue)
    return resultHexValueString


def fromHexToDec(hexNumberString):
    if hexNumberString[0] != 'h':
        return
    hexNumberString = hexNumberString.replace('h', '')
    hexNumberArray = []
    for number in hexNumberString:
        if number.isdigit():
            hexNumberArray.append(int(number))
        if number == 'A':
            hexNumberArray.append(10)
        if number == 'B':
            hexNumberArray.append(11)
        if number == 'C':
            hexNumberArray.append(12)
        if number == 'D':
            hexNumberArray.append(13)
        if number == 'E':
            hexNumberArray.append(14)
        if number == 'F':
            hexNumberArray.append(15)
    decimalNumber = 0
    for i in range(len(hexNumberArray)):
        decimalNumber += hexNumberArray[i] * (16 ** (len(hexNumberArray) - i - 1))
    return decimalNumber


def fromDecToOct(decNumber):
    if isinstance(decNumber, float):
        decNumber = int(decNumber)
    isNegative = False
    if decNumber < 0:
        isNegative = True
        decNumber = abs(decNumber)
    octValue = []
    if not isNegative:
        while decNumber != 0:
            octValue.append(decNumber % 8)
            decNumber = decNumber // 8
        octValue.reverse()
    else:
        binValue = getBinaryValue(decNumber)
        binValue = getNegativeBinaryValue(binValue)
        octValue.append(fromBinToDec('b' + str(binValue[0]) + str(binValue[1])))
        for i in range(2, len(binValue), 3):
            octValue.append(fromBinToDec('b' + str(binValue[i]) + str(binValue[i + 1]) + str(binValue[i + 2])))

    resultOctValueString = 'o' + ''.join(str(e) for e in octValue)
    return resultOctValueString


def fromOctToDec(octNumberString):
    if octNumberString[0] != 'o':
        return
    octNumberString = octNumberString.replace('o', '')
    octNumberArray = []
    for number in octNumberString:
        octNumberArray.append(int(number))
    decimalNumber = 0
    for i in range(len(octNumberArray)):
        decimalNumber += octNumberArray[i] * (8 ** (len(octNumberArray) - i - 1))
    return decimalNumber