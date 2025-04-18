# Problem-2: With a single integer as the input, generate the following until a = x [series of numbers as shown in below examples]
 
#   Output: (examples)
#     1) input a = 1, then output : 1
#     2) input a = 2, then output : 1, 3
#     3) input a = 3, then output : 1, 3, 5
#     4) input a = 4, then output : 1, 3, 5, 7
#     .
#     .
#     5) input a = x, then output : 1, 3, 5, 7, .......

# Solution
def generate_series(a: int) -> str:
    series = [str(2 * i + 1) for i in range(a)]
    return ', '.join(series)

# Example usage:
a = 4
print(generate_series(a))  # Output: 1, 3, 5, 7