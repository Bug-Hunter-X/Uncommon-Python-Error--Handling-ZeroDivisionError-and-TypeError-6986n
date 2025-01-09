def improved_division(x, y):
    if y == 0:
        print("Error: Division by zero")
        return None
    elif not isinstance(y,(int,float)):
        print("Error: Cannot divide by non-numeric type.")
        return None
    else:
        return x / y

# Example usage
print(improved_division(10, 0))
print(improved_division(10, 2))
print(improved_division(10, "hello"))