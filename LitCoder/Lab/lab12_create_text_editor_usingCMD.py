class CustomStack:
    def __init__(self):
        self.text = []  # List to store the text as a series of characters
        self.history = []  # Stack to track operations for undo
    
    def insert(self, value):
        # Insert value at the current position (end of text)
        self.text.extend(value)
        # Save the reverse operation to undo stack
        self.history.append(('delete', len(value)))
    
    def delete(self, value):
        # Delete the last 'value' characters from the text
        deleted = self.text[-value:] if value <= len(self.text) else self.text[:]
        self.text = self.text[:-value] if value <= len(self.text) else []
        # Save the reverse operation to undo stack
        self.history.append(('insert', ''.join(deleted)))
    
    def get(self, value):
        # Return the character at index value (1-based index)
        if 1 <= value <= len(self.text):
            return self.text[value-1]
        else:
            return ''  # Return an empty string if index is out of bounds
    
    def undo(self):
        if not self.history:
            return  # No operations to undo
        last_operation, last_value = self.history.pop()
        # Reverse the last operation
        if last_operation == 'delete':
            self.text = self.text[:-last_value] if last_value <= len(self.text) else []
        elif last_operation == 'insert':
            self.text.extend(last_value)

def process_commands(commands):
    custom_stack = CustomStack()
    result = []
    
    for command in commands:
        operation = command.split()
        cmd = operation[0]
        if cmd == '1':
            # Insert the string value
            custom_stack.insert(operation[1])
        elif cmd == '2':
            # Delete last 'value' characters
            custom_stack.delete(int(operation[1]))
        elif cmd == '3':
            # Get the character at index value and add to result
            result.append(custom_stack.get(int(operation[1])))
        elif cmd == '4':
            # Undo the last operation
            custom_stack.undo()
    
    return result

# Input format processing
def parse_input(input_string):
    commands = input_string.split(',')
    return commands

# Driver code
if __name__ == "__main__":
    # Taking input from the user
    input_string = input("Enter the commands: ")  # e.g., '1 abc,3 3,2 2,3 1'
    commands = parse_input(input_string)
    
    # Process the commands and get the output
    output = process_commands(commands)
    
    # Display the output
    for char in output:
        print(char)
                                                                                                                            
