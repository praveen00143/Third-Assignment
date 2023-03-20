# Write a Python function to sum all the numbers in a list.



# Sample List : (8, 2, 3, 0, 7)

# Expected Output : 20


list = [1, 10, 25, 9 ,33, 0,22]
def num(l):
   sum = 0
   for x in l:
      sum = sum + x
   return sum

print("sum of list : ",num(list))