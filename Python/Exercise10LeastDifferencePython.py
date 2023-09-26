def least_difference(a, b, c):
    dif1 = abs(a - b)
    dif2 = abs(b - c)
    dif3 = abs(a - c)
    return min(dif1, dif2, dif3)

print(
    least_difference(1, 10, 100),
    least_difference(1, 10, 10),
    least_difference(5, 6, 7),
)