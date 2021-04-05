# printing basic
# print("Akshat Pandey")
# print("o----")
# print(" ||||")
# print('*' * 10)
# end

# variables
# price = 10
# price = 20  # price updated because line by line interpretion
# rating = 4.9
# name = 'Akshat'
# is_published = True
# print(price)
# end

# taking input
# name = input("What is your name? ")
# print("Hi " + name)
# color = input("What is your favourite color? : ")
# print("Your favourite color is " + color)
# print(name + " likes " + color)
# end



# type conversion ( to convert string to int )
#Birth_YEar = input("What is your Birth Year : ")
#print(type(Birth_YEar))
#age = 2020 - int(Birth_YEar)
#print(type(age))
#print(age)
# always convert input (string) to int or float
#weight = input("What is your weight(in KG) : ")
#gram = int(weight) * 1000
#print(gram)
# emd

#strings
#course = '''python
#for
#begineers'''
#print(course[-2])
#print(course[0:3])
#another=course[:]
#print(course)

#name = 'Jennifer'
#print(name[1:-1])

#Formatted Strings
#first = 'John'
#last = 'Smith'
#message = first + '['  + last + ']' + 'is a coder' #unformatted
#msg = f'{first} [{last}] is a coder' #formatted
#print(msg)

#string methods
#course = 'Python for begineers'
#print("NUmber of Characters are : ",len(course)) #to print number of charaters
#print(course.upper()) #for upper case (doesnt change base string)
#print(course.lower())
#print(course.find('P'))
#print(course.replace('P','Q'))
#print('Python' in course)  #to check if present (bool)

#print(10**2) #** for power

#math functions
#import math
#x=-2.9;
#print(round(x))
#print(abs(x))
#print(math.ceil(x))
#print(math.floor(x))

#if statement
#is_hot = True
#is_cold = False

#if is_hot:
#  print("""It's a hot day
#drink plenty of water
#enjoy your day""")
#elif is_cold:
 #   print("""It's a cold day
#Wear warm clothes""")
#else:
  #  print("It's a lovely day")

#question to print downpayment
#price=100000
#has_credit=True

#if has_credit:
#    down_payment = 0.1 * price
#else:
#    down_payment = 0.2 * price
#print(f"Down Payment : {down_payment}")

#logical operators
#has_high_income = True
#has_good_credit = True
#has_criminal_record =True

#if has_high_income and has_good_credit and not has_criminal_record: #and, or ,and not
#    print("Elegible for loan")

#comparison operator
#temp= 30
#if temp >= 30 :
#    print("It's a hot day")
#else :
#    print("It's not a hot day")

#name = "Akshat"

#if len(name) <3 :
#    print("Name must be atleast 3 characters")
#elif len(name)>10:
#    print("Max length of name is 10 characters")
#else:
#    print("Name looks good")

#while loop
#i = 0
#while i<5:
#    print("*" * i)
#    i+=1
#print("Done")

#guessing game
#secret_num=9;
#guess_count=0
#guess_limit=3;
#while guess_count<guess_limit:
#   guess = int(input("Guess : "))
#   guess_count+=1
#   if guess == secret_num :
#       print("You Won")
#       break
#else :
#    print("Number of try limit reached, you failed")
 #car game
#command = ""
#while true:
#    command = input("> ").lower()
#if command =="start":
#    print("Car Started...")
#elif command =="stop":
#    print("Car Stopped...")
#elif command == "help":
#    print("""
#start - to start the car
#stop - to stop the car
#quit - to quit
 #   """)
#elif command == "quit":
#    break
#else:
#    print("Sorry, didn't understand")

#for loops
#for item in "Python":
#for item in ["Akshat", "Pandey", "Lullu"]:
#for item in range(100):
#for item in range(5,10,2):
#print(item)
#shopping cart
#prices = [10,20,30]
#total = 0
#for price in prices :
#    total += price
#print(f"Total : {total}")

#nested loops
#for x in range(4):
#    for y in range(3):
#        print(f"({x},{y})")

#numbers = [1,1,1,1,5]
#for x in numbers :
    #print("x" * x) #simple way
#    output = ""
#    for y in range(x):
#        output += "x"
#    print(output)

