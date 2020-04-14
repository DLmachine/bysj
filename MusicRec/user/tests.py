def WaitInLine(a, b):
    # write code here
    m = {}
    for i in range(1, len(a) + 1):
        m[i] = a[i-1]-b[i-1]
    ss=sorted(m.items(), key=lambda x: x[1], reverse=True)
    res=[i[0] for i in ss]
    return res

print(WaitInLine([8,9,7],[5,8,3]))