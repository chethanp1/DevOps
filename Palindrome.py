#Palindrome program using string  def is_palindrome(s):
s = str(s) # Convert to string (works for numbers too)
if s == s[::-1]:
return "Palindrome"
else:
return "Not Palindrome"

# Input
value = input("Enter a string or number: ")
print(is_palindrome(value);