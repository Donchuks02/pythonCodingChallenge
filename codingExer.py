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