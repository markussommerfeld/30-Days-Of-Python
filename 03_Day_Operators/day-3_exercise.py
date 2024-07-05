# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 12:45:13 2024

@author: marku
"""

"""
    Declare your age as integer variable
    Declare your height as a float variable
    Declare a variable that store a complex number
    Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).

    Enter base: 20
    Enter height: 10
    The area of the triangle is 100

    Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).

Enter side a: 5
Enter side b: 4
Enter side c: 3
The perimeter of the triangle is 12

    Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
    Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
    Calculate the slope, x-intercept and y-intercept of y = 2x -2
    Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
    Compare the slopes in tasks 8 and 9.
    Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
    Find the length of 'python' and 'dragon' and make a falsy comparison statement.
    Use and operator to check if 'on' is found in both 'python' and 'dragon'
    I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
    There is no 'on' in both dragon and python
    Find the length of the text python and convert the value to float and convert it to string
    Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
    Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
    Check if type of '10' is equal to type of 10
    Check if int('9.8') is equal to 10
    Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?

Enter hours: 40
Enter rate per hour: 28
Your weekly earning is 1120

    Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years

Enter number of years you have lived: 100
You have lived for 3153600000 seconds.

    Write a Python script that displays the following table

1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125


"""

age = 37 # 1 done [year]
height = 1.78 #2 done [m]
complex_number  = 22 + 1j # 3 done

#%%
# 4 done
base, height = input("Enter: base and height of the triangle: ").split()
area = 0.5 * float(base)* float(height)
print("The area of the triangle is " + str(area))

#%%
# 5 done
side_a, side_b, side_c = input("Enter: the 3 lengths of the sides of the triangle: ").split()
perimeter = float(side_a) + float(side_b) + float(side_c)
print("The perimeter  of the triangle is " + str(perimeter))

#%%
# 6 done
length, width = input("Enter: the length and width of a rectangle: ").split()
area_rec = float(length) * float(width)
perimeter_rec = 2*(float(length) + float(width))
print("The area  of the rectangle  is " + str(area_rec))
print("The perimeter  of the rectangle  is " + str(perimeter_rec))

#%%
# 7 done
radius = input("Enter: the length and width of a rectangle: ")
pi =  3.14
area_circ = pi * float(radius)**2 
circ = 2 * pi * float(radius)
print("The area  of the circle  is " + str(area_circ))
print("The circumference  of the circle  is " + str(circ))

#%%
import numpy as np
import matplotlib.pyplot as plt
# 8 done
x = np.arange(0,7,1)
def y(x):
  return(2*x-2)
plt.plot(x,y(x))
plt.grid(True)
plt.ylim(-2,10)
plt.xlim(0,6)
slope = ((y(5))-(y(2)))/(5-2)
y_intercept = y(0)
x_intercept = (0+2)/2

# 9 done 
x_1 = 2
x_2 = 6
y_1 = 2
y_2 = 10
eucidian_dist = np.sqrt((x_2-x_1)**2+(y_2-y_1)**2)
slope_2 = (y_2-y_1)/(x_2-x_1)

# 10 done
print("slope 1: " + str(slope) + ", slope 2: " + str(slope_2))

# 11 done
x = np.arange(-5,5,0.1)
def y2(x):
    return(x**2 + 6*x + 9)
plt.plot(x,y2(x))
plt.grid(True)
plt.ylim(-1,20)
plt.xlim(-6,6) 
# x= 3, y=0

#%%
# 12 done
string_1 = 'python' 
string_2 = 'dragon' 
len(string_1) != len(string_2)

# 13 done
"on" in string_1 and "on" in string_2

# 14 done
"jargon" in "I hope this course is not full of jargon." 

# 16 done
str(float(len("python")))

# 17 done
num_in = 7
if num_in % 2 == 0:
    print("number is even")
else:
    print("number is uneven")
    
# 18 done
7//3 == int(2.7)

# 19 done
type('10') == type(10)

# 20 done
int(float('9.8')) == 10

#%%
# 21 done

hours, rate_per_hour = input("Enter the hours and rate per hour: ").split()
pay = float(hours) * float(rate_per_hour)
print("The weekly earning of the person is: " + str(pay*5))

#%%
# 22 done

years = input("Enter the number in years: ")
seconds = int(years) * 365*24*60*60
print("You have lived: " + str(seconds) + " seconds.")

#%%
# 22 done

matrix = [[1, 1, 1, 1, 1],
          [2, 1, 2, 4, 8],
          [3, 1, 3, 9, 27],
          [4, 1, 4, 16, 64],
          [5, 1, 5, 25, 125]]

print(matrix)
