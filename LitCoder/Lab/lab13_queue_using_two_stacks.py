class QueueWithTwoStacks:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, x):
        # Push element to the input stack
        self.stack_in.append(x)

    def dequeue(self):
        # If stack_out is empty, transfer all elements from stack_in
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        # Pop from stack_out (front of the queue)
        if self.stack_out:
            self.stack_out.pop()

    def print_front(self):
        # If stack_out is empty, transfer all elements from stack_in
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        # Print the element at the front of the queue
        if self.stack_out:
            print(self.stack_out[-1])

# Parse the input and execute queries
def process_queries(queries):
    queue = QueueWithTwoStacks()

    for query in queries:
        if query.startswith("1"):
            _, x = query.split()  # Enqueue operation
            queue.enqueue(int(x))
        elif query == "2":
            queue.dequeue()  # Dequeue operation
        elif query == "3":
            queue.print_front()  # Print the front element

# Accept input from the user
def main():
    # Accept queries as a single line of input, split by commas
    input_queries = input("Enter queries (comma-separated): ").split(",")
    
    # Strip leading/trailing spaces from each query
    input_queries = [query.strip() for query in input_queries]
    
    # Process the list of queries
    process_queries(input_queries)

if __name__ == "__main__":
    main()
                                                                                                                            
