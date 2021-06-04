# Problem D: Mikrop
import re


def ksy(x):
    return re.sub(r'K[S]*Y', "S", x)


control = []
no = input()
s = input().strip()
while True:
    s = ksy(s)
    control.append(s)
    if len(control) >= 2 and control[-2] == control[-1]:
        break

if control[-1][-1] == "S":
    print("EVET")
else:
    print("HAYIR")
