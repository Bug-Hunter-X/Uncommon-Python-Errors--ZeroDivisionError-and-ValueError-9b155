import math
def function_with_improved_error_handling(x):
    try:
        if x == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        elif x < 0:
            raise ValueError("Cannot calculate square root of a negative number.")
        else:
            return x + 5
    except ZeroDivisionError as e:
        print(f"Error: {e}")
        return None
    except ValueError as e:
        print(f"Error: {e}")
        return None

# Example usage
result1 = function_with_improved_error_handling(0)
result2 = function_with_improved_error_handling(-1)
result3 = function_with_improved_error_handling(5)
print(f"Result 1: {result1}")
print(f"Result 2: {result2}")
print(f"Result 3: {result3}") 