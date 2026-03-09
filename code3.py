# Take input from user
value = input("Enter a string or number: ")

# Check if the value is equal to its reverse
if value == value[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
