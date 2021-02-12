"""
Name: Max S.
Purpose: To identify a right angle triangle from its side lengths. 
Date: Feb, 12 2021
"""

 # User inputs side lengths
length_1 = int(input("Enter the length of side 1: "))
length_2 = int(input("Enter the length of side 2: "))
length_3 = int(input("Enter the length of side 3: "))

 # Calculations and display of data
if length_1 ** 2 + length_2 ** 2 == length_3 ** 2 or length_1 ** 2 + length_3 ** 2 == length_2 ** 2 or length_3 ** 2 + length_2 ** 2 == length_1 ** 2:
  print("The triangle with side lengths", str(length_1) + ",", str(length_2) + ", and", length_3 ,"form a right-angled triangle.")
else: 
  print("The triangle with side lengths", str(length_1) + ",", str(length_2) + ", and", length_3 ,"does not form a right-angled triangle.")