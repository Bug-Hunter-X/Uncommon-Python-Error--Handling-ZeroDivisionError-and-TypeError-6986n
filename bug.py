def function_with_uncommon_error(x, y):
    try:
        result = x / y
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Unsupported operand type(s) for / ")
        return None

# Example usage
print(function_with_uncommon_error(10, 0))
print(function_with_uncommon_error(10, 2))
print(function_with_uncommon_error(10, "hello"))