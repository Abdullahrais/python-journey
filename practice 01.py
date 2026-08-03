# import pyttsx3
# engine = pyttsx3.init()

# # For Mac, If you face error related to "pyobjc" when running the `init()` method :
# # Install 9.0.1 version of pyobjc : "pip install pyobjc>=9.0.1"

# engine.say("My name is Yahya and I am learning python programming language")
# engine.runAndWait()

# import pyttsx3
# password=int(input("Enter your password: "))
# if password>=12345:
#     print("success")
#     pyttsx3.speak("success")
# else:
#      print("not valid")
#      pyttsx3.speak("not valid")
 


# name = "Ali"      # Text (string)
# age = 16          # Number (integer)
# marks = 85.5      # Decimal (float)
# passed = True     # True/False (boolean)



# practice 
# age=int(input("Enter your age"))
# if age >=18:
#     print("You are an adult")
# else:
#     print("You are not an adult")

# Practice2
# user=int(input("Enter your age:"))
# if user>=60:
#      print("senior citizen")
# elif user>=18:
#     print("aap vote de sakhte hain")
# else:
#     print("aap vote nhi de sakhte hai.")

# # practice3
# user=int(input("enter your marks:"))
# if user>=90:
#     print("A1")
# elif user>=80:
#     print("A")
# elif user>=70:
#     print("B")
# elif user>=60:
#     print("C")
# else:
#     print("fail")



# practice 
# age=int(input("enter your age"))
# cnic=input("yes/no")
# if age>=18 and cnic=="yes":
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")


# ATMLogin1
# password=int(input("enter your password: "))
# if password>=12345:
#     print("success")
# else:
#     print("wrong password")

# Even/Odd Number
# user=int(input("enter your number: "))
# if user%2==0:
#     print("even")
# else:
#     print("odd")

# traffic light
# user=input("enter a color: ")
# if user=="red":
#     print("stop")
# elif user=="yellow":
#     print("ready")
# elif user=="green":
#     print("go")

# username=input("enter your name: ")
# password=int(input("enter your password: "))
# if username=="abdullah" and password==1234:
#     print("login")    
# else: print("try again")


# username = input("Enter your name: ")

# if username == "abdullah":
#     password = int(input("Enter your password: "))

#     if password == 1234:
#         print("Login Success")
#     else:
#         print("Wrong Password")

# else:
#     print("Invalid Username")

# Data Type	Description	Example
# int	Whole numbers	10, -5, 1000
# float	Decimal numbers	3.14, 99.5
# str	Text/String	"Hello", 'Python'
# bool	True or False values	True, False
# list	Ordered, mutable collection	[1, 2, 3]
# tuple	Ordered, immutable collection	(1, 2, 3)
# set	Unordered collection of unique items	{1, 2, 3}
# dict	Key-value pairs	{"name": "Ali", "age": 20}


# user = "abdullah"
# print(type(user)


# user=int(input("enter your marks:"))
# if user>=90:
#     print("A1")
# elif user>=80:
#     print("A")
# elif user>=70:
#     print("B")
# elif user>=60:
#     print("C")
# else:
#     print("fail")

     
# for loop
# Qno 1 pracice chat gpt

# for i in range(1,6):
#     print(i)


# Qno2
# for i in range(2,21,2):
#     print(i)
# Qno3
# for i in range(1,11).__reversed__():
#     print(i)
# Qno4
# n=int(input("konse tabel chaiye aap ko: "))
# for i in range(1,11):
#     print(f"{n} x {i} = {n*i}")

# Qno 5
# n=int(input("enter a number: "))
# for i in range(1,n+1,2):
#     print (i)
# Qno6
# n=int(input("enter a number :"))
# for i in range(1,n+1):
#     print(i*i) 
  
# Qno7
# for i in range(1,6):  
#     print(i*"*")

#//////////////////

# for i in range(5):
#     user=str(input("enter your name :"))
#     print(f"{i} welcome {user}")

first_name=str(input("first name :"))
last_name=str(input("last  name :"))

full_name=first_name+"   "+last_name
print(f"{full_name }")

