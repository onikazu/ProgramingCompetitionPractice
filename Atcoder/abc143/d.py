import bisect

def solve():
    N = int(input())
    Ls = list(map(int, input().split()))
    Ls.sort()
    
    ans = 0
    for a_i in range(N):
        for b_i in range(a_i+1, N):
            c_i = bisect.bisect_left(Ls, Ls[a_i] + Ls[b_i])
            if c_i > b_i:
                ans += c_i - b_i -1
            else:
                pass
    print(ans)

solve()

