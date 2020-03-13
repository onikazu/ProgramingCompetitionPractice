def brute_force(s):
    if len(list(s)) == len(set(list(s))):
        return s
    res = ""
    dup_count = 1
    for i in range(1, len(s)):
        prev_c = s[i-1]
        c = s[i]
        if c == prev_c:
            dup_count += 1
        else:
            res = res + prev_c + str(dup_count)
            dup_count = 1
    res = res + prev_c + str(dup_count)
    return res

def string_builder_solution(s):
    # どうやらpython3ではstring buiilderは考えなくてもいいっぽい？ 
    pass

if __name__ == "__main__":
    print(brute_force("aabcccccaaa"))
    print(brute_force("HelloWorld"))
            


