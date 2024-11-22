# ternary operations
score = int(input('Enter a score between 0 & 100:'))

#conditional assignments /ternary
is_top_score = True if score >= 90 else False
print(f'is_top_score {is_top_score}')

#nested ternary

temp = int(input('Enter a temp in celsius between 0 & 40'))

weather = "hot" if temp > 35 else ("miled" if temp > 20 else "cold")
print(weather)