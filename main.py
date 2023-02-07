# stack = []
#
# stack.append(10)
# stack.append(20)
# stack.append(30)
#
# print(stack)
#
# stack.pop()
# print(stack)
#
# print(len(stack) == 0)
#
# print(stack[-1])

stack = []


def push():
    element = input('Enter a value to push in stack')
    stack.append(element)
    print(stack)


def pop_out():
    if not stack:
        print('Stack is empty')
    else:
        element = stack.pop()
        print(f'Element removed = {element}')
        print(stack)


while True:
    print('Press 1 for push operation')
    print('Press 2 for pop operation')
    choice = int(input())
    if choice == 1:
        push()
    elif choice == 2:
        pop_out()
    else:
        print('Enter correct option')
