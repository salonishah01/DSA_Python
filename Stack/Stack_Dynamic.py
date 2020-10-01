def main():

    inputs_operation = [
        # [operation, value] => [0: remove - pop; 1: add - push]
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

    stack = Stack()
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


class Item:

    def __init__(self, value, next):
        self.value = value  # Value
        self.next = next    # reference next item


class Stack:

    def __init__(self):
        self.head = Item(0, None)  # Head stack - globa reference to head stack

    def push(self, value):
        # Add new item in top stack

        self.head.next = Item(value, self.head.next)
        return self.head.next

    def pop(self):
        # Remove item top stack

        if(self.__is_empty()):
            raise Exception('Stack Empty')

        item = self.head.next
        self.head.next = item.next
        return item.value

    def __is_empty(self):
        # Check if stack is empty

        return self.head.next == None

    def show(self):
        # Print stack

        print(f'Status:')
        if(self.__is_empty()):
            print("|- Empty")
        else:
            item_actual = self.head.next
            while item_actual != None:
                print(f'|- {item_actual.value}')
                item_actual = item_actual.next
        print('----------\n')


main()
