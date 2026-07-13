s = "bbbbb"
l = 0
r = l+1
maxlen = 0
while (l< len(s) and r < len(s)):
    hs = set()
    for i in range(l, r):
        hs.add(s[i])
    if s[r] in hs:
        l += 1
    else:
        r += 1
        maxlen = max(maxlen, r - l)
print (maxlen)
