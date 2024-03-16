'''
Exercise 1: Mailing Address
(Solved—9 Lines)
Create a program that displays your name and complete mailing address formatted in
the manner that you would usually see it on the outside of an envelope. Your program
does not need to read any input from the user

# solution

print(" Chukwudi David Okoro")
print(" BackEnd Developer")
print(" Lagos Nigeria")

'''


'''
# Exercise 2: Hello

# Write a program that asks the user to enter his or her name. The program should
# respond with a message that says hello to the user, using his or her name.

def greetings():
  name = input("What is your name ?")
  print(f"Hello {name}")

greetings()

'''

'''
# Exercise 3: Area of a Room

# Write a program that asks the user to enter the width and length of a room. Once
# the values have been read, your program should compute and display the area of the
# room. The length and the width will be entered as floating point numbers. Include
# units in your prompt and output message; either feet or meters, depending on which
# unit you are more comfortable working with.

width = float(input("Enter the width of your room in ft ? "))
lenght = float(input("Enter the lenght of your room in ft ? "))
area = width * lenght
print(f"The area of your room is {area} sqft")

'''



'''
# Exercise 4: Area of a Field

# Create a program that reads the length and width of a farmer’s field from the user in
# feet. Display the area of the field in acres.
# Hint: There are 43,560 square feet in an acre


width = float(input("Enter the width of your farm in ft ? "))
lenght = float(input("Enter the lenght of your farm in ft ? "))
area = width * lenght
acre = area / 43560
print(f"The area of your field is {acre} acre ")

'''



'''
# Exercise 5: Bottle Deposits

# In many jurisdictions a small deposit is added to drink containers to encourage people
# to recycle them. In one particular jurisdiction, drink containers holding one liter or
# less have a $0.10 deposit, and drink containers holding more than one liter have a
# $0.25 deposit.
# Write a program that reads the number of containers of each size from the user.
# Your program should continue by computing and displaying the refund that will be
# received for returning those containers. Format the output so that it includes a dollar
# sign and always displays exactly two decimal places.

import random
Oneltr_amount = 0.10
Twoltr_amount = 0.25

_1liters_ques = int(input("How many 1 liters or less do you have ? "))
_2liters_ques = int(input("How many 2 liters or higher do you have ? "))

total_1ltr = _1liters_ques * Oneltr_amount
total_2ltr = _2liters_ques * Twoltr_amount

grandTotal = round(total_1ltr + total_2ltr, 2)
print(f" Your total refund is ${grandTotal}")


'''


'''
# Exercise 6: Tax and Tip
#
# The program that you create for this exercise will begin by reading the cost of a meal
# ordered at a restaurant from the user. Then your program will compute the tax and
# tip for the meal. Use your local tax rate when computing the amount of tax owing.
# Compute the tip as 18 percent of the meal amount (without the tax). The output from
# your program should include the tax amount, the tip amount, and the grand total for
# the meal including both the tax and the tip. Format the output so that all of the values
# are displayed using two decimal places

tax_rate = 0.05
cost = int(input("What is the cost of the meal ? $ "))
tip = cost * 0.18
grandTotal = cost + tax_rate + tip
print(f"Your tax amount is ${tax_rate:.2f} , \n your tip is ${tip:.2f} \n and the grand total for the meal is {grandTotal:.2f}")

'''



'''
# Exercise 7: Sum of the First n Positive Integers

# Write a program that reads a positive integer, n, from the user and then displays the
# sum of all of the integers from 1 to n. The sum of the first n positive integers can be
# computed using the formula:
# sum = (n)(n + 1) / 2

number = int(input("Input a positive number"))
sum_of_num = (number * ( number + 1 )) / 2
print(sum_of_num)

'''


'''

# Exercise 8:Widgets and Gizmos
#
# An online retailer sells two products: widgets and gizmos. Each widget weighs 75
# grams. Each gizmo weighs 112 grams. Write a program that reads the number of
# widgets and the number of gizmos in an order from the user. Then your program
# should compute and display the total weight of the order

widget = 75
gizmo = 112

gizmo_count = int(input("How many Gizmo ? "))
widget_count = int(input("How many Widget ? "))

print(f"The total weight of your order is {(gizmo * gizmo_count) + (widget * widget_count)}gram")

'''

'''
# Exercise 9: Compound Interest
#
# Pretend that you have just opened a new savings account that earns 4 percent interest
# per year. The interest that you earn is paid at the end of the year, and is added
# to the balance of the savings account. Write a program that begins by reading the
# amount of money deposited into the account from the user. Then your program should
# compute and display the amount in the savings account after 1, 2, and 3 years. Display
# each amount so that it is rounded to 2 decimal places.

percentage_amount = 4
amount_deposited = int(input("What is the amount deposited ? $"))
print(f"After 1st year you'd earn ${(amount_deposited + (percentage_amount))} \n 2nd year you'd earn ${(amount_deposited + (percentage_amount * 2 )) } \n 3rd year you'd earn ${(amount_deposited + (percentage_amount * 3))}")

'''



'''
# Exercise 10: Arithmetic
#
# Create a program that reads two integers, a and b, from the user. Your program should
# compute and display:
# • The sum of a and b
# • The difference when b is subtracted from a
# • The product of a and b
# • The quotient when a is divided by b
# • The remainder when a is divided by b
# • The result of log10 a
# • The result of ab
import math

a = int(input("Enter Your first number ? "))
b = int(input("Enter Your second number ? "))

Sum = a + b
Sub = b - a
Mul = a * b
Div = a / b
remainder =  a % b
log10 = math.log10(a)
power = a**b

print(f"The sum is {Sum} \n The difference is {Sub} \n The product is {Mul} \n The quotient is {Div} \n The remainder is {remainder} \n The Base10 is {log10} \n The power is {power}")

'''

'''
# Exercise 11: Fuel Efficiency
#
# In the United States, fuel efficiency for vehicles is normally expressed in miles-per-gallon (MPG). In Canada, fuel efficiency is normally expressed in liters-per-hundred
# kilometers (L/100 km). Use your research skills to determine how to convert from
# MPG to L/100 km. Then create a program that reads a value from the user in American
# units and displays the equivalent fuel efficiency in Canadian units

liter_per_km = 235.21
MGP_input = int(input("Enter your MGP amount : "))
L100_km = liter_per_km / MGP_input
print(L100_km)

'''


# Exercise 12: Distance Between Two Points on Earth
#
# The surface of the Earth is curved, and the distance between degrees of longitude
# varies with latitude. As a result, finding the distance between two points on the surface
# of the Earth is more complicated than simply using the Pythagorean theorem.
# Let (t1, g1) and (t2, g2) be the latitude and longitude of two points on the Earth’s
# surface. The distance between these points, following the surface of the Earth, in
# kilometers is:
# distance = 6371.01 × arccos(sin(t1) × sin(t2) + cos(t1) × cos(t2) × cos(g1 − g2))
# The value 6371.01 in the previous equation wasn’t selected at random. It is
# the average radius of the Earth in kilometers.
# Create a program that allows the user to enter the latitude and longitude of two
# points on the Earth in degrees. Your program should display the distance between
# the points, following the surface of the earth, in kilometers.
# Exercise 12: Distance Between Two Points on Earth 7
# Hint: Python’s trigonometric functions operate in radians. As a result, you will
# need to convert the user’s input from degrees to radians before computing the
# distance with the formula discussed previously. The math module contains a
# function named radians which converts from degrees to radians.




'''
# Exercise 13: Making Change
#
# Consider the software that runs on a self-checkout machine. One task that it must be
# able to perform is to determine how much change to provide when the shopper pays
# for a purchase with cash.
# Write a program that begins by reading a number of cents from the user as an
# integer. Then your program should compute and display the denominations of the
# coins that should be used to give that amount of change to the shopper. The change
# should be given using as few coins as possible. Assume that the machine is loaded
# with pennies, nickels, dimes, quarters, loonies and toonies.
# A one dollar coin was introduced in Canada in 1987. It is referred to as a
# loonie because one side of the coin has a loon (a type of bird) on it. The two
# dollar coin, referred to as a toonie, was introduced 9 years later. It’s name is
# derived from the combination of the number two and the name of the loonie


cents_per_toonie = 200
cents_per_loonie = 100
cents_per_quarter = 25
cents_per_dime = 10
cents_per_nickel = 5

cents = int(input("Enter the number of cents : "))

print(cents // cents_per_toonie , "toonies")
cents = cents % cents_per_toonie

print(cents // cents_per_loonie , "loonies")
cents = cents % cents_per_loonie

print(cents // cents_per_quarter , "quarter")
cents = cents % cents_per_quarter

print(cents // cents_per_dime , "dimes")
cents = cents % cents_per_dime

print(cents // cents_per_nickel , "nickel")
cents = cents % cents_per_nickel

print(" ", cents, "pennies")


'''

'''
# Exercise 14: Height Units
#
# Many people think about their height in feet and inches, even in some countries that
# primarily use the metric system. Write a program that reads a number of feet from
# the user, followed by a number of inches. Once these values are read, your program
# should compute and display the equivalent number of centimeters.
# Hint: One foot is 12 inches. One inch is 2.54 centimeters

one_foot = 12
one_inch = 2.54

feet = int(input("Enter the number of feet : "))
inches = int(input("Enter the number of inches : "))

cm = (feet * one_foot + inches) * one_inch
print(f"Your height in CM is : {cm}cm")

'''



'''
# Exercise 15: Distance Units
#
# In this exercise, you will create a program that begins by reading a measurement
# in feet from the user. Then your program should display the equivalent distance in
# inches, yards and miles. Use the Internet to look up the necessary conversion factors
# if you don't have them memorized

input_feet = int(input("Enter the number of feet : "))

inches = 12 / input_feet
yards = input_feet / 3
miles = input_feet / 5280

print(f"{input_feet} feet is {inches:.2f} inches")
print(f"{input_feet} feet is {yards:.2f} yards")
print(f"{input_feet} feet is {miles:.2f} miles")

'''

# Exercise 16: Area and Volume
#
# Write a program that begins by reading a radius, r, from the user. The program will
# continue by computing and displaying the area of a circle with radius r and the
# volume of a sphere with radius r. Use the pi constant in the math module in your
# calculations.
# Hint: The area of a circle is computed using the formula area = πr 2. The
# volume of a sphere is computed using the formula volume = 4
# 3πr 3





#
# Exercise 17: Heat Capacity
#
# The amount of energy required to increase the temperature of one gram of a material
# by one degree Celsius is the material’s specific heat capacity, C. The total amount
# of energy required to raise m grams of a material by ΔT degrees Celsius can be
# computed using the formula:
# q = mCΔT.
# Write a program that reads the mass of some water and the temperature change
# from the user. Your program should display the total amount of energy that must be
# added or removed to achieve the desired temperature change.
# Hint: The specific heat capacity of water is 4.186 J
# g◦C. Because water has a density of 1.0 gram per millilitre, you can use grams and millilitres interchangeably
# in this exercise.
# Extend your program so that it also computes the cost of heating the water. Electricity is normally billed using units of kilowatt hours rather than Joules. In this
# exercise, you should assume that electricity costs 8.9 cents per kilowatt-hour. Use
# your program to compute the cost of boiling water for a cup of coffee.
# Hint: You will need to look up the factor for converting between Joules and
# kilowatt hours to complete the last part of this exercise





'''
# Exercise 18:Volume of a Cylinder
#
# The volume of a cylinder can be computed by multiplying the area of its circular
# base by its height. Write a program that reads the radius of the cylinder, along with
# its height, from the user and computes its volume. Display the result rounded to one
# decimal place.

# circular_area = 3.14
# height = 5

input_circular_area = int(input("Enter the number of circular area : "))
input_height = int(input("Enter the number of height : "))

input_circular_area = input_circular_area * input_circular_area
print(f"Area of the circular area is {input_circular_area:.1f}")

volume = input_circular_area * input_height
print(f"Volume of the cylinder is {volume:.1f}")

'''



# Exercise 19: Free Fall
# Create a program that determines how quickly an object is traveling when it hits the
# ground. The user will enter the height from which the object is dropped in meters (m).
# Because the object is dropped its initial speed is 0 m/s. Assume that the acceleration
# due to gravity is 9.8 m/s2. You can use the formula vf =
# v2
# i + 2ad to compute the
# final speed, vf , when the initial speed, vi , acceleration, a, and distance, d, are known.





#
# Exercise 20: Ideal Gas Law
#
# The ideal gas law is a mathematical approximation of the behavior of gasses as
# pressure, volume and temperature change. It is usually stated as:
# PV = nRT
# where P is the pressure in Pascals, V is the volume in liters, n is the amount of
# substance in moles, R is the ideal gas constant, equal to 8.314 J
# mol K , and T is the
# temperature in degrees Kelvin.
# Write a program that computes the amount of gas in moles when the user supplies
# the pressure, volume and temperature. Test your program by determining the number
# of moles of gas in a SCUBA tank. A typical SCUBA tank holds 12 liters of gas at
# a pressure of 20,000,000 Pascals (approximately 3,000 PSI). Room temperature is
# approximately 20 degrees Celsius or 68 degrees Fahrenheit
# Hint: A temperature is converted from Celsius to Kelvin by adding 273.15
# to it. To convert a temperature from Fahrenheit to Kelvin, deduct 32 from it,
# multiply it by 5
# 9 and then add 273.15 to it.


'''
# Exercise 21: Area of a Triangle
#
# The area of a triangle can be computed using the following formula, where b is the
# length of the base of the triangle, and h is its height:
# area = b * h / 2
# Write a program that allows the user to enter values for b and h. The program
# should then compute and display the area of a triangle with base length b and height h.

base_length = int(input("Enter the length of base ? "))
height = int(input("Enter the height ? "))

area = (base_length * height) / 2

print(f"The base lenght is {base_length} \n The height is {height} \n The area of the triangle is {area}")


'''

'''
# Exercise 22: Area of a Triangle (Again)
#
# In the previous exercise you created a program that computed the area of a triangle
# when the length of its base and its height were known. It is also possible to compute
# the area of a triangle when the lengths of all three sides are known. Let s1, s2 and s3
# be the lengths of the sides. Let s = (s1 + s2 + s3)/2. Then the area of the triangle
# can be calculated using the following formula: area = s × (s − s1) × (s − s2) × (s − s3)
# Develop a program that reads the lengths of the sides of a triangle from the user and displays its area
import math
s1 = int(input("Enter the length of base : "))
s2 = int(input("Enter the left side lenght : "))
s3 = int(input("Enter the right side lenght "))

s = (s1 + s2 + s3) / 2

area = math.sqrt( s * ( s - s1 ) * ( s - s2 ) * ( s - s3 ) )

print(f"The area of the triangle is {area}")

'''

# Exercise 23: Area of a Regular Polygon
#
# A polygon is regular if its sides are all the same length and the angles between all of
# the adjacent sides are equal. The area of a regular polygon can be computed using
# the following formula, where s is the length of a side and n is the number of sides
# area = n * s2 / 4 * tan (π/π)
# Write a program that reads s and n from the user and then displays the area of a
# regular polygon constructed from these values.



'''
# Exercise 24: Units of Time
#
# Create a program that reads a duration from the user as a number of days, hours,
# minutes, and seconds. Compute and display the total number of seconds represented
# by this duration.

days = int(input("Input number of days : "))
hours = int(input("Input number of hours : "))
minutes = int(input("Input number of mintues : "))
seconds = int(input("Input number of seconds : "))

seconds_per_day = 86400
seconds_per_hour = 3600
seconds_per_min = 60

total = days * seconds_per_day + hours * seconds_per_hour + minutes * seconds_per_min + seconds

print(f"The total number of seconds represented by this duration is {total}")

'''

'''
# Exercise 25: Units of Time (Again)
#
# In this exercise you will reverse the process described in the previous exercise.
# Develop a program that begins by reading a number of seconds from the user.
# Then your program should display the equivalent amount of time in the form
# D:HH:MM:SS, where D, HH, MM, and SS represent days, hours, minutes and seconds respectively. The hours, minutes and seconds should all be formatted so that they occupy exactly two digits, with a leading 0 displayed if necessary.

total_seconds = int(input("Enter the number of seconds: "))

days = total_seconds / 86400
total_seconds = total_seconds % 86400

hours = total_seconds / 3600
total_seconds = total_seconds % 3600

minutes = total_seconds / 60
total_seconds = total_seconds % 60


formatted_time = f"{days} : {hours:.1f} : {minutes:.1f} : {total_seconds:.1f}"

print("Equivalent time:", formatted_time)

'''



'''
# Exercise 26: Current Time
#
# Python includes a library of functions for working with time, including a function
# called asctime in the time module. It reads the current time from the computer’s internal clock and returns it in a human-readable format. Write a program that displays the current time and date. Your program will not require any input from the user

import time
current_time = time.asctime(time.localtime(time.time()))
print(current_time)

'''


'''
# Exercise 27: Body Mass Index
#
# Write a program that computes the body mass index (BMI) of an individual. Your program should begin by reading a height and weight from the user. Then it should use one of the following two formulas to compute the BMI before displaying it. If you read the height in inches and the weight in pounds then body mass index is computed using the following formula:
# BMI = weight / height * height * 703.
# If you read the height in meters and the weight in kilograms then body mass index is computed using this slightly simpler formula: BMI = weight / height * height

height = int(input("What is your height in meters ? "))
weight = int(input("What is your weight in kilogram ? "))
BMI = weight / (height * height)
print(f"Your BMI is {BMI}")

'''



'''
# Exercise 28:Wind Chill
#
# When the wind blows in cold weather, the air feels even colder than it actually is because the movement of the air increases the rate of cooling for warm objects, like people. This effect is known as wind chill.
# In 2001, Canada, the United Kingdom and the United States adopted the following formula for computing the wind chill index. Within the formula Ta is the
# air temperature in degrees Celsius and V is the wind speed in kilometers per hour.
# A similar formula with different constant values can be used with temperatures in
# degrees Fahrenheit and wind speeds in miles per hour.
# WCI = 13.12 + 0.6215Ta − 11.37V0.16 + 0.3965TaV0.16
# Write a program that begins by reading the air temperature and wind speed from the user. Once these values have been read your program should display the wind chill index rounded to the closest integer.
# The wind chill index is only considered valid for temperatures less than or equal to 10 degrees Celsius and wind speeds exceeding 4.8 kilometers per hour

Ta = int(input("Enter the air temperature in degrees Celsius : "))
V = int(input("Enter the wind speed in kilometers : "))

WCI = 13.12 + 0.6215 * (Ta) - 11.37(V)**0.16 + 0.3965*(Ta)*(V)**0.16

# UNABLE TO SOLVE THIS !!

'''


'''
# Exercise 29: Celsius to Fahrenheit and Kelvin
# Write a program that begins by reading a temperature from the user in degrees
# Celsius. Then your program should display the equivalent temperature in degrees
# Fahrenheit and degrees Kelvin. The calculations needed to convert between different
# units of temperature can be found on the internet

temperature = int(input("Enter the temperature degree celsius : "))
calcFahrenheit = (temperature * 2) + 30
calcKelvin = temperature + 273.15
print(f"Celcius is {temperature}°C ,converted to Fahrenheit is {calcFahrenheit}°F, converted to kelvin is {calcKelvin}K")

'''

# Exercise 30: Units of Pressure
#
# In this exercise you will create a program that reads a pressure from the user in kilopascals. Once the pressure has been read your program should report the equivalent pressure in pounds per square inch, millimeters of mercury and atmospheres. Use your research skills to determine the conversion factors between these units.



'''
# Exercise 31: Sum of the Digits in an Integer
# Develop a program that reads a four-digit integer from the user and displays the sum
# of the digits in the number. For example, if the user enters 3141 then your program
# should display 3+1+4+1=9.

numbers = input("Enter a four-digit integer : ")
firstNum = numbers[0]
secondNum = numbers[1]
thirdNum = numbers[2]
fourthNum = numbers[3]

total = int(firstNum) + int(secondNum) + int(thirdNum) + int(fourthNum)

print(f"{firstNum} + {secondNum} + {thirdNum} + {fourthNum} = {total} ")

'''


'''
# Exercise 32: Sort 3 Integers
#
# Create a program that reads three integers from the user and displays them in sorted
# order (from smallest to largest). Use the min and max functions to find the smallest
# and largest values. The middle value can be found by computing the sum of all three
# values, and then subtracting the minimum value and the maximum value.


numbers = input("Enter a three-digit integer : ")
min_num = min(numbers)
max_num = max(numbers)
firstNum = numbers[0]
secondNum = numbers[1]
thirdNum = numbers[2]
middle_num = int(firstNum) + int(secondNum) + int(thirdNum) - int(min_num) - int(max_num)
print(f"The largest value is {max_num} \n The smallest value is {min_num} \n The middle value is {middle_num}")

'''




'''
# Exercise 33: Day Old Bread
#
# A bakery sells loaves of bread for $3.49 each. Day old bread is discounted by 60
# percent. Write a program that begins by reading the number of loaves of day old
# bread being purchased from the user. Then your program should display the regular
# price for the bread, the discount because it is a day old, and the total price. All of the
# values should be displayed using two decimal places, and the decimal points in all
# of the numbers should be aligned when reasonable values are entered by the user.

bread_price =  3.49
discounted_price = 3.49 * 0.60

bread_purchased = float(input("How many of loaves of day old bread was purchased ?  "))
total = bread_purchased * discounted_price
print(f"Regular price : ${bread_price} \nDiscount price : ${discounted_price:.1f} \nTotal price : ${total:.1f}")

'''


# IF STATEMENT EXERCISES



'''
# Exercise 34: Even or Odd?
#
# Write a program that reads an integer from the user. Then your program should
# display a message indicating whether the integer is even or odd.

number = int(input("Enter a number : "))
if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

'''

'''

# Exercise 35: Dog Years
#
# It is commonly said that one human year is equivalent to 7 dog years. However this
# simple conversion fails to recognize that dogs reach adulthood in approximately two
# years. As a result, some people believe that it is better to count each of the first two
# human years as 10.5 dog years, and then count each additional human year as 4 dog years.
# Write a program that implements the conversion from human years to dog years
# described in the previous paragraph. Ensure that your program works correctly for
# conversions of less than two human years and for conversions of two or more human
# years. Your program should display an appropriate error message if the user enters a negative number.

human_years = 5

if human_years < 0:
    print("Error: Please enter a non-negative number")
elif human_years <= 2:
    dog_years = human_years * 10.5
    print(dog_years)
else:
    dog_years = 21 + (human_years - 2) * 4
    print(dog_years)
'''


# UNABLE TO SOLVE

''''


# Exercise 36:Vowel or Consonant
#
# In this exercise you will create a program that reads a letter of the alphabet from the
# user. If the user enters a, e, i, o or u then your program should display a message
# indicating that the entered letter is a vowel. If the user enters y then your program
# should display a message indicating that sometimes y is a vowel, and sometimes y is
# a consonant. Otherwise your program should display a message indicating that the letter is a consonant.


inputed_letter = input("Enter a letter : ")
if inputed_letter == "a" or inputed_letter == "e" or inputed_letter == "i" or inputed_letter == "o" or inputed_letter == "u":
  print(f"{inputed_letter} is a Vowel")
elif inputed_letter == 'y':
  print(f"sometimes {inputed_letter} is a vowel, and sometimes {inputed_letter} is a consonant")
else:
  print(f"{inputed_letter} is a consonant")

'''

'''
# Exercise 37: Name that Shape

# Write a program that determines the name of a shape from its number of sides. Read
# the number of sides from the user and then report the appropriate name as part of
# a meaningful message. Your program should support shapes with anywhere from 3 up to (and including) 10 sides.
# If a number of sides outside of this range is entered
# then your program should display an appropriate error message.

inputed_sides = int(input("Enter the number of sides : "))

if inputed_sides == 3:
  print("This is a Triangle")
elif inputed_sides == 4:
  print("This is a Quadrilateral")
elif inputed_sides == 5:
  print("This is a Pentagon")
elif inputed_sides == 6:
  print("This is a Hexagon")
elif inputed_sides == 7:
  print("This is a Octagon")
elif inputed_sides == 8:
  print("This is a Octagon")
elif inputed_sides == 9:
  print("This is a Nonagon")
elif inputed_sides == 9:
  print("This is a Decagon")
else:
  print("Please enter a side within the range of 3 - 10")


'''


'''
# Exercise 38: Month Name to Number of Days
#
# The length of a month varies from 28 to 31 days. In this exercise you will create
# a program that reads the name of a month from the user as a string. Then your
# program should display the number of days in that month. Display “28 or 29 days”
# for February so that leap years are addressed

name_of_month = (input("Enter the name of a month : ")).lower()

if name_of_month == 'september' or name_of_month == 'april' or name_of_month == 'june' or name_of_month == 'november':
  print(f"{name_of_month} has 30 days")
elif name_of_month == 'february':
  print(f"{name_of_month} has 28 - 29 days")
else:
  print(f"{name_of_month} has 31 days ")

'''

'''
# Exercise 39: Sound Levels
#
# The following table lists the sound level in decibels for several common noises.

# Noise               Decibel level (dB)
# Jackhammer          130
# Gas lawnmower       106
# Alarm clock         70
# Quiet room          40

# Write a program that reads a sound level in decibels from the user. If the user
# enters a decibel level that matches one of the noises in the table then your program
# should display a message containing only that noise. If the user enters a number
# of decibels between the noises listed then your program should display a message
# indicating which noises the level is between. Ensure that your program also generates
# reasonable output for a value smaller than the quietest noise in the table, and for a
# value larger than the loudest noise in the table

decibel_level = int(input("Enter a decibel level : "))

if decibel_level == 130:
  print("Jackhammer")
elif decibel_level > 106 and decibel_level < 130:
 print("Your noise level is between Jackhammer and Gas lawnmower ")
elif decibel_level == 106:
  print("Gas lawnmower")
elif decibel_level > 70 and decibel_level < 106:
 print("Your noise level is between Gas lawnmower and Alarm clock ")
elif decibel_level == 70:
  print("Alarm clock")
elif decibel_level > 40 and decibel_level < 70:
  print("Your noise level is between Alarm clock and Quiet room ")
elif decibel_level == 40:
  print("Quiet room")
elif decibel_level < 40:
  print("Your noise level is less than Quiet room")
elif decibel_level > 130:
  print("Your noise level is greater than Jackhammer")

  '''


'''
# Exercise 40: Name that Triangle
#
# A triangle can be classified based on the lengths of its sides as equilateral, isosceles
# or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles
# triangle has two sides that are the same length, and a third side that is a different
# length. If all of the sides have different lengths then the triangle is scalene.
# Write a program that reads the lengths of 3 sides of a triangle from the user.
# Display a message indicating the type of the triangle.

first_side = int(input("Enter the length of first side : "))
second_side = int(input("Enter the length of second side : "))
third_side = int(input("Enter the length of third side : "))

if first_side == second_side and first_side == third_side:
  print("This is an equilateral triangle")
elif first_side == second_side or first_side == third_side or second_side == third_side:
  print("This is an isosceles triangle")
else:
  print("This is a scalene triangle")

  '''




'''
# Exercise 41: Note To Frequency
#
# The following table lists an octave of music notes, beginning with middle C, along with their frequencies.

# Note      Frequency (Hz)
# C4        261.63
# D4        293.66
# E4        329.63
# F4        349.23
# G4        392.00
# A4        440.00
# B4        493.88
#
#
# Begin by writing a program that reads the name of a note from the user and
# displays the note’s frequency. Your program should support all of the notes listed previously.
# Once you have your program working correctly for the notes listed previously you
# should add support for all of the notes from C0 to C8. While this could be done by
# adding many additional cases to your if statement, such a solution is cumbersome,
# inelegant and unacceptable for the purposes of this exercise. Instead, you should
# exploit the relationship between notes in adjacent octaves. In particular, the frequency
# of any note in octave n is half the frequency of the corresponding note in octave n+1.
# By using this relationship, you should be able to add support for the additional notes
# without adding additional cases to your if statement.
# Hint: To complete this exercise you will need to extract individual characters
# from the two-character note name so that you can work with the letter and
# the octave number separately. Once you have separated the parts, compute the
# frequency of the note in the fourth octave using the data in the table above.
# Then divide the frequency by 24−x , where x is the octave number entered by
# the user. This will halve or double the frequency the correct number of times

name_of_note = input("Enter the name of the note : ")
if name_of_note == "C4":
  print("Your note is 261.63")
elif name_of_note == "D4":
  print("Your note is 293.66")
elif name_of_note == "E4":
  print("Your note is 329.63")
elif name_of_note == "F4":
  print("Your note is 349.23")
elif name_of_note == "G4":
  print("Your note is 392.00")
elif name_of_note == "A4":
  print("Your note is 440.00")
elif name_of_note == "B4":
  print("Your note is 493.88")

c0 = 261.63
c1 = 261.63/2
c2 = 261.63/4
c3 = 261.63/8
c4 = 261.63/16
c5 = 261.63/32
c6 = 261.63/64
c7 = 261.63/128
c8 = 261.63/256


UNABLE TO SOLVE

'''


# Exercise 42: Frequency To Note
#
# In the previous question you converted from note name to frequency. In this question
# you will write a program that reverses that process. Begin by reading a frequency
# from the user. If the frequency is within one Hertz of a value listed in the table in
# the previous question then report the name of the note. Otherwise report that the
# frequency does not correspond to a known note. In this exercise you only need to
# consider the notes listed in the table. There is no need to consider notes from other
# octaves.





'''

#
# Exercise 43: Faces on Money
#
# It is common for images of a country’s previous leaders, or other individuals of historical significance, to appear on its money. The individuals that appear on banknotes
# in the United States are listed in Table 2.1.
# Write a program that begins by reading the denomination of a banknote from the
# user. Then your program should display the name of the individual that appears on the
#
#
# Table 2.1 Individuals that
# appear on Banknotes
# Individual          Amount
# George Washington     $1
# Thomas Jefferson      $2
# Abraham Lincoln       $5
# Alexander Hamilton    $10
# Andrew Jackson        $20
# Ulysses S. Grant      $50
# Benjamin Franklin     $100
#
#
# banknote of the entered amount. An appropriate error message should be displayed
# if no such note exists.
# While two dollar banknotes are rarely seen in circulation in the United States
# they are legal tender that can be spent just like any other denomination. The
# United States has also issued banknotes in denominations of $500, $1,000,
# $5,000, and $10,000 for public use. However, high denomination banknotes
# have not been printed since 1945 and were officially discontinued in 1969. As
# a result, we will not consider them in this exercise.

enter_denomination = int(input("Enter the denomination :$ "))
if enter_denomination == 1:
  print("George Washington")
elif enter_denomination == 2:
  print("Thomas Jefferson")
elif enter_denomination == 5:
  print("Abraham Lincoln")
elif enter_denomination == 10:
  print("Alexander Hamilton")
elif enter_denomination == 20:
  print("Andrew Jackson")
elif enter_denomination == 50:
  print("Ulysses S. Grant")
elif enter_denomination == 100:
  print("Benjamin Franklin")
else:
    print("No such banknote exists")



'''


'''
# Exercise 44: Date to Holiday Name

# Canada has three national holidays which fall on the same dates each year.

# Holiday             Date
# New year’s day      January 1
# Canada day          July 1
# Christmas day       December 25

# Write a program that reads a month and day from the user. If the month and day
# match one of the holidays listed previously then your program should display the
# holiday’s name. Otherwise your program should indicate that the entered month and
# day do not correspond to a fixed-date holiday.
# Canada has two additional national holidays, Good Friday and Labour Day,
# whose dates vary from year to year. There are also numerous provincial and
# territorial holidays, some of which have fixed dates, and some of which have
# variable dates. We will not consider any of these additional holidays in this
# exercise.

month = (input("Enter the month : ")).lower()
day = (input("Enter the day : "))

date = month + day

if date == "january1":
 print("New Year's Day")
elif date == "july1":
 print("Canada Day")
elif date == "december25":
 print("Christmas Day")
else:
 print("Entered month and day do not correspond to a fixed-date holiday.")


'''



'''

# Exercise 45: What Color is that Square?
#
# Positions on a chess board are identified by a letter and a number. The letter    identifies the column, while the number identifies the row, as shown below:
#
# img.md
#
# Write a program that reads a position from the user. Use an if statement to determine if the column begins with a black square or a white square. Then use modular
# arithmetic to report the color of the square in that row. For example, if the user enters a1 then your program should report that the square is black. If the user enters d5
# then your program should report that the square is white. Your program may assume that a valid position will always be entered. It does not need to perform any error checking.

# BELLOW IS THE ANSWER AI GAVE ME

# position = input("Enter the position on the chess board (e.g. a1, d5): ")

column = position[0]
row = int(position[1])

columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

column_index = columns.index(column)

if (column_index + row) % 2 == 0:
 print(f"The square at position {position} is white")
else:
 print(f"The square at position {position} is black")


#  MY SOLUTION AFTER I STUDIED HOW TO CHECK FOR THE WHITE AND BLACK BOX IN THE CHESS BOARD
#  all even numbers are in white squares, all odd numbers are in black squares


columns = input("Enter the alphabetical column of the position on the chess board : ")
rows = int(input("Enter the numberic row of the position on the chess board: "))

if rows % 2 == 0:
  print("The square is white")
else:
  print("The square is black")



'''





'''

# Exercise 46: Season from Month and Day

# The year is divided into four seasons: spring, summer, fall and winter. While the
# exact dates that the seasons change vary a little bit from year to year because of the
# way that the calendar is constructed, we will use the following dates for this exercise:

# Season      First day
# Spring      March 20
# Summer      June 21
# Fall        September 22
# Winter      December 21

# Create a program that reads a month and day from the user. The user will enter
# the name of the month as a string, followed by the day within the month as an
# integer. Then your program should display the season associated with the date that was entered

month = (input("Enter the month : ")).lower()
day = int(input("Enter the day : "))

date = month + str(day)

if date == "march20":
 print("Spring")
elif date == "june21":
 print("Summer")
elif date == "september22":
 print("Fall")
elif date == "december21":
 print("Winter")
else:
 print("Please enter a month within the range of March - December")


'''

'''
# Exercise 47: Birth Date to Astrological Sign
#
# The horoscopes commonly reported in newspapers use the position of the sun at the
# time of one's birth to try and predict the future. This system of astrology divides the
# year into twelve zodiac signs, as outline in the table below:

# Zodiac sign           Date range
# Capricorn             December 22 to January 19
# Aquarius              January 20 to February 18
# Pisces                February 19 to March 20
# Aries                 March 21 to April 19
# Taurus                April 20 to May 20
# Gemini                May 21 to June 20
# Cancer                June 21 to July 22
# Leo                   July 23 to August 22
# Virgo                 August 23 to September 22
# Libra                 September 23 to October 22
# Scorpio               October 23 to November 21
# Sagittarius           November 22 to December 21

# Write a program that asks the user to enter his or her month and day of birth. Then
# your program should report the user’s zodiac sign as part of an appropriate output message.

month = input("Enter your birth month : ").lower()
day = int(input("Enter your birth day : "))

if (month == 'december' and day >= 22) or (month == 'january' and day <= 19):
  print("Capricorn")
elif (month == 'january' and day >= 20) or (month == 'february' and day <= 18):
  print("Aquarius")
elif (month == 'february' and day >= 19) or (month == 'march' and day <= 20):
  print("Pisces")
elif (month == 'march' and day >= 21) or (month == 'april' and day <= 19):
  print("Aries")
elif (month == 'april' and day >= 20) or (month == 'may' and day <= 20):
  print("Taurus")
elif (month == 'may' and day >= 21) or (month == 'june' and day <= 20):
  print("Gemini")
elif (month == 'june' and day >= 21) or (month == 'july' and day <= 22):
  print("Cancer")
elif (month == 'july' and day >= 23) or (month == 'august' and day <= 22):
  print("Leo")
elif (month == 'august' and day >= 23) or (month == 'september' and day <= 22):
  print("Virgo")
elif (month == 'september' and day >= 23) or (month == 'october' and day <= 22):
  print("Libra")
elif (month == 'october' and day >= 23) or (month == 'november' and day <= 21):
  print("Scorpio")
elif (month == 'november' and day >= 22) or (month == 'december' and day <= 21):
  print("Sagittarius")
else:
  print("Please enter a month within the range of January - December")


'''






# Exercise 48: Chinese Zodiac
#
# The Chinese zodiac assigns animals to years in a 12 year cycle. One 12 year cycle is
# shown in the table below. The pattern repeats from there, with 2012 being another
# year of the dragon, and 1999 being another year of the hare.
#
# Year                Animal
# 2000                Dragon
# 2001                Snake
# 2002                Horse
# 2003                Sheep
# 2004                Monkey
# 2005                Rooster
# 2006                Dog
# 2007                Pig
# 2008                Rat
# 2009                Ox
# 2010                Tiger
# 2011                Hare
#
# Write a program that reads a year from the user and displays the animal associated
# with that year. Your program should work correctly for any year greater than or equal
# to zero, not just the ones listed in the table




'''

# Exercise 49: Richter Scale
#
# The following table contains earthquake magnitude ranges on the Richter scale and
# their descriptors:
#
# Magnitude                 Descriptor
# Less than 2.0             Micro
# 2.0 to less than 3.0      Very minor
# 3.0 to less than 4.0      Minor
# 4.0 to less than 5.0      Light
# 5.0 to less than 6.0      Moderate
# 6.0 to less than 7.0      Strong
# 7.0 to less than 8.0      Major
# 8.0 to less than 10.0     Great
# 10.0 or more              Meteoric
#
# Write a program that reads a magnitude from the user and displays the appropriate
# descriptor as part of a meaningful message. For example, if the user enters 5.5 then
# your program should indicate that a magnitude 5.5 earthquake is considered to be a
# moderate earthquake

magnitude = float(input("Enter the magnitude : "))

if magnitude < 2.0 :
  print('Micro earthquake')
elif magnitude >= 2.0 and magnitude < 3.0:
  print('Very minor earthquake ')
elif magnitude >= 3.0 and magnitude < 4.0:
  print('Minor earthquake ')
elif magnitude >= 4.0 and magnitude < 5.0:
  print('Light earthquake ')
elif magnitude >= 5.0 and magnitude < 6.0:
  print('Moderate earthquake ')
elif magnitude >= 6.0 and magnitude < 7.0:
  print('Strong earthquake ')
elif magnitude >= 7.0 and magnitude < 8.0:
  print('Major earthquake ')
elif magnitude >= 8.0 and magnitude < 10.0:
  print('Great earthquake ')
elif magnitude >= 10.0:
  print('Meteoric earthquake ')
else:
 print("Please enter a magnitude within the range of 2.0 - 10.0")


'''



# Exercise 50: Roots of a Quadratic Function
#
# A univariate quadratic function has the form f (x) = ax2 + bx + c, where a, b and
# c are constants, and a is non-zero. The roots of a quadratic function can be found
# by finding the values of x that satisfy the quadratic equation ax2 + bx + c = 0. A
# quadratic function may have 0, 1 or 2 real roots. These roots can be computed using
# the quadratic formula, shown below:
# root = −b ± √b2 − 4ac / 2a
# The portion of the expression under the square root sign is called the discriminant.
# If the discriminant is negative then the quadratic equation does not have any real roots.
# If the discriminant is 0, then the equation has one real root. Otherwise the equation
# has two real roots, and the expression must be evaluated twice, once using a plus
# sign, and once using a minus sign, when computing the numerator.
# Write a program that computes the real roots of a quadratic function. Your program
# should begin by prompting the user for the values of a, b and c. Then it should display
# a message indicating the number of real roots, along with the values of the real roots (if any)





'''
# Exercise 51: Letter Grade to Grade Points
#
# At a particular university, letter grades are mapped to grade points in the following
# manner:
# Letter        Grade points
# A+            4.0
# A             4.0
# A−            3.7
# B+            3.3
# B             3.0
# B−            2.7
# C+            2.3
# C             2.0
# C−            1.7
# D+            1.3
# D             1.0
# F             0
#
# Write a program that begins by reading a letter grade from the user. Then your
# program should compute and display the equivalent number of grade points. Ensure that your program generates an appropriate error message if the user enters an invalid letter grade.

letter_grade  = input("Enter the letter grade : ").capitalize()

if letter_grade == "A+":
  print("4.0")
elif letter_grade == "A":
  print("4.0")
elif letter_grade == "A-":
  print("3.7")
elif letter_grade == "B+":
  print("3.3")
elif letter_grade == "B":
  print("3.0")
elif letter_grade == "B-":
  print("2.7")
elif letter_grade == "C+":
  print("2.3")
elif letter_grade == "C":
  print("2.0")
elif letter_grade == "C-":
  print("1.7")
elif letter_grade == "D+":
  print("1.3")
elif letter_grade == "D":
  print("1.0")
elif letter_grade == "F":
  print("0")
else:
  print("Please enter a valid letter grade")

'''




'''
# Exercise 52: Grade Points to Letter Grade
#
# In the previous exercise you created a program that converts a letter grade into the
# equivalent number of grade points. In this exercise you will create a program that
# reverses the process and converts from a grade point value entered by the user to a
# letter grade. Ensure that your program handles grade point values that fall between
# letter grades. These should be rounded to the closest letter grade. Your program should report A+ for a 4.0 (or greater) grade point average.

grade = float(input('Enter your grade number: '))
if grade >= 4.0:
  print("A+")
elif grade >= 3.7 and grade < 4.0:
  print("A")
elif grade >= 3.3 and grade < 3.7:
  print("A-")
elif grade >= 3.0 and grade < 3.3:
  print("B+")
elif grade >= 2.7 and grade < 3.0:
  print("B")
elif grade >= 2.3 and grade < 2.7:
  print("B-")
elif grade >= 2.0 and grade < 2.3:
  print("C+")
elif grade >= 1.7 and grade < 2.0:
  print("C")
elif grade >= 1.3 and grade < 1.7:
  print("C-")
elif grade >= 1.0 and grade < 1.3:
  print("D+")
elif grade >= 0.7 and grade < 1.0:
  print("D")
elif grade >= 0.0 and grade < 0.7:
  print("F")
else:
  print("Please enter a valid grade number")

'''


'''
# Exercise 53: Assessing Employees
#
# At a particular company, employees are rated at the end of each year. The rating scale
# begins at 0.0, with higher values indicating better performance and resulting in larger raises. The value awarded to an employee is either 0.0, 0.4, or 0.6 or more. Values between 0.0 and 0.4, and between 0.4 and 0.6 are never used. The meaning associated with each rating is shown in the following table. The amount of an employee’s raise is $2400.00 multiplied by their rating.
#
# Rating            Meaning
# 0.0               Unacceptable performance
# 0.4               Acceptable performance
# 0.6 or more       Meritorious performance
#
# Write a program that reads a rating from the user and indicates whether the performance was unacceptable, acceptable or meritorious. The amount of the employee’s raise should also be reported. Your program should display an appropriate error message if an invalid rating is entered.
import math

emplo_raise = 2400.00

rating = float(input("Enter your rating : "))
if rating == 0.00:
  total = emplo_raise
  print(f"Your rating is an Unacceptable performance, your raise is ${total} ")
elif rating == 0.04:
  total =  emplo_raise * rating
  print(f"Your rating is an Acceptable performance, your raise is ${total} ")
elif rating >= 0.06:
  total = emplo_raise * rating
  print(f"Your rating is a Meritorious performance, your raise is ${total} ")
else:
  print("Please enter a valid rating")


'''


'''
# Exercise 54:Wavelengths of Visible Light
#
# The wavelength of visible light ranges from 380 to 750 nanometers (nm). While the
# spectrum is continuous, it is often divided into 6 colors as shown below:
#
# Color             Wavelength (nm)
# Violet            380 to less than 450
# Blue              450 to less than 495
# Green             495 to less than 570
# Yellow            570 to less than 590
# Orange            590 to less than 620
# Red               620 to 750
#
# Write a program that reads a wavelength from the user and reports its color. Display
# an appropriate error message if the wavelength entered by the user is outside of the
# visible spectrum


wavelenght = int(input("Enter the wavelength : "))

if wavelenght >= 380 and wavelenght < 450:
  print("Violet")
elif wavelenght >= 450 and wavelenght < 495:
  print("Blue")
elif wavelenght >= 495 and wavelenght < 570:
  print("Green")
elif wavelenght >= 570 and wavelenght < 590:
  print("Yellow")
elif wavelenght >= 590 and wavelenght < 620:
  print("Orange")
elif wavelenght >= 620 and wavelenght <= 750:
  print("Red")
else:
  print("Please enter a valid wavelength")

'''



'''
# Exercise 55: Frequency to Name
#
# Electromagnetic radiation can be classified into one of 7 categories according to its
# frequency, as shown in the table below:
# Name                  Frequency range (Hz)
# Radio waves           Less than 3 × 10⁹
# Microwaves            3 × 10⁹ to less than 3 × 10¹²
# Infrared light        3 × 10¹² to less than 4.3 × 10¹⁴
# Visible light         4.3 × 10¹⁴ to less than 7.5 × 10¹⁴
# Ultraviolet light     7.5 × 10¹⁴ to less than 3 × 10¹⁷
# X-rays                3 × 10¹⁷ to less than 3 × 10¹⁹
# Gamma rays            3 × 10¹⁹ or more

# Write a program that reads the frequency of the radiation from the user and displays
# the appropriate name.

radiation_frequency = int(input("Enter the radiation frequency : "))

if radiation_frequency < 3*10**9:
  print("Radio waves")
elif radiation_frequency >= 3*10**9 and radiation_frequency < 3*10**12:
  print("Microwaves")
elif radiation_frequency >= 3*10**12 and radiation_frequency < 4.3*10**14:
  print("Infrared light")
elif radiation_frequency >= 4.3*10**14 and radiation_frequency < 7.5*10**14:
  print("Visible light")
elif radiation_frequency >= 7.5*10**14 and radiation_frequency < 3*10**17:
  print("Ultraviolet light")
elif radiation_frequency >= 3*10**17 and radiation_frequency < 3*10**19:
  print("X-rays")
elif radiation_frequency >= 3*10**19:
  print("Gamma rays")
else:
  print("Please enter a valid radiation frequency")

'''



'''
# Exercise 56: Cell Phone Bill
#
# A particular cell phone plan includes 50 minutes of air time and 50 text messages
# for $15.00 a month. Each additional minute of air time costs $0.25, while additional
# text messages cost $0.15 each. All cell phone bills include an additional charge of
# $0.44 to support 911 call centers, and the entire bill (including the 911 charge) is
# subject to 5 percent sales tax.
# Write a program that reads the number of minutes and text messages used in a
# month from the user. Display the base charge, additional minutes charge (if any),
# additional text message charge (if any), the 911 fee, tax and total bill amount. Only
# display the additional minute and text message charges if the user incurred costs in
# these categories. Ensure that all of the charges are displayed using 2 decimal places.

cellphone_plan = 15.00
additonal_minutes = 0.25
addtional_text = 0.15
additional_charge = 0.44

minutes = int(input("Enter the number of minutes used : "))
text_messages = int(input("Enter the number of text messages used : "))
additional_minutes_input = int(input("How many additional minutes did you use? : "))
additional_text_messages = int(input("How many additional text messages did you use? : "))


if additional_minutes_input == True and additional_text_messages == True:
  total = (additional_minutes_input * additonal_minutes) + (additional_text_messages * addtional_text)
  tax = total * 0.05
  print("The total bill amount is : ", ((minutes + text_messages) * cellphone_plan) + total + tax + additional_charge)
else:
  print("The total bill amount is : ", ((minutes + text_messages) * cellphone_plan)+ additional_charge)



  MY SOLUTION HERE MIGHT NOT BE CORRECT, BECAUSE AM UNABLE TO WRAP MY HEAD AROUND THE PROBLEM
'''



'''
# Exercise 57: Is it a Leap Year?

# Most years have 365 days. However, the time required for the Earth to orbit the Sun
# is actually slightly more than that. As a result, an extra day, February 29, is included
# in some years to correct for this difference. Such years are referred to as leap years.
# The rules for determining whether or not a year is a leap year follow:
# • Any year that is divisible by 400 is a leap year.
# • Of the remaining years, any year that is divisible by 100 is not a leap year.
# • Of the remaining years, any year that is divisible by 4 is a leap year.
# • All other years are not leap years.
# Write a program that reads a year from the user and displays a message indicating whether or not it is a leap year

year = int(input("Enter a Year : "))

if year % 400 == 0 or year % 4 == 0:
  print(f"{year} is a leap year")
else:
  year % 100 == 0
  print(f"{year} is not a leap year ")


'''


''''
# Exercise 58: Next Day
#
# Write a program that reads a date from the user and computes its immediate successor.
# For example, if the user enters values that represent 2013-11-18 then your program
# should display a message indicating that the day immediately after 2013-11-18 is
# 2013-11-19. If the user enters values that represent 2013-11-30 then the program
# should indicate that the next day is 2013-12-01. If the user enters values that represent
# 2013-12-31 then the program should indicate that the next day is 2014-01-01. The
# date will be entered in numeric form with three separate input statements; one for
# the year, one for the month, and one for the day. Ensure that your program works correctly for leap years.

year = int(input("Enter the year: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))

if month in [1, 3, 5, 7, 8, 10, 12]:
    max_day = 31
elif month in [4, 6, 9, 11]:
    max_day = 30
else:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        max_day = 29
    else:
        max_day = 28

if day < max_day:
    next_year, next_month, next_day = year, month, day + 1
else:
    if month < 12:
        next_year, next_month, next_day = year, month + 1, 1
    else:
        next_year, next_month, next_day = year + 1, 1, 1

print(f"The day immediately after {year}-{month:02d}-{day:02d} is {next_year}-{next_month:02d}-{next_day:02d}")

'''


'''
# Exercise 59: Is a License Plate Valid?
#
# In a particular jurisdiction, older license plates consist of three uppercase letters
# followed by three numbers. When all of the license plates following that pattern had been used, the format was changed to four numbers followed by three uppercase letters.
# Write a program that begins by reading a string of characters from the user. Then
# your program should display a message indicating whether the characters are valid
# for an older style license plate or a newer style license plate. Your program should
# display an appropriate message if the string entered by the user is not valid for either
# style of license plate.

license_plate = input("Enter your license plate number : ")
if license_plate[0:3].isalpha() and license_plate[0:3].isupper() and license_plate[3:6].isdigit():
  print(f"{license_plate} is a valid old style license plate number")
elif license_plate[0:4].isdigit() and license_plate[4:7].isalpha() and license_plate[4:7].isupper():
  print(f"{license_plate} is a valid new style license plate number")
else:
  print(f"{license_plate} is not a valid license plate number")

'''


'''
# Exercise 60: Roulette Payouts
#
# A roulette wheel has 38 spaces on it. Of these spaces, 18 are black, 18 are red, and two
# are green. The green spaces are numbered 0 and 00. The red spaces are numbered 1,
# 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30 32, 34 and 36. The remaining integers
# between 1 and 36 are used to number the black spaces.
# Many different bets can be placed in roulette. We will only consider the following
# subset of them in this exercise:
# • Single number (1 to 36, 0, or 00)
# • Red versus Black
# • Odd versus Even (Note that 0 and 00 do not pay out for even)
# • 1 to 18 versus 19 to 36
# Write a program that simulates a spin of a roulette wheel by using Python’s random
# number generator. Display the number that was selected and all of the bets that must
# be payed. For example, if 13 is selected then your program should display:
# The spin resulted in 13...
# Pay 13
# Pay Black
# Pay Odd
# Pay 1 to 18
# If the simulation results in 0 or 00 then your program should display Pay 0 or
# Pay 00 without any further output
import random

red_spaces = [ 1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36 ]
black_spaces = [2,4,6,8,10,11,13,15,17,20,22,24,26,28,29,31,33,35]
green_spaces = [0, 00]
roulette =  [0,00, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36 ]

random_num = random.choice(roulette)

if random_num is red_spaces:
  print(f"The spin is {random_num}... \n Pay Red \n Pay Even \n Pay 2 to 35")
elif random_num is black_spaces:
  print(f"The spin is {random_num}... \n Pay Black \n Pay Odd \n Pay 1 to 18")
elif random_num is green_spaces:
  print(f"The spin is {random_num}... \n Pay 0 or Pay 00")
else:
  print(f"The spin is {random_num}... \n Pay {random_num}")


   WRONG ANSWER, UNABLE TO SOLVE
'''




# LOOP EXERCISES STATRS HERE



'''
# Exercise 61: Average
#
# In this exercise you will create a program that computes the average of a collection
# of values entered by the user. The user will enter 0 as a sentinel value to indicate
# that no further values will be provided. Your program should display an appropriate
# error message if the first value entered by the user is 0.
# Hint: Because the 0 marks the end of the input it should not be included in the
# average

average = []
number = int(input("Enter a number: "))
while number != 0:
  average.append(number)
  number = int(input("Enter a number: "))
print(f"The average is {sum(average) // (len(average))}")

'''





'''

# Exercise 62: Discount Table
#
# A particular retailer is having a 60 percent off sale on a variety of discontinued
# products. The retailer would like to help its customers determine the reduced price
# of the merchandise by having a printed discount table on the shelf that shows the
# original prices and the prices after the discount has been applied. Write a program that
# uses a loop to generate this table, showing the original price, the discount amount,
# and the new price for purchases of $4.95, $9.95, $14.95, $19.95 and $24.95. Ensure
# that the discount amounts and the new prices are rounded to 2 decimal places when
# they are displayed.


allPrices = [4.95, 9.95, 14.95, 19.95, 24.95]
discountPrice = 0.60

for price in allPrices:
  print(f"Original Price : {price:.2f} \t Discount : {price * discountPrice:.2f} \t New Price : {price - (price * discountPrice):.2f}")


'''


'''
# Exercise 63: Temperature Conversion Table
#
# Write a program that displays a temperature conversion table for degrees Celsius and
# degrees Fahrenheit. The table should include rows for all temperatures between 0
# and 100 degrees Celsius that are multiples of 10 degrees Celsius. Include appropriate
# headings on your columns. The formula for converting between degrees Celsius and
# degrees Fahrenheit can be found on the internet.

print("Degrees Celsius \t Degrees Fahrenheit")
for number in range(0,101, 10):
 print(f"{number}⁰C\t \t \t {(number * 9 / 5) + 32}f")

'''

# Exercise 64: No More Pennies
#
# February 4, 2013 was the last day that pennies were distributed by the Royal Canadian
# Mint. Now that pennies have been phased out retailers must adjust totals so that they
# are multiples of 5 cents when they are paid for with cash (credit card and debit card
# transactions continue to be charged to the penny). While retailers have some freedom
# in how they do this, most choose to round to the closest nickel.
# Write a program that reads prices from the user until a blank line is entered.
# Display the total cost of all the entered items on one line, followed by the amount
# due if the customer pays with cash on a second line. The amount due for a cash
# payment should be rounded to the nearest nickel. One way to compute the cash
# payment amount is to begin by determining how many pennies would be needed to
# pay the total. Then compute the remainder when this number of pennies is divided
# by 5. Finally, adjust the total down if the remainder is less than 2.5. Otherwise adjust
# the total up

