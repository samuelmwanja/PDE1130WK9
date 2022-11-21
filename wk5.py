'''
ELIGIBLEAGE = 18
age = eval(input("Enter your age"))
role = input("Enter your role ")

if (age >=50):
    print ("Check your eyesight.")

elif (age >= ELIGIBLEAGE and role =="student"):
    print("You can drive")
else :
    left_age = ELIGIBLEAGE - age
    print("You still have ", left_age," years to drive.")
print("BYE ")
'''

#import random#

#num = int(input("Enter number :"))#
#num = random.randint(0, 1000)#

#using a function to add two numbers#
'''
def add_numbers(num1, num2):
    ans = num1 + num2
    print ("The ans is ",ans)

add_numbers(2,4)
'''

def add_numbersv2(num1, num2):
    answer = num1 + num2
    return answer

print (add_numbersv2(3, 4))



