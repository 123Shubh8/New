def iterative_fibonacci(n):
    if n <= 0:
        print(0)
        return 0
    elif n == 1:
        print(1)
        return 1

    fib = [0, 1]
    print(0)
    print(1)
    for i in range(2, n + 1):
        fib.append(fib[-1] + fib[-2])
        print(fib[-1])
    return fib[-1]

def recursive_fibonacci(n, fib_list=None):
    if fib_list is None:
        fib_list = [0, 1]
    if n < len(fib_list):
        return fib_list[n]
    else:
        fib_number = recursive_fibonacci(n - 1, fib_list) + recursive_fibonacci(n - 2, fib_list)
        if n == len(fib_list):
            fib_list.append(fib_number)
            print(fib_number)
        return fib_number

# Helper function to initialize the recursive approach
def print_recursive_fibonacci(n):
    fib_list = [0, 1]
    for i in range(n + 1):
        if i < len(fib_list):
            print(fib_list[i])
        else:
            recursive_fibonacci(i, fib_list)

# Main function to handle user input
def main():
    print("Choose Fibonacci method:")
    print("1. Iterative")
    print("2. Recursive")
    choice = int(input("Enter your choice (1 or 2): "))

    n = int(input("Enter the number of terms (n): "))

    if choice == 1:
        print("\nIterative Approach:")
        iterative_fibonacci(n)
    elif choice == 2:
        print("\nRecursive Approach:")
        print_recursive_fibonacci(n)
    else:
        print("Invalid choice! Please enter 1 or 2.")

# Execute the main function
if __name__ == "__main__":
    main()
