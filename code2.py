arr = [1, 2, 3, 4, 2, 5, 3, 6]

repeating = []

for num in arr:
    if arr.count(num) > 1 and num not in repeating:
        repeating.append(num)

print("Repeating numbers:", repeating)
