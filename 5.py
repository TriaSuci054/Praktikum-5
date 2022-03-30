'''
Nama    : Tria Suci Cahyani
NIM     : 20051397054
Kelas   : 2020B
'''


def postfix(expr):
    if len(expr)<=0 or not isinstance(expr,str): 
        print("expr error: postfix")
        return "error"
    expr=expr.strip()
    items=Stack()
    outputVariable = ""
    pos=0

    for i in range(len(expr)):
        if expr[i] in '+-*/^()':  
            items.push(expr[pos:i].strip())  
            items.push(expr[i])    # operator
            pos=i+1  
            items.push(expr[pos:].strip())

        elif expr[i] is '1234567890':
            outputVariable += i
        elif expr[i] is '(':
            items.push(expr[i])
        elif expr[i] is ')':
            while True:
                temp = items.pop()
                if temp is None or temp == '(':
                    break
                else:
                    outputVariable += temp

        elif expr[i] in '+-*/^' and (items is False or items.peek() is '('):
            items.push(expr[i])
        elif PrecedenceCheck(expr[i]) is True:
            items.push(expr[i])

        elif expr[i] in '+-*/^' and PrecedenceCheck(expr[i]) is False:
        while True:
            items.pop()
            if items.isEmpty() is True:
                items.push(expr[i])
                break
    return outputVariable

precedence = {}
precedence['*'] = 3
precedence['/'] = 3
precedence['+'] = 2
precedence['-'] = 2
precedence['('] = 1
precedence['^'] = 1

def PrecedenceCheck(char):
    items=Stack()
    outputVariable= " "
    if char in '1234567890':
        return False
    elif PrecedenceCheck(char) is True:
        while precedence[char] < precedence[items.peek()]:
            x = items.pop()
            x += outputVariable
            items.push(char)
        return outputVariable
     else:
         return 'error message'







