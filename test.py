# Qno-1 Write a program that print the numbers from 1 to 10 using loop

# for i in range(1,11):
#     print(i)

#///////////////////

# Qno-2 Write a program to print even numbers from 1 to 10.

# for i in range(2,11,2):
#  print(i)

#///////////////////

# Qn0-3  Write a program that prints 'Happy Birthday!' five times on screen.

# for i in range(5):
#     print("Happy birthday")

#/////////////////////////

# Qno-4 Write a program that takes a number n as input from the user and generates the first n terms of 
# the series formed by squaring the natural numbers. Sample output Enter a number: 6 The first 6 terms 
# of the series are: 1 4 9 16 25 36

# n=int(input("enter your number :"))

# print(f"the first {n} term of the series are :")
# for i in range(1,n+1):
#    print(i*i,end=" ")

#//////////////////////

# Qno-5 Write a program that prompts the user to input a number and prints its multiplication table.

# num=int(input("Kis number ka table chahiye? :"))
# for i in range (1,11):
#     print(f"{num} x {i} = {num*i}")

#////////////////////

# Qno-6 Write a program that prompts the user to enter a number n, and then prints
# all the odd numbers between 1 and n.


# n = int(input("Enter a number: "))

# for i in range(1, n + 1, 2):
#     print(i)

#//////////////////

# Qno-7 Write a Python program to print the numbers from 20 to 1 using a while loop.

num=20
while num >= 1:
  print(num)
  num-=1

#/////////////////////

# Qno-8 Write a program that prompts the user to enter a number n and prints all the numbers from 1 to n.

# n=int(input("enter your number :"))

# for i in range(1,n+1):
#     print(i)

#////////////////////
#Qno-9Write a program that prompts the user to enter a number and repeats this process 5 times. 
# The program should accumulate the numbers entered and then display the final running total.

# total = 0

# for i in range(5):
#     num = int(input("Enter a number: "))
#     total += num

# print(f"Final total = {total}")


#////////////////////////

# Qno-10 Write a Python program that:
# 1- Creates a list named clean_countries containing the following countries: [Bangladesh India Pakistan China]

# 2- Repeatedly asks the user to enter a country name.

# 3- Checks whether the entered country exists in the clean_countries list.

# 4-If the country is found in the list:

# Display the message:

# <country_name> is in clean countries list

# Stop the program.

# 5-If the country is not found, keep asking the user to enter another country.

# clean_countries = ["Bangladesh", "India", "Pakistan", "China"]

# while True:
#     country = input("Enter country name: ").title()

#     if country in clean_countries:
#         print(f"{country} is in clean countries list")
#         break
#     else:
#         print("Country not found. Try again.")
