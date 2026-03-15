numbers = range(0, 100)

for num in numbers:
    if num % 2 == 0:
        print(str(num) + " is even")
    else:
        print(str(num) + " is odd")

if 10 in numbers:
    print("10 is in numbers")

scores = [90, 80, 70, 60, 50]
for id in (range(0, len(scores))):
    score = scores[id]
    if score >= 90:
        print(str(id) + ": A")
    elif score >= 80:
        print(str(id) + ": B")
    elif score >= 70:
        print(str(id) + ": C")
    elif score >= 60:
        print(str(id) + ": D")
    else:
        print(str(id) + ": F")

