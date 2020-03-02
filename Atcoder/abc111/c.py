# input
n = int(input())
v = list(map(int, input().split()))

# special case
if len(set(v)) == 1:
    print(len(v) // 2)
    exit()

d_odds = {}
d_even = {}

for i in range(0, len(v), 2):
    if v[i] in d_even:
        d_even[v[i]] += 1
    else:
        d_even[v[i]] = 1
    
for i in range(1, len(v), 2):
    if v[i] in d_odds:
        d_odds[v[i]] += 1
    else:
        d_odds[v[i]] = 1
 
max_freq_even = max(d_even.values())
if len(d_even.values()) > 1:
    max_freq_even_2nd = sorted(d_even.values())
else:
    max_freq_even_2nd = float("inf")

max_freq_odds = max(d_odds.values())
if len(d_odds.values()) > 1:
    max_freq_odds_2nd = sorted(d_odds.values())
else:
    max_freq_odds_2nd = float("inf")

if max_freq_even == max_freq_odds and max_freq_even_2nd != float("inf") and max_freq_even_2nd != float("inf"):
    print(max(n-max_freq_even-max_freq_odds_2nd, n-max_freq_even_2nd-max_freq_odds))
    exit()

print(n - max_freq_even - max_freq_odds)

