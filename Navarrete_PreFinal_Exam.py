def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

while True:
    start = int(input("Enter the starting number (enter 0 to terminate): "))
    
    if start < 0:
        print("Enter a non-negative number.")
        continue
    
    if start == 0:
        print("Program terminated.")
        break
    
    end = int(input("Enter the ending number: "))
    
    if end <= start:
        print("Enter a number greater than the starting number.")
        continue
    
    print(f"Prime numbers between {start} and {end}:")
    
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)
