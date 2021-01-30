import math
import csv

with open('data.csv', newline = '') as f:
    reader = csv.reader(f)
    fileData = list(reader)

data = fileData[0]

def mean(data):
    length = len(data)
    total = 0

    for w in data:
        total += int(w)

    mean = total / length
    return mean

squaredList = []
for number in data:
    a = int(number) - mean(data)
    a = a**2
    squaredList.append(a)

sum1 = 0
for a in squaredList:
    sum1 = sum1 + a

result = sum1 / (len(data)-1)

standardDeviation = math.sqrt(result)
print(standardDeviation)