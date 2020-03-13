# 面白い
def is_substring(s1, s2):
    if len(s1) < len(s2):
        return False
    for i in range(len(s1)-len(s2)+1):
        sub = s1[i:i+len(s2)]
        if sub == s2:
            return True
    return False

def ans_func(s1, s2):
    s1 = s1 + s1
    return is_substring(s1, s2)

if __name__ == "__main__":
    print(ans_func("waterbottle", "bottlewater"))
