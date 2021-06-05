def sup_str(arr):
    if len(arr) == 1:
        return arr[0]
    dic = {}
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j:
                ol = 0
                for k in range(1, min(len(arr[i]), len(arr[j]))):
                    if arr[j][:k] == arr[i][-k:]:
                        ol = k
                dic[(i, j)] = ol
    if max(dic.values()) == 0:
        return "".join(arr)
    ret = "".join(arr)
    lr = len(ret)
    stack = []
    for i, wd in enumerate(arr):
        tmp = set(range(len(arr)))
        tmp.remove(i)
        stack.append((wd, i, tmp))
    while stack:
        aaa, bbb, ccc = stack.pop()
        if len(aaa) < lr:
            if not ccc:
                ret = aaa
                lr = len(ret)
            else:
                tmp = [[dic[bbb, ddd], ddd] for ddd in ccc]
                tmp.sort()
                for ol, ddd in tmp:
                    aaa2 = aaa + arr[ddd][ol:]
                    ccc2 = set(ccc)
                    ccc2.remove(ddd)
                    stack.append((aaa2, ddd, ccc2))
    return ret


sss = input().split()
sss2 = input().strip()
cf, fc, cc, ff = [int(i) for i in sss]
zzz = []

for i in range(cf):
    zzz.append("CF")
for i in range(fc):
    zzz.append("FC")
for i in range(cc):
    zzz.append("CC")
for i in range(ff):
    zzz.append("FF")

result = sup_str(zzz)
print(result.count("C"), result.count("F"))
if sss2 == "yes":
    print(result)
