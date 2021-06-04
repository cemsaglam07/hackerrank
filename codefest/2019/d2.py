# Problem D: Mikrop
import re


def ksy(x):
    return re.sub(r'(KY)*', "", x)


control = []
no = input()
s = input().strip()
while True:
    if len(s) == 0:
        control = [""]
        break
    s = ksy(s)
    control.append(s)
    if len(control) >= 2 and control[-2] == control[-1]:
        break

if control[-1] == "":
    print("EVET")
else:
    print("HAYIR")
