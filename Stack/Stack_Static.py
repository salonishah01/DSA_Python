def main():

    max_stack = 5  # length the stack
    inputs_operation = [
        # [operation, value] => [0: pop; 1: push]
        [0],
        [1, 5],
        [0],
        [0],
        [1, 4],
        [1, 3],
        [0],
        [0],
        [1, 10],
        [1, -2],
        [1, 256],
        [1, 46],
        [1, 30],
        [1, -5866]
    ]

    stack = Stack(max_stack)

    for input_l in inputs_operation:
        try:
            if(input_l[0] == 0):  # Remove
                print('POP:', end=' ')
                print(f'{stack.pop()}')
            else:  # Add
                print(f'PUSH: {input_l[1]} => ', end=' ')
                stack.push(input_l[1])
                print("OK")
        except Exception as identifier:
            print(identifier)
        stack.show()


class Stack:

    def __init__(self, length):
        self.length = length  # Length stack
        self.top = -1         # Actual position top the stack
        self.data = [None for i in range(self.length)]  # Data

    def push(self, value):
        # Add new item in top stack

        if(self.__is_full()):
            raise Exception('Stack Full')

        self.top += 1
        self.data[self.top] = value
        return self.data[self.top]

    def pop(self):
        # Remove item top stack

        if(self.__is_empty()):
            raise Exception('Stack Empty')

        item = self.data[self.top]
        self.data[self.top] = None
        self.top -= 1
        return item

    def __is_empty(self):
        # Check if stack is empty

        return self.top == -1

    def __is_full(self):
        # Check if stack is full

        return self.top + 1 == self.length

    def show(self):
        # Print stack

        print(f'Status: (max: {self.length})')
        if(self.__is_empty()):
            print("|- Empty")
        else:
            for i in range(self.top, -1, -1):
                print(f'|- {self.data[i]}')
        print('----------\n')


main()
