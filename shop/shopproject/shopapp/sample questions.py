#Exercise 1: Print First 10 natural numbers using while loop

i=1
while i<=10:
    print(i);
    i=i+1


#Write a program to accept person is eligible for voting

x=int(input("Enter your age :"))
if x>=18:
    print("Eligible for voting")
else:
    print("Not Eligible for voting")

#write a pgm to check odd/even number

x=int(input("Enter your Number :"))
if x%2==0:
    print("EVEN NUMBER")
else:
    print("odd number")


#write a pgm to check whether a number is divisible by 7

x=int(input("Enter your Number :"))
if x%7==0:
    print("Multiple of 7")
else:
    print("Not divisible")

#write a pgm to calculate the electricity bill
#first 100 unit -no charge
#next 100 - 5 per unit
#after 200- 10 per unit
#eg:if bill unit  is 350 amount should be 2000

x=int(input("Enter your Unit :"))
if x<100:
    print("No charge")
elif x>=100 and x<200:
    print((x-100)*5)
elif x>=200:
    print(500+(x-200)*10)

 #write a pgm to disply the last digit of a number

x = int(input("Enter your numbeer"))
print("LAST DIGIT IS ", x % 10)

#Write a pgm to check whether las t number os divisible by 3
x=int(input("Enter your number:"))
y=x%10
if (y%3==0):
    print("Number is divisible by 3")
else:
    print("Not divisible")

#write a pgm to accept the mark from user and display the grade
x=int(input("Enter your Mark:"))
if x>90 and x<=100:
    print("Grade is A")
elif x>80 and x<=90:
    print("Grade B")
elif x>=60 and x<=80:
    print("Grade C")
elif x<60:
    print("Grade D")
else:
    print("Enter a valid Number")

#write a pg to check the leap year
x=int(input("Enter the year"))
if x%4==0:
    print("Leap year")
else:
    print("Not a leap year")

#write a pgm to check the 3 digit number
x=(input("Enter the Number"))

l=len(x)
if l==3:
    print("3 digit number")
else:
    print("Not 3 digit")

#write a pgm to find the lowest number
x=int(input("Enter the Number"))
y=int(input("Enter the second number"))
if x>y:
    print("Lowest number is",y)
else:
    print("Lowest number is ",x)

    