import sys
input = sys.stdin.readline
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LI(): return list(map(int, input().split()))

def main():
    N = INT()
    A = [INT() for _ in range(N)]
    stack = [10 ** 9]
    from bisect import bisect_left

    for i in range(N):
        index = bisect_left(stack, A[i])
        if index == len(stack):
            stack.append(A[i])
        else:
            stack[index] = A[i]
    print(N-len(stack))

if __name__ == "__main__":
    main()

