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
        [0],
        [1, -5866]
    ]

    queue = Queue()

    for input_l in inputs_operation:
        try:
            if(input_l[0] == 0):  # Remove
                print('DEQUEUE:', end=' ')
                print(f'{queue.dequeue()}')
            else:  # Add
                print(f'ENQUEUE: {input_l[1]} => ', end=' ')
                queue.enqueue(input_l[1])
                print("OK")
        except Exception as identifier:
            print(identifier)
        queue.show()


class Item:

    def __init__(self, value):
        """
        Constructor
        """
        self.value = value  # Value
        self.next = None    # Reference to next item


class Queue:

    def __init__(self):
        """
        Constructor
        """
        self.head = Item(0)  # Head queue - globa reference to head queue
        self.back = self.head  # Reference back(last) item in the queue

    def enqueue(self, value):
        """
        Add. new value at the end of the queue
        """
        self.back.next = Item(value)
        self.back = self.back.next
        return self.back

    def dequeue(self):
        """
        Remove the value at the front of the queue
        """

        if(self.__is_empty()):
            raise Exception('Queue Empty')

        item = self.head.next
        self.head.next = item.next

        if(self.__is_empty()):
            self.back = self.head

        return item.value

    def __is_empty(self):
        """
        Check if queue is empty
        """
        return self.head.next == None

    def peek(self):
        """
        Return the value in the front queue
        """

        return self.head.next if not self.__is_empty() else None

    def show(self):
        """
        Show all item in the queue
        """
        print(f'Status:')
        if(self.__is_empty()):
            print("|- Empty", end='')
        else:
            item_actual = self.head.next
            while item_actual != None:
                print(f'{item_actual.value}', end='; ')
                item_actual = item_actual.next
        print('\n-----------------------\n')


main()
