print("===================1====================")
print("/n")

print("1.-----------------")
n="KOMAL"
a=20
c="RAJKOT"
print("Name = " , n , "AGE = " , a ,"CITY = " , c)


print("2.-------------------")
a=1
b=2
a=b
b=a
print("Swap value " , a)

print("3.---------------------------")
l=2
b=3
Area = (l*b)
print("AREA OF RECTANGLE :: ",Area)

print("4.---------------------------")
principle=9000
intrestrate=0.07
timeinyear=5
si=principle*intrestrate*timeinyear/100
print("Simple Interest =  ", si)

print("5.--------------------------")
c=25
f=(c*9/5)+32
print("Celsius To Fahrenheit ::" , f)



print("===================2===================")




print("1.---------------------------")
a=2
b=2.8
c="Hello"
complex1=3+2j
is_logged_in=True
print("Int = ",a,"Float =",f,"Str =",c,"Bool =",is_logged_in,"Complex =",complex1)

print("2.--------------------------")
a=int(input("Enter the Number ::"))
b=float(input("Enter the float value :: "))
print(type(a))
print(type(b))

print("3.-------------------------")
a="56"
i=int(a)
f=float(a)
print("String to integer :: ",i)
print("String to float  :: ",f)

print("4.------------------------")
s="Zala Komal"
l=len(s)
print("Length of String = ",l)

print("5.------------------------")
list1=["Apple","Mango","Banana"]
set1={"Red","Green","Blue"}
tuple1=("Potato","Tomato","Onion")
dis={1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}
print(list1,"=",type(list1))
print(set1,"=",type(set1))
print(tuple1,"=",type(tuple1))
print(dis,"=",type(dis))



print("=================3==================")

print("1.----------------")
a=10
b=5
print("Addition =",a+b)
print("Subtraction =",a-b)
print("Division = ",a/b)
print("Multiplication = ",a*b)

print("2.----------------")
dividend = 10
divisor = 3
quotient=dividend // divisor
remainder = dividend%divisor
print("Quotient:", quotient)
print("Remainder:", remainder)


print("3.-----------------")
n=4
if 4%2==0:
            print("Even")
else :
            print("Odd")


print("4.----------------")
a=1
b=1

if a==b:
         print(" numbers  value is  same")

else :
         print("numbers value is not same")

print("5.----------------")
a=1
b=2
c=3

if a < b and b < c:
    print("AND: Both conditions are true")

if a == 1 or c == 5:
    print("OR: At least one condition is true")

if not a == 5:
    print("NOT: The condition is reversed")

print("6.----------------")
a = 10

a += 5
print(a)   

a -= 3
print(a)   

a *= 2
print(a)   

a /= 4
print(a)

print("7.------------")
a = 10
b = 20
if a > b:
    print("Largest number is", a)
else:
    print("Largest number is", b)


print("================= 4 =================")

print("1.------------------")

a=-6
if a<0:
       print("Nageative Number")
elif a>0:
       print("Positive Number")
else:
        print("Zero ")
        

print("2.-----------------")
a=20

if a>=18:
          print("Eligible Person To Vote")
else :
          print("NotEligible Person To Vote ")
          
print("3.-----------------")
a=100
b=2
c=3

if a>b and  a>c :
                  print("A is largest number")

elif b>a and b>c:
                 print("B  is largest number")
else:
     print("C is largest number")


print("4.----------------")
Year=int(input("Enter the year"))

if Year%4==0:
             print("This year is leap year")
else:
     print("This is not leap year ")

print("5.-------------------")
marks = float(input("Enter your marks: "))

if marks >= 90:
    grade = "A+"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B+"
elif marks >= 60:
    grade = "B"
elif marks >= 50:
    grade = "C"
elif marks >= 40:
    grade = "D"
elif marks >= 33:
    grade = "E"
else:
    grade = "F"

print("Grade:", grade)


print("6.------------------")
num = 55
if num % 5 == 0 and num % 11 == 0:
    print("Number is divisible by 5 and 11")
else:
    print("Number is not divisible by 5 and 11")


print("7.---------------------")
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if operator == "+":
    print("Result:", num1 + num2)
elif operator == "-":
    print("Result:", num1 - num2)
elif operator == "*":
    print("Result:", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")


print("=======================5=========================")

print("1.-----------------")
print("\n")


for i in range(1, 11):
    print(i)

print("\n")
print("2.-----------------")
print("\n")
i = 10
while i >= 1:
    print(i)
    i -= 1

print("\n")
print("3.------------------")
print("\n")
num = int(input("Enter a number: "))

for i in range(1, 11):
    print(num, "x", i, "=", num * i)

    
print("\n")
print("4.----------------------")
print("\n")
n = int(input("Enter n: "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("Sum =", sum)

print("\n")
print("5.-----------------")
print("\n")
n = int(input("Enter a number: "))
fact = 1

for i in range(1, n + 1):
    fact *= i

print("Factorial =", fact)


print("\n")
print("6.------------------")
print("\n")
for i in range(2, 101, 2):
    print(i)


print("\n")
print("7.------------------")
print("\n")
num = int(input("Enter a number: "))
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

print("Reversed number:", reverse)


print("\n")
print("8.-----------------")
print("\n")
num = int(input("Enter a number: "))
count = 0

while num != 0:
    num = num // 10
    count += 1
print("Number of digits:", count)



print("\n")
print("9.-----------------")
print("\n")
num = int(input("Enter a number: "))

if num < 2:
    print("Not a prime number")
else:
    prime = True

    for i in range(2, num):
        if num % i == 0:
            prime = False
            break

    if prime:
        print("Prime number")
    else:
        print("Not a prime number")

        

print("\n")
print("10.-------------------")
print("\n")
n = int(input("Enter number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
