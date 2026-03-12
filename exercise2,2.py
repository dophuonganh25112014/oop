# Exercise 2.2

import math

# 1
print((4/3) * math.pi * 5**3)

# 2
book = 24.95 * 0.6
shipping = 3 + 0.75 * 59
print(60 * book + shipping)

# 3
start = 6*60 + 52
easy = 8*60 + 15
tempo = 7*60 + 12

total = easy + 3*tempo + easy
finish = start + total

print(finish // 60, ":", finish % 60)