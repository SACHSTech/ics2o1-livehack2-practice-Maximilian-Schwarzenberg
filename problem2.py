"""
Name: Max S.
Purpose: To find out if you are able to go on vacation during the summer. 
Date: Feb, 12 2021
"""

 # Input of data
mark = int(input("What is your average? (%): "))
earnings_before = int(input("What is your earnings before the summer?: $"))

 # Processing and Display of the data
if mark >= 80 and earnings_before >= 500: 
  print("You can now for vacation to Europe!")
elif mark >= 80 and earnings_before < 500: 
  print("You can now for vacation to California!")
else: 
  print("You did not achieve an average of 80% or over or earn $500 so you can not go on vacation. You need",80 - mark,"more of an average and $",500 - earnings_before,"more money.")