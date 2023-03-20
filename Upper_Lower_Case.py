# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.



# Sample String : 'The quick Brow Fox'

# Expected Output :

# No. of Upper case characters : 3

# No. of Lower case Characters : 12

#Code

p=input("Enter the string:- ")
def char(p):
  k=0
  b=0
  for i in p:
      if i>='a' and i<='z':
       b+=1

      if i >='A' and i<='Z':
       k+=1

  print("LowerCase letter in the String",b)
  print("UpperCase letter in the String",k)
char(p)                                         #Enter the string in terminal any upper or lower case it shown you the output.