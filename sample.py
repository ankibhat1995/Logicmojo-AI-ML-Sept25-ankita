a=10 type(a) **int**
b=10.5 type(b) **float**
a=7+3j  type(a) **complex** 
print(a.real)  7.0
print(a.imag)  3.0
name="Ankita" print(name) type(name) Ankita,str  ----**String**
my_tuple = (10, 20, 30, 40) print(my_tuple)----- **tuple**
fruits = ["apple", "banana", "cherry"]   **List**
print(fruits[1])          # Accessing items
fruits[1] = "mango"       # Changing items
fruits.append("orange")   # Adding items at end
fruits.insert(1, "grape") # Adding items in specific place .
fruits.remove("mango")    # remove by value
fruits.pop(0)             # remove by index
del fruits[1]             # delete by index
my_set = {1, 2, 3, 4, 4, 2}                 **set**
{1, 2, 3, 4}   # duplicates removed automatically
person = {"name": "Ankita","age": 30,"city": "Kolkata"}   **Dictionary**
Here is the complete set — 10 questions with their answers, one by one, in clean copy-paste format.
****************************IF ELSE**************************************************************

✅ 1️⃣ Problem 1 — Positive, Negative, Zero

Write a program that checks if a number n is:

Positive

Negative

Zero

Answer:

n = 10

if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

✅ 2️⃣ Problem 2 — Even or Odd

Write a program that checks if a number is even or odd.

Answer:

n = 7

if n % 2 == 0:
    print("Even")
else:
    print("Odd")

✅ 3️⃣ Problem 3 — Largest of Two Numbers

Write a program that prints which number is larger or if both are equal.

Answer:

a = 10
b = 20

if a > b:
    print("a is larger")
elif b > a:
    print("b is larger")
else:
    print("Both are equal")

✅ 4️⃣ Problem 4 — Vowel or Consonant

Check if a character is a vowel or consonant.

Answer:

ch = "a"

if ch.lower() in "aeiou":
    print("Vowel")
else:
    print("Consonant")

✅ 5️⃣ Problem 5 — Password Check

If password is "python123" → print Access Granted.
Else → print Access Denied.

Answer:

password = "python123"

if password == "python123":
    print("Access Granted")
else:
    print("Access Denied")

✅ 6️⃣ Problem 6 — Divisible by 3 and/or 5

Write a program to check:

Divisible by both 3 and 5

Divisible by 3 only

Divisible by 5 only

Not divisible

Answer:

n = 15

if n % 3 == 0 and n % 5 == 0:
    print("Divisible by both")
elif n % 3 == 0:
    print("Divisible by 3")
elif n % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible")

✅ 7️⃣ Problem 7 — Grade Calculator

Given marks (0–100):

= 90 → A

= 75 → B

= 60 → C

= 40 → D

Else → Fail

Answer:

marks = 82

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
elif marks >= 40:
    print("D")
else:
    print("Fail")

✅ 8️⃣ Problem 8 — Leap Year Checker

Rules:

Divisible by 400 → Leap Year

Divisible by 100 → Not Leap Year

Divisible by 4 → Leap Year

Answer:

year = 2024

if year % 400 == 0:
    print("Leap Year")
elif year % 100 == 0:
    print("Not Leap Year")
elif year % 4 == 0:
    print("Leap Year")
else:
    print("Not Leap Year")

✅ 9️⃣ Problem 9 — Smallest of Three Numbers

Print the smallest value among a, b, and c.

Answer:

a = 5
b = 3
c = 8

if a <= b and a <= c:
    print(a, "is smallest")
elif b <= a and b <= c:
    print(b, "is smallest")
else:
    print(c, "is smallest")

✅ 🔟 Problem 10 — Billing Discount

Discount rules:

≥ 5000 → 20%

≥ 3000 → 10%

≥ 1000 → 5%

Else → No discount

Answer:

bill = 4500

if bill >= 5000:
    discount = bill * 0.20
elif bill >= 3000:
    discount = bill * 0.10
elif bill >= 1000:
    discount = bill * 0.05
else:
    discount = 0

final_amount = bill - discount
print("Final Amount =", final_amount)

1️⃣ — Simple if
Example
age = 18
if age >= 18:
    print("You can vote")


2️⃣ — if with else
Example
age = 16
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote yet")


3️⃣ — if / elif / else (multiple branches)
Example (grading)
marks = 76

if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
else:
    grade = "C or below"

print("Grade:", grade)


4️⃣ — Nested if
Example
x = 10
if x > 0:
    print("Positive")
    if x % 2 == 0:
        print("Even number")

5️⃣ — Boolean operators (and, or, not)
Example
age = 20
has_id = True

if age >= 18 and has_id:
    print("Allowed")
else:
    print("Not allowed")


8️⃣ — Ternary operator (short if)
Example
age = 17
message = "Adult" if age >= 18 else "Minor"
print(message)


9️⃣ — if with input()
Example
n = int(input("Enter a number: "))  # user types 7
if n % 2 == 0:
    print("Even")
else:
    print("Odd")

🔟 — Using pass for an empty block
Example
if condition:
    pass  # do nothing for now
else:
    print("Other")
