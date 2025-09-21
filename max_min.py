numbers = []

while True:
    user_input = input("Enter a number (or 'done' to finish): ")
    if user_input.lower() == "done":
        break
    try:
        num = int(user_input)
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if numbers:
    print("Maximum is", max(numbers))
    print("Minimum is", min(numbers))
else:
    print("No valid numbers were entered.")
