a=10
print(a)

num = 10
print("the value of num is:", num)
num += 5
print("the value of num after += 5 is:", num)
num -= 3
print("the value of num after -= 3 is:", num)
num *= 2
print("the value of num after *= 2 is:", num)
num /= 4
print("the value of num after /= 4 is:", num)
num %= 3
print("the value of num after %= 3 is:", num)
num **= 2
print("the value of num after **= 2 is:", num)



#switch case

def switch_exam(day):
    switcher = {
        "Monday": "Math",
        "Tuesday": "English",
        "Wednesday": "Science",
        "Thursday": "History",
        "Friday": "Art"
    }
    return switcher.get(day, "No exam scheduled")

# if else

num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
if num % 2 == 0:
    print("The number is even.")
    else:
print("The number is odd.")


#write a program to check whether a number is positive, negative or zero using if-else statement
num = float(input("Enter a number:"))
if num > 0:
    print("the number is positive")
elif num < 0:
    print("the number is negative")
else:
    print("the number is zero")





 #write a program to check if a person is eligible to vote or not using if-else statement
age = int (input("Enter your age:"))
if age >= 18:
        print("you are eligible to vote")
else:
        print("you are not eligible to vote")


        #check odd even
num = int(input("Enter a number:"))
if num % 2 == 0:
    print("the number is even")
else:
    print("the number is odd")


    #Take two number and print greater one 
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print("The greater number is:", num1)
else:
    print("The greater number is:", num2)


    #take a students marks as input and print thier grade 
marks = int(input("Enter the student's marks;"))
if marks >= 90:
    print("grade; A")
elif marks >= 80:
    print("grade; B")
elif marks >= 70:
    print("grade; C")
elif marks >= 60:
    print("grade; D")
else:
    print("grade; Fail")


    #check leap year
year = int (input("Enter a year:"))
if(year % 4 ==0 and year %100 !=0) or (year %400 ==0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))



    #single digit double digit or more tha two digit
num = int(input("Enter a number:"))
if num <10:
    print ("the number is single digit")
elif num <100:
    print ("the number is double digit")
else:
    print ("the number is more than two digit")
    


    #weekdays
num = (input("day number: "))
if num == '1':
    print("Monday")
elif num == '2':
    print("Tuesday")
elif num == '3':
    print("Wednesday")
elif num == '4':
    print("Thursday")
elif num == '5':
    print("Friday")
elif num == '6':
    print("Saturday")
elif num == '7':
    print("Sunday")
