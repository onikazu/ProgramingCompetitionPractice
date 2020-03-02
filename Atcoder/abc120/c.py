s = list(input())

ans = 0
stack = []
for c in s:
    print(stack)
    if not stack or stack[-1] != c:
        stack.append(c)
    elif stack[-1] == c:
        stack.pop()
        ans += 2
print(ans)

