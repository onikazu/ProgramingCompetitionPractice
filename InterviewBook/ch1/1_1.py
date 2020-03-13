def brute_force(s):
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                print("There is duplicate charactor!!")
                return
    print("There is no duplicate charactor!!")


def hash_solution(s):
    hs = set()
    for c in s:
        if c in hs:
            print("There is duplicate charactor!!")
            return 
        hs.add(c)
    print("There is no duplicate charactor!!")


def sort_solution(s):
    s_l = sorted(list(s))
    for i in range(1, len(s_l)):
        if s_l[i-1] == s_l[i]:
            print("There is duplicate charactor!!")
            return
    print("There is no duplicate charactor!!")


def execute_solutions(s):
    print(f"target string: {s}")
    brute_force(s)
    hash_solution(s)
    sort_solution(s)
    print("=" * 20)

if __name__ == "__main__":
    execute_solutions("abcdef")
    execute_solutions("hello, world")

