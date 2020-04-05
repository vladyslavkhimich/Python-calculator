resultExpressionArray = []
operationsStack = []
wholeExpression = ''
wholeExpressionIndex = 0
trigonometricFuncModule = __import__("trigonometric-functions")
binOctHexFuncModule = __import__("bin-oct-hex-functions")


def setWholeExpression(expression):
    global wholeExpression
    wholeExpression = ''
    wholeExpression = expression
    global wholeExpressionIndex
    wholeExpressionIndex = 0
    resultExpressionArray.clear()
    operationsStack.clear()
    convertToPostfixNotation(expression)
    result = calculatePostfixExpression()
    return result


def convertToPostfixNotation(expression):
    expressionStringIndex = 0
    isWholeExpression = expression == wholeExpression
    global wholeExpressionIndex
    if isWholeExpression:
        expressionStringIndex = wholeExpressionIndex
    while expressionStringIndex != len(expression):
        if wholeExpressionIndex == len(wholeExpression):
            break

        if expression[expressionStringIndex] == '(':
            operationsStack.append(expression[expressionStringIndex])
            expressionStringIndex += 1
            wholeExpressionIndex += 1

        elif expression[expressionStringIndex] == ')':
            operationStackIndex = len(operationsStack) - 1
            if operationStackIndex > 0:
                while operationsStack[operationStackIndex] != '(':
                    resultExpressionArray.append(operationsStack.pop())
                    operationStackIndex -= 1
                operationsStack.pop()
            expressionStringIndex += 1
            wholeExpressionIndex += 1

        elif str.isdigit(expression[expressionStringIndex]):
            digit = str(expression[expressionStringIndex])
            expressionStringIndex += 1
            wholeExpressionIndex += 1
            if expressionStringIndex != len(expression):
                while str.isdigit(expression[expressionStringIndex]) or expression[expressionStringIndex] == '.':
                    digit += expression[expressionStringIndex]
                    expressionStringIndex += 1
                    wholeExpressionIndex += 1
                    if expressionStringIndex == len(expression):
                        break
                digit = float(digit)
            resultExpressionArray.append(digit)

        elif expression[expressionStringIndex] == '-':

            if expressionStringIndex == 0:
                digit = '-'
                expressionStringIndex += 1
                wholeExpressionIndex += 1
                if expressionStringIndex != len(expression) - 1:
                    while str.isdigit(expression[expressionStringIndex]) or expression[expressionStringIndex] == '.':
                        digit += expression[expressionStringIndex]
                        expressionStringIndex += 1
                        wholeExpressionIndex += 1
                        if expressionStringIndex == len(expression):
                            break
                    digit = int(digit)
                    resultExpressionArray.append(digit)

            elif expression[expressionStringIndex - 1] == '(':
                digit = '-'
                expressionStringIndex += 1
                wholeExpressionIndex += 1
                if expressionStringIndex != len(expression) - 1:
                    while str.isdigit(expression[expressionStringIndex]) or expression[expressionStringIndex] == '.':
                        digit += expression[expressionStringIndex]
                        expressionStringIndex += 1
                        if isWholeExpression:
                            wholeExpressionIndex += 1
                        if expressionStringIndex == len(expression):
                            break
                    digit = int(digit)
                    resultExpressionArray.append(digit)

            else:

                if len(operationsStack) != 0:
                    if operationsStack[len(operationsStack) - 1] != '(':
                        if operationsStack[len(operationsStack) - 1] == '+' or operationsStack[len(operationsStack) - 1] == '-' or operationsStack[len(operationsStack) - 1] == '*' or operationsStack[len(operationsStack) - 1] == '/' or operationsStack[len(operationsStack) - 1] == 'sin':
                            resultExpressionArray.append(operationsStack.pop())
                            operationsStack.append(expression[expressionStringIndex])
                        elif operationsStack[len(operationsStack) - 1] == 'sin' or operationsStack[len(operationsStack) - 1] == 'cos' or operationsStack[len(operationsStack) - 1] == 'tg' or operationsStack[len(operationsStack) - 1] == 'ctg':
                            resultExpressionArray.append(operationsStack.pop())
                            operationsStack.append(expression[expressionStringIndex])
                        elif operationsStack[len(operationsStack) - 1] == 'bin' or operationsStack[len(operationsStack) - 1] == 'hex' or operationsStack[len(operationsStack) - 1] == 'oct':
                            resultExpressionArray.append(operationsStack.pop())
                            operationsStack.append(expression[expressionStringIndex])
                        else:
                            operationsStack.append(expression[expressionStringIndex])
                    else:
                        operationsStack.append(expression[expressionStringIndex])
                else:
                    operationsStack.append(expression[expressionStringIndex])
                expressionStringIndex += 1
                wholeExpressionIndex += 1

        elif expression[expressionStringIndex] == '+':
            if len(operationsStack) != 0:
                if operationsStack[len(operationsStack) - 1] != '(':
                    if operationsStack[len(operationsStack) - 1] == '-' or operationsStack[len(operationsStack) - 1] == '+' or operationsStack[len(operationsStack) - 1] == '*' or operationsStack[len(operationsStack) - 1] == '/':
                        resultExpressionArray.append(operationsStack.pop())
                        operationsStack.append(expression[expressionStringIndex])
                    elif operationsStack[len(operationsStack) - 1] == 'sin' or operationsStack[len(operationsStack) - 1] == 'cos' or operationsStack[len(operationsStack) - 1] == 'tg' or operationsStack[len(operationsStack) - 1] == 'ctg':
                        resultExpressionArray.append(operationsStack.pop())
                        operationsStack.append(expression[expressionStringIndex])
                    elif operationsStack[len(operationsStack) - 1] == 'bin' or operationsStack[len(operationsStack) - 1] == 'hex' or operationsStack[len(operationsStack) - 1] == 'oct':
                        resultExpressionArray.append(operationsStack.pop())
                        operationsStack.append(expression[expressionStringIndex])
                    else:
                        operationsStack.append(expression[expressionStringIndex])
                else:
                    operationsStack.append(expression[expressionStringIndex])
            else:
                operationsStack.append(expression[expressionStringIndex])
            expressionStringIndex += 1
            wholeExpressionIndex += 1

        elif expression[expressionStringIndex] == '*' or expression[expressionStringIndex] == '/':
            if len(operationsStack) != 0:
                if operationsStack[len(operationsStack) - 1] != '(':
                    if operationsStack[len(operationsStack) - 1] == '*' or operationsStack[len(operationsStack) - 1] == '/':
                        resultExpressionArray.append(operationsStack.pop())
                        operationsStack.append(expression[expressionStringIndex])
                    elif operationsStack[len(operationsStack) - 1] == 'sin' or operationsStack[len(operationsStack) - 1] == 'cos' or operationsStack[len(operationsStack) - 1] == 'tg' or operationsStack[len(operationsStack) - 1] == 'ctg':
                        resultExpressionArray.append(operationsStack.pop())
                        operationsStack.append(expression[expressionStringIndex])
                    elif operationsStack[len(operationsStack) - 1] == 'bin' or operationsStack[len(operationsStack) - 1] == 'hex' or operationsStack[len(operationsStack) - 1] == 'oct':
                        resultExpressionArray.append(operationsStack.pop())
                        operationsStack.append(expression[expressionStringIndex])
                    else:
                        operationsStack.append(expression[expressionStringIndex])
                else:
                    operationsStack.append(expression[expressionStringIndex])
            else:
                operationsStack.append(expression[expressionStringIndex])
            expressionStringIndex += 1
            wholeExpressionIndex += 1

        elif expression[expressionStringIndex] == 's':
            wholeExpressionIndex += 3
            expressionStringIndex += 3
            if len(operationsStack) != 0:
                if operationsStack[len(operationsStack) - 1] != '(':
                    if operationsStack[len(operationsStack) - 1] == 'cos' or operationsStack[len(operationsStack) - 1] == 'tg' or operationsStack[len(operationsStack) - 1] == 'ctg' or operationsStack[len(operationsStack) - 1] == 'sin':
                        resultExpressionArray.append(operationsStack.pop())
                        operationsStack.append('sin')
                    elif operationsStack[len(operationsStack) - 1] == 'bin' or operationsStack[len(operationsStack) - 1] == 'hex' or operationsStack[len(operationsStack) - 1] == 'oct':
                        resultExpressionArray.append(operationsStack.pop())
                        operationsStack.append('sin')
                    else:
                        operationsStack.append('sin')
                else:
                    operationsStack.append('sin')
            else:
                operationsStack.append('sin')

        elif expression[expressionStringIndex] == 'c' and expression[expressionStringIndex + 1] == 'o':
            wholeExpressionIndex += 3
            expressionStringIndex += 3
            if len(operationsStack) != 0:
                if operationsStack[len(operationsStack) - 1] != '(':
                    if operationsStack[len(operationsStack) - 1] == 'cos' or operationsStack[len(operationsStack) - 1] == 'tg' or operationsStack[len(operationsStack) - 1] == 'ctg' or operationsStack[len(operationsStack) - 1] == 'sin':
                        resultExpressionArray.append(operationsStack.pop())
                        operationsStack.append('cos')
                    elif operationsStack[len(operationsStack) - 1] == 'bin' or operationsStack[len(operationsStack) - 1] == 'hex' or operationsStack[len(operationsStack) - 1] == 'oct':
                        resultExpressionArray.append(operationsStack.pop())
                        operationsStack.append('cos')
                    else:
                        operationsStack.append('cos')
                else:
                    operationsStack.append('cos')
            else:
                operationsStack.append('cos')

        elif expression[expressionStringIndex] == 't':
            wholeExpressionIndex += 2
            expressionStringIndex += 2
            if len(operationsStack) != 0:
                if operationsStack[len(operationsStack) - 1] != '(':
                    if operationsStack[len(operationsStack) - 1] == 'cos' or operationsStack[len(operationsStack) - 1] == 'tg' or operationsStack[len(operationsStack) - 1] == 'ctg' or operationsStack[len(operationsStack) - 1] == 'sin':
                        resultExpressionArray.append(operationsStack.pop())
                        operationsStack.append('tg')
                    elif operationsStack[len(operationsStack) - 1] == 'bin' or operationsStack[len(operationsStack) - 1] == 'hex' or operationsStack[len(operationsStack) - 1] == 'oct':
                        resultExpressionArray.append(operationsStack.pop())
                        operationsStack.append('tg')
                    else:
                        operationsStack.append('tg')
                else:
                    operationsStack.append('tg')
            else:
                operationsStack.append('tg')

        elif expression[expressionStringIndex] == 'c' and expression[expressionStringIndex + 1] == 't':
            wholeExpressionIndex += 3
            expressionStringIndex += 3
            if len(operationsStack) != 0:
                if operationsStack[len(operationsStack) - 1] != '(':
                    if operationsStack[len(operationsStack) - 1] == 'cos' or operationsStack[len(operationsStack) - 1] == 'tg' or operationsStack[len(operationsStack) - 1] == 'ctg' or operationsStack[len(operationsStack) - 1] == 'sin':
                        resultExpressionArray.append(operationsStack.pop())
                        operationsStack.append('ctg')
                    elif operationsStack[len(operationsStack) - 1] == 'bin' or operationsStack[len(operationsStack) - 1] == 'hex' or operationsStack[len(operationsStack) - 1] == 'oct':
                        resultExpressionArray.append(operationsStack.pop())
                        operationsStack.append('ctg')
                    else:
                        operationsStack.append('ctg')
                else:
                    operationsStack.append('ctg')
            else:
                operationsStack.append('ctg')

        elif expression[expressionStringIndex] == 'b':
            if expression[expressionStringIndex + 1] == 'i':
                wholeExpressionIndex += 3
                expressionStringIndex += 3
                if len(operationsStack) != 0:
                    if operationsStack[len(operationsStack) - 1] != '(':
                        if operationsStack[len(operationsStack) - 1] == 'cos' or operationsStack[len(operationsStack) - 1] == 'tg' or operationsStack[len(operationsStack) - 1] == 'ctg' or operationsStack[len(operationsStack) - 1] == 'sin':
                            resultExpressionArray.append(operationsStack.pop())
                            operationsStack.append('bin')
                        elif operationsStack[len(operationsStack) - 1] == 'bin' or operationsStack[len(operationsStack) - 1] == 'hex' or operationsStack[len(operationsStack) - 1] == 'oct':
                            resultExpressionArray.append(operationsStack.pop())
                            operationsStack.append('bin')
                        else:
                            operationsStack.append('bin')
                    else:
                        operationsStack.append('bin')
                else:
                    operationsStack.append('bin')
            else:
                binaryDigit = expression[expressionStringIndex]
                wholeExpressionIndex += 1
                expressionStringIndex += 1
                while str.isdigit(expression[expressionStringIndex]):
                    binaryDigit += expression[expressionStringIndex]
                    expressionStringIndex += 1
                    wholeExpressionIndex += 1
                    if expressionStringIndex == len(expression):
                        break
                resultExpressionArray.append(binaryDigit)

        elif expression[expressionStringIndex] == 'h':
            if expression[expressionStringIndex + 1] == 'e':
                wholeExpressionIndex += 3
                expressionStringIndex += 3
                if len(operationsStack) != 0:
                    if operationsStack[len(operationsStack) - 1] != '(':
                        if operationsStack[len(operationsStack) - 1] == 'cos' or operationsStack[len(operationsStack) - 1] == 'tg' or operationsStack[len(operationsStack) - 1] == 'ctg' or operationsStack[len(operationsStack) - 1] == 'sin':
                            resultExpressionArray.append(operationsStack.pop())
                            operationsStack.append('hex')
                        elif operationsStack[len(operationsStack) - 1] == 'bin' or operationsStack[len(operationsStack) - 1] == 'hex' or operationsStack[len(operationsStack) - 1] == 'oct':
                            resultExpressionArray.append(operationsStack.pop())
                            operationsStack.append('hex')
                        else:
                            operationsStack.append('hex')
                    else:
                        operationsStack.append('hex')
                else:
                    operationsStack.append('hex')
            else:
                hexDigit = expression[expressionStringIndex]
                wholeExpressionIndex += 1
                expressionStringIndex += 1
                while str.isdigit(expression[expressionStringIndex]) or expression[expressionStringIndex] == 'A' or expression[expressionStringIndex] == 'B' or expression[expressionStringIndex] == 'C' or expression[expressionStringIndex] == 'D' or expression[expressionStringIndex] == 'E' or expression[expressionStringIndex] == 'F':
                    hexDigit += expression[expressionStringIndex]
                    expressionStringIndex += 1
                    wholeExpressionIndex += 1
                    if expressionStringIndex == len(expression):
                        break
                resultExpressionArray.append(hexDigit)

        elif expression[expressionStringIndex] == 'o':
            if expression[expressionStringIndex + 1] == 'c':
                wholeExpressionIndex += 3
                expressionStringIndex += 3
                if len(operationsStack) != 0:
                    if operationsStack[len(operationsStack) - 1] != '(':
                        if operationsStack[len(operationsStack) - 1] == 'cos' or operationsStack[len(operationsStack) - 1] == 'tg' or operationsStack[len(operationsStack) - 1] == 'ctg' or operationsStack[len(operationsStack) - 1] == 'sin':
                            resultExpressionArray.append(operationsStack.pop())
                            operationsStack.append('oct')
                        elif operationsStack[len(operationsStack) - 1] == 'bin' or operationsStack[len(operationsStack) - 1] == 'hex' or operationsStack[len(operationsStack) - 1] == 'oct':
                            resultExpressionArray.append(operationsStack.pop())
                            operationsStack.append('oct')
                        else:
                            operationsStack.append('oct')
                    else:
                        operationsStack.append('oct')
                else:
                    operationsStack.append('oct')
            else:
                octDigit = expression[expressionStringIndex]
                wholeExpressionIndex += 1
                expressionStringIndex += 1
                while str.isdigit(expression[expressionStringIndex]):
                    octDigit += expression[expressionStringIndex]
                    expressionStringIndex += 1
                    wholeExpressionIndex += 1
                    if expressionStringIndex == len(expression):
                        break
                resultExpressionArray.append(octDigit)

        if expressionStringIndex == len(expression):
            if isWholeExpression:
                for i in range(len(operationsStack)):
                    if operationsStack[len(operationsStack) - 1] == '(':
                        continue
                    resultExpressionArray.append(operationsStack.pop())

def calculatePostfixExpression():
    numbersStack = []
    for element in resultExpressionArray:
        try:
            floatValue = float(element)
        except ValueError:
            if element[0] == 'b' and str.isdigit(element[1]):
                decimalValue = binOctHexFuncModule.fromBinToDec(element)
                numbersStack.append(float(decimalValue))
            elif element[0] == 'h' and (str.isdigit(element[1]) or element[1] == 'A' or element[1] == 'B' or element[1] == 'C' or element[1] == 'D' or element[1] == 'E' or element[1] == 'F'):
                decimalValue = binOctHexFuncModule.fromHexToDec(element)
                numbersStack.append(float(decimalValue))
            elif element[0] == 'o' and str.isdigit(element[1]):
                decimalValue = binOctHexFuncModule.fromOctToDec(element)
                numbersStack.append(float(decimalValue))
            elif element == '+':
                rightOperand = numbersStack.pop()
                rightOperand = convertToFloat(rightOperand)
                leftOperand = numbersStack.pop()
                leftOperand = convertToFloat(leftOperand)
                numbersStack.append(float(leftOperand + rightOperand))
            elif element == '-':
                rightOperand = numbersStack.pop()
                rightOperand = convertToFloat(rightOperand)
                leftOperand = numbersStack.pop()
                leftOperand = convertToFloat(leftOperand)
                numbersStack.append(float(leftOperand - rightOperand))
            elif element == '*':
                rightOperand = numbersStack.pop()
                rightOperand = convertToFloat(rightOperand)
                leftOperand = numbersStack.pop()
                leftOperand = convertToFloat(leftOperand)
                numbersStack.append(float(leftOperand * rightOperand))
            elif element == '/':
                rightOperand = numbersStack.pop()
                rightOperand = convertToFloat(rightOperand)
                leftOperand = numbersStack.pop()
                leftOperand = convertToFloat(leftOperand)
                numbersStack.append(float(leftOperand / rightOperand))
            elif element[0] == 's':
                lastOperand = numbersStack.pop()
                lastOperand = convertToFloat(lastOperand)
                numbersStack.append(trigonometricFuncModule.sine(lastOperand))
            elif element[0] == 'c' and element[1] == 'o':
                lastOperand = numbersStack.pop()
                lastOperand = convertToFloat(lastOperand)
                numbersStack.append(trigonometricFuncModule.cosine(lastOperand))
            elif element[0] == 't':
                lastOperand = numbersStack.pop()
                lastOperand = convertToFloat(lastOperand)
                numbersStack.append(trigonometricFuncModule.tangent(lastOperand))
            elif element[0] == 'c':
                lastOperand = numbersStack.pop()
                lastOperand = convertToFloat(lastOperand)
                numbersStack.append(trigonometricFuncModule.cotangent(lastOperand))
            elif element[0] == 'b':
                lastOperand = numbersStack.pop()
                lastOperand = convertToFloat(lastOperand)
                numbersStack.append(binOctHexFuncModule.fromDecToBin(lastOperand))
            elif element[0] == 'h':
                lastOperand = numbersStack.pop()
                lastOperand = convertToFloat(lastOperand)
                numbersStack.append(binOctHexFuncModule.fromDecToHex(lastOperand))
            elif element[0] == 'o':
                lastOperand = numbersStack.pop()
                lastOperand = convertToFloat(lastOperand)
                numbersStack.append(binOctHexFuncModule.fromDecToOct(lastOperand))
        else:
            numbersStack.append(floatValue)
    if isinstance(numbersStack[0], float):
        if numbersStack[0].is_integer():
            numbersStack[0] = int(numbersStack[0])
    return numbersStack[0]


def convertToFloat(number):
    try:
        floatNumber = float(number)
    except ValueError:
        if number[0] == 'b':
            floatNumber = float(binOctHexFuncModule.fromBinToDec(number))
        if number[0] == 'h':
            floatNumber = float(binOctHexFuncModule.fromHexToDec(number))
        if number[0] == 'o':
            floatNumber = float(binOctHexFuncModule.fromOctToDec(number))
    return float(floatNumber)

setWholeExpression('cos(85+tg(96))*hAC/1')