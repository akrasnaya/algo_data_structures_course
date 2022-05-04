from task4 import Stack


def balanced_string(string):
    stack = Stack()
    for s in string:
        if s == '(':
            stack.push(s)
        else:
            if stack.size() == 0:
                return False
            stack.pop()
    return stack.size() == 0


def postfix_form(stack1):
    stack2 = Stack()
    for element in stack1.stack:
        if element == '+':
            stack2.push(stack2.pop() + stack2.pop())
        elif element == "*":
            stack2.push(stack2.pop() * stack2.pop())
        elif element == "-":
            stack2.push(stack2.stack[0] - stack2.stack[1])
            stack2.pop()
            stack2.pop()
        elif element == '/':
            stack2.push(stack2.stack[0] / stack2.stack[1])
            stack2.pop()
            stack2.pop()
        elif element == "=":
            return stack2.stack[0]
        else:
            stack2.push(element)

