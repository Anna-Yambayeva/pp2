
def permutate(s,ans=""):
    if len(s)==0:
        print(ans)
        return ""
    for i in range (0,len(s)):
        a=s[i]
        s_a=s[:i]+s[i+1:]
        permutate(s_a, a+ans)


def has_33(nums):
    for i in range (0,len(nums)):
        if nums[i]==3:
            if (i>=1)and(i<=(len(nums)-2)):
                if (nums[i]==nums[i-1]):
                    return True
                if (nums[i]==nums[i+1]):
                    return True
    return False


def unic(list):
    new_list=[]
    for i in range (0,len(list)):
        is_here=False
        for j in range(0,len(new_list)):
            if list[i]==new_list[j]:
                is_here=True
        if (not is_here):
            new_list.append(list[i])
    return new_list

def palyndrom(slovo):
    if slovo == slovo[::-1]:
        print("yes")
        return ""
    print ("no")
    return ""