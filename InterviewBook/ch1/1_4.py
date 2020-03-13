# assume that not to distinguish larger or smaller case
# assume that string include spaces
def brute_force(s):
    s = "".join(s.split(" "))
    s = s.lower()
    ch_l = [0] * (ord("z")-ord("a")+1)
    for ch in s:
        ch_i = ord(ch) - ord("a")
        ch_l[ch_i] += 1
    return check_list_v1(ch_l)

def check_list_v1(l):
    num_odd = 0
    for v in l:
        if v % 2 == 1:
            num_odd += 1
    if num_odd > 1:
        return False
    else:
        return True


def revised_force1(s):
    s = "".join(s.split(" "))
    s = s.lower()
    ch_l = [0] * (ord("z")-ord("a")+1)
    for ch in s:
        ch_i = ord(ch) - ord("a")
        ch_l[ch_i] += 1
    return check_list_v2(ch_l)


def check_list_v2(l):
    num_odd = 0
    for v in l:
        if v % 2 == 1:
            num_odd += 1
        if num_odd == 2:
            return False
    return True

def bit_solution(s):
    pass

if __name__ == "__main__":
    print(brute_force("taco cat"))
    print(brute_force("atco cta"))
    print(brute_force("tomato"))

