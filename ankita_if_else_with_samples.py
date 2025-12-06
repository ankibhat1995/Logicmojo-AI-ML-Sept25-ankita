# If-Else Practice Examples (Ankita) + 10 Sample Runs

# -----------------------------
# 1. Positive, Negative, Zero
Write a program that checks if a number n is:
Positive
Negative
Zero
# -----------------------------
def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

# -----------------------------
# 2. Even or Odd
# -----------------------------
def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

samples_even_odd = [
    even_odd(2),
    even_odd(9),
    even_odd(0)
]


# -----------------------------
# 3. Largest of Two Numbers
# -----------------------------
def largest(a, b):
    if a > b:
        return "a is larger"
    elif b > a:
        return "b is larger"
    else:
        return "Both are equal"

samples_largest = [
    largest(10, 5),
    largest(3, 8),
    largest(7, 7)
]


# -----------------------------
# 4. Vowel or Consonant
# -----------------------------
def vowel_consonant(ch):
    if ch.lower() in "aeiou":
        return "Vowel"
    else:
        return "Consonant"

samples_vowel = [
    vowel_consonant("a"),
    vowel_consonant("b"),
    vowel_consonant("o")
]


# -----------------------------
# 5. Password Check
# -----------------------------
def password_check(p):
    if p == "python123":
        return "Access Granted"
    else:
        return "Access Denied"

samples_password = [
    password_check("python123"),
    password_check("wrongpassword")
]


# -----------------------------
# 6. Divisible by 3 and/or 5
# -----------------------------
def divisible(n):
    if n % 3 == 0 and n % 5 == 0:
        return "Divisible by both"
    elif n % 3 == 0:
        return "Divisible by 3"
    elif n % 5 == 0:
        return "Divisible by 5"
    else:
        return "Not divisible"

samples_divisible = [
    divisible(15),
    divisible(9),
    divisible(10),
    divisible(7)
]


# -----------------------------
# 7. Grade System
# -----------------------------
def grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "Fail"

samples_grade = [
    grade(95),
    grade(80),
    grade(62),
    grade(35)
]


# -----------------------------
# 8. Leap Year Checker
# -----------------------------
def leap_year(year):
    if year % 400 == 0:
        return "Leap Year"
    elif year % 100 == 0:
        return "Not Leap Year"
    elif year % 4 == 0:
        return "Leap Year"
    else:
        return "Not Leap Year"

samples_leap = [
    leap_year(2020),
    leap_year(2023),
    leap_year(2000),
    leap_year(1900)
]


# -----------------------------
# 9. Smallest of Three Numbers
# -----------------------------
def smallest(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c

samples_smallest = [
    smallest(2, 5, 9),
    smallest(8, 3, 6),
    smallest(4, 4, 7)
]


# -----------------------------
# 10. Billing Discount
# -----------------------------
def billing(bill):
    if bill >= 5000:
        discount = bill * 0.20
    elif bill >= 3000:
        discount = bill * 0.10
    elif bill >= 1000:
        discount = bill * 0.05
    else:
        discount = 0
    return bill - discount

samples_billing = [
    billing(6000),
    billing(3500),
    billing(1200),
    billing(500)
]


# -----------------------------
# PRINT ALL SAMPLES TOGETHER
# -----------------------------
print("SAMPLE OUTPUTS FOR ALL FUNCTIONS:\n")

print("1. Check Number Samples:", samples_check_number)
print("2. Even/Odd Samples:", samples_even_odd)
print("3. Largest Samples:", samples_largest)
print("4. Vowel Samples:", samples_vowel)
print("5. Password Samples:", samples_password)
print("6. Divisible Samples:", samples_divisible)
print("7. Grade Samples:", samples_grade)
print("8. Leap Year Samples:", samples_leap)
print("9. Smallest Samples:", samples_smallest)
print("10. Billing Samples:", samples_billing)

