def josephus(n, k):
    if n == 1:
        return 1
    else:
        return (josephus(n - 1, k) + k - 1) % n + 1

# Example usage:
n = int(input("Enter the number of people: "))
k = int(input("Enter the step count: "))
print("The safe position is:", josephus(n, k))
