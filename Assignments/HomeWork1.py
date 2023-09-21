#Factorial Function using Recursion
def factorial(num):
    if(num <0):
        return 'Factorial no defined for negative numbers'
    if (num ==0 or num ==1):
        return 1
    else :
        return num *factorial(num-1)
print(factorial(0))
print(factorial(10))


#Making BLT sandwiches
import math
def make_blt(b,l,t):
    return math.floor(min(b/8,l/3,t/4))  
make_blt(100,50,70)

# Calories Burned Calculator
def caloriesBurned(weight,miles_ran):
    print('You calories burned is ',round(weight*miles_ran*0.65,1))

caloriesBurned(178,2)