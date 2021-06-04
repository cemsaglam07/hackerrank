n = "DOGRU"
for i in range(9):
    x = input().split()
    if sorted(x) != ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        n = "YANLIS"
print(n)
