# If-Else Practice Examples (Ankita)

# 1. Positive, Negative, Zero
def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

# 2. Even or Odd
def even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

# 3. Largest of Two Numbers
def largest(a, b):
    if a > b:
        return "a is larger"
    elif b > a:
        return "b is larger"
    else:
        return "Both are equal"

# 4. Vowel or Consonant
def vowel_consonant(ch):
    if ch.lower() in "aeiou":
        return "Vowel"
    else:
        return "Consonant"

# 5. Password Check
def password_check(p):
    if p == "python123":
        return "Access Granted"
    else:
        return "Access Denied"

# 6. Divisible by 3 and/or 5
def divisible(n):
    if n % 3 == 0 and n % 5 == 0:
        return "Divisible by both"
    elif n % 3 == 0:
        return "Divisible by 3"
    elif n % 5 == 0:
        return "Divisible by 5"
    else:
        return "Not divisible"

# 7. Grade System
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

# 8. Leap Year
def leap_year(year):
    if year % 400 == 0:
        return "Leap Year"
    elif year % 100 == 0:
        return "Not Leap Year"
    elif year % 4 == 0:
        return "Leap Year"
    else:
        return "Not Leap Year"

# 9. Minimum of Three Numbers
def smallest(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c

# 10. Billing Discount
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
