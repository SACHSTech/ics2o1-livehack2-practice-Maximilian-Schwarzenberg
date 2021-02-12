"""
Name: Max S.
Purpose: To identify a right angle triangle from its side lengths. 
Due date: ?
"""

 # User inputs side lengths
length1 = int(input("Enter the length of side 1: "))
length2 = int(input("Enter the length of side 2: "))
length3 = int(input("Enter the length of side 3: "))

 # Calculations and display
if length1 ** 2 + length2 ** 2 == length3 ** 2:
  print("The triangle with side lengths",length1,",",length2,", and",length3,"form a right-angled triangle.")
else: 
  print("The triangle with side lengths",length1,",",length2,", and",length3," does not form a right-angled triangle.")