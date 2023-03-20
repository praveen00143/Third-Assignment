# Write a Python program to reverse a string.

# Sample String : "1234abcd"

# Expected Output : "dcba4321"




def reverse(str):
   new_str = "  "
   for i in str:
         new_str = i + new_str
   return new_str
str = "72YcHtApX"
print("The original string is:", str)
print("The reverse string is:",reverse(str))