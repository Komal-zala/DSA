print("==================================  FUNCTION  ==========================")

print("1. -------")
def hello():
            print("Hello World.....")
hello()

print("2. -------")
def gree(name):
              print("Hello ",name)
gree('komal')


print("3 .---------")
def  add(a,b):
              print("Addition of two number = " ,a+b)
add(5,2)


print("4.----------")
def squ(a):
            print("Square of this nyumber is ", a*a)
squ(2)

print("5.--------")
def check(a):
                if a%2==0:
                            print("This numer is Even")
                else:
                            print("This number is Odd")
check(7)

print("6.--------")
def find(a,b):
            if a>b:
                  print("A is Max then B")
            else:
                 print("B is MAx then A")
find(4,5)

print("7.--------")
def convert(c):
    print((c * 9/5) + 32)

convert(25)

print("8.---------")
def area(r):
    print("Area =", 3.14 * r * r)

area(5)

print("9.---------")
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    print("Factorial =", f)

factorial(5)

print("10.-------")
def check(n):
    if n > 0:
        print("Number is Positive")
    elif n < 0:
        print("Number is Negative")
    else:
        print("Number is Zero")

check(5)

print("11.--------")
def maximum(a, b, c):
    if a > b and a > c:
        print("A is Maximum")
    elif b > a and b > c:
        print("B is Maximum")
    else:
        print("C is Maximum")

maximum(4, 8, 6)


print("12.---------")
def count_vowels(s):
    count = 0
    for i in s:
        if i in "aeiouAEIOU":
            count = count + 1
    print("Number of Vowels =", count)

count_vowels("hello")

print("13. ---------")
def reverse(s):
    print("Reverse =", s[::-1])

reverse("hello")

print("14.-----------")
def palindrome(s):
    if s == s[::-1]:
        print("String is Palindrome")
    else:
        print("String is Not Palindrome")

palindrome("madam")

print("15.----------")
def sum_list(a):
    total = 0
    for i in a:
        total = total + i
    print("Sum =", total)

sum_list([1, 2, 3, 4, 5])

print("16.----------")
a = [10, 20, 5, 30, 15]
def largest(a):
    return max(a)

print(largest(a))

print("17.--------")
a = [1, 2, 2, 3, 3, 4]
def remove_dup(a):
    return list(set(a))
print(remove_dup(a))

print("18.--------")
a = [1, 2, 2, 3, 2, 4]
def count(a, n):
    c = 0
    for i in a:
        if i == n:
            c = c + 1
    return c

print(count(a, 2))

print("19.---------")
def prime(n):
    c = 0
    for i in range(1, n + 1):
        if n % i == 0:
            c += 1

    if c == 2:
        return True
    return False

print(prime(7))

print("20.----------")
def primes(a, b):
    for n in range(a, b + 1):
        if prime(n):
            print(n)
primes(10, 30)

print("21.---------")
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a)
        c = a + b
        a = b
        b = c

fibonacci(7)
print("22.-------")
a = [10, 5, 8, 20, 15]
def second_largest(a):
    a.sort()
    return a[-2]
print("Second largest =", second_largest(a))

print("23.--------")
def sort_list(a):
    a.sort()
    return a
a = [5, 2, 8, 1, 3]

print("Sorted list =", sort_list(a))


print("24.---------")
def merge_lists(list1, list2):
    return list(set(list1 + list2))
print("Final list =" ,merge_lists([1, 2, 3], [3, 4, 5]))

print("25.--------------- ")

def add(*args):
    return sum(args)
print(add(1, 2, 3, 4))


print("26.---------")
def details(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

details(name="Alice", age=25, city="Delhi")

print("27.---------")
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

print("28.----------")
def sum_num(n):
    if n == 0:
        return 0
    return n + sum_num(n - 1)

print(sum_num(5))

print("29.-----------")
def frequency(sentence):
    words = sentence.split()

    for word in set(words):
        print(word, words.count(word))

frequency("apple banana apple mango banana apple")

print("30.------------")
def anagram(a, b):
    return sorted(a) == sorted(b)
print(anagram("listen", "silent"))

print('\n')
print("============================================================")













