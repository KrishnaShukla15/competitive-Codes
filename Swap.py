def swap_case(s):
    res =""
    for i in range(len(s)):
        if s[i].islower() == True:
            res=res+s[i].upper()
        else:
            res=res+s[i].lower()
    return res
print(swap_case("HeLlo"))