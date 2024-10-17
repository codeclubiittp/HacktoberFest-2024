# Stack class
class Stack:
    def __init__(self):
        self.stack = []

    # Function to check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Function to push an element onto the stack
    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed to stack")

    # Function to pop an element from the stack
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    # Function to peek at the top element of the stack
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    # Function to display the entire stack
    def display(self):
        print(f"Stack: {self.stack}")


# Example usage
if __name__ == "__main__":
    my_stack = Stack()

    # Pushing elements onto the stack
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)

    # Display the current stack
    my_stack.display()

    # Peek at the top element
    print(f"Top element is {my_stack.peek()}")

    # Popping elements from the stack
    print(f"Popped element: {my_stack.pop()}")
    print(f"Popped element: {my_stack.pop()}")

    # Display the current stack
    my_stack.display()

    # Check if the stack is empty
    print(f"Is stack empty? {my_stack.is_empty()}")
