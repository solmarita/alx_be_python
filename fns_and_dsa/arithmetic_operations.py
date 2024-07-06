def perform_operation(num1, num2, operation):
    """Does basic arithmetic: Add, Subtract, Multiply, and Divide"""

    if operation not in ("add", "subtract", "multiply", "divide"):
        return "Enter a valid operation, ie. add, subtract, multiply, or divide"
    
    if operation == "divide":
        if num2 == 0:
            return "Can not divide by Zero!"
        elif:
            return num1 / num2
        else:

        

    if operation == "add":
        return num1 + num2
    
    if operation == "subtract":
        return num1 - num2
    
    if operation == "multiply":
        return num1 * num2