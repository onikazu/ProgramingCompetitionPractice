h = int(input())

ans = 0
tmp_h = h
add_step = 1
while tmp_h > 1:
    tmp_h //= 2
    ans += add_step
    add_step *= 2
ans += h 
print(ans)
