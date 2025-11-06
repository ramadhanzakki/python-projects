number = [4, 5, 2, 7, 8, 2]

for num in number:
    if number.count(num) > 1:
        number.remove(num)

print(number)
