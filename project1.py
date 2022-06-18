def sum_of_squears(a, b, c):
"""this function will find out two bigest numbers and will count the sum of the squares of those numbers"""
if a > c and  b > c:
         return a**2 + b**2
 elif  a > b and c > b:
         return a**2 + c**2
 else: 
          return b**2 + c**2
 print("sum of squears is :", sum_of_squears(0, 6, 10))
