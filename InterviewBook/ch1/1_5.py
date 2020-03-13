def brute_force(s1, s2):
    length_gap = abs(len(s1) - len(s2))
    if length_gap == 0:
        return check_replace(s1, s2)
    elif length_gap == 1:
        return check_insert(s1, s2)
    return False


def check_replace(s1, s2):
    diff_flag = False
    for i in range(len(s1)):
        c1 = s1[i]
        c2 = s2[i]
        if c1 != c2:
            if diff_flag:
                return False
            diff_flag = True
    return True


def check_insert(long_s, short_s):
    if len(long_s) < len(short_s):
        long_s, short_s = short_s, long_s
    long_idx= 0
    short_idx = 0
    while len(long_s) <= long_idx or len(short_s) <= short_idx:
        long_c = long_s[long_idx]
        short_c = short_s[short_idx]
        if long_c != short_c:
            if long_idx != short_idx:
                return False
            long_idx += 1
        else:
            long_idx += 1
            short_idx += 1
    return True


if __name__ == "__main__":
    print(brute_force("pale", "ple"))
    print(brute_force("pale", "bale"))
    print(brute_force("pale", "bake"))


