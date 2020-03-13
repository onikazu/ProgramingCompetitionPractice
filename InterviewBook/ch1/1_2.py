def sort_solution(s1, s2):
    s1_sorted = "".join(sorted(list(s1)))
    s2_sorted = "".join(sorted(list(s2)))
    if s1_sorted == s2_sorted:
        print("Yes")
    else:
        print("No")

def hash_solution(s1, s2):
    s1_hs = dict()
    s2_hs = dict()
    for c in s1:
        s1_hs[c] = s1_hs.get(c, 0) + 1
    for c in s2:
        s2_hs[c] = s2_hs.get(c, 0) + 1
    if s1_hs == s2_hs:
        print("Yes")
    else:
        print("No")


def execute_solution(s1, s2):
    print("=" * 10)
    print(f"s1: {s1}, s2: {s2}")
    sort_solution(s1, s2)
    hash_solution(s1, s2)

if __name__ == "__main__":
    execute_solution("hello", "heoll")
    execute_solution("world", "heoll")
