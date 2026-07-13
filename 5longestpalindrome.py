s = "cbbd"

def isPalindrome(arr,l,r):
    while l < r:
        if arr[l] != arr[r]:
            return False
        l += 1
        r -= 1
    return True


maxPalindromeLength = 0
maxPalindrome = ""
left, right = 0, 0
while right < len(s):
    print(f"Checking substring: {s[left:right+1]}")
    if isPalindrome(s, left, right) and len(s[left:right+1]) > 1:
        print(f"Found palindrome: {s[left:right+1]}")
        if right - left + 1 > maxPalindromeLength:
            maxPalindromeLength = right - left + 1
            maxPalindrome = s[left:right+1]
            print(f"Updated max palindrome: {maxPalindrome} with length {maxPalindromeLength}")
        left += 1
        print(f"shrinking left to {left} : updated left and right to {left} and {right}")
    else:
        right += 1
        print(f"expanding right to {right}")
        if left > right:
            right = left
print(maxPalindrome)
    