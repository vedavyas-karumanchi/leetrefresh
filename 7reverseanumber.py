x = 1534236469

strx = str(x)

# if strx[0] == '-':
#     strx= strx[1:]
#     reversed_strx = strx[::-1]
#     print()
#     print(-1 * (int(reversed_strx)))
# else : 
#     reversed_strx = strx[::-1]
#     print()
#     print(int(reversed_strx))


if (x >= -(2 **31) and x <= (2**31) -1):
    if strx[0] == '-':
        strx= strx[1:]
        reversed_strx = strx[::-1]
        print()
        print(-1 * (int(reversed_strx)))
    else : 
        reversed_strx = strx[::-1]
        print()
        print(int(reversed_strx))