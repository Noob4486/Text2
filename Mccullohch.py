# AND operation
def fire(theta, sum):
    if sum >= theta:
        return 1
    else:
        return 0

inp = [[1, 1, 1], [1, 1, 0], [0, 0, 1], [0, 0, 0]]
for i in inp:
    sum = 0
    for j in i:
        sum += j
    print("AND(", i, ")=", fire(len(i), sum))

# OR operation
def fire(theta, sum):
    if sum >= theta:
        return 1
    else:
        return 0

inp = [[1, 1, 1], [1, 1, 0], [0, 0, 1], [0, 0, 0]]
for i in inp:
    sum = 0
    for j in i:
        sum += j
    print("OR(", i, ")=", fire(1, sum))

# NOT operation
def firen(sum, theta):
    if sum == theta:
        return 1
    else:
        return 0

inpt = [0, 1]
for i in inpt:
    print("NOT(", i, ")=", firen(0, i))
