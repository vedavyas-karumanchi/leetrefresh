nums1 = [1,3]
nums2 = [2]
res=[]
l,r=0,0
while l < len(nums1) or r < len(nums2):
    print (f"(l={l}, r={r}) -> res={res}")
    if l >= len(nums1):
        res.append(nums2[r])
        r += 1
    elif r >= len(nums2):
        res.append(nums1[l])
        l += 1
    elif nums1[l] < nums2[r]:
        res.append(nums1[l])
        l += 1
    else:
        res.append(nums2[r])
        r += 1
print (res)