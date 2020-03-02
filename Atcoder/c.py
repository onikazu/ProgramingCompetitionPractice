n = int(input())
A = []
proofs = []
for i in range(n):
    A.append(int(input()))
    proof = [tuple(map(int, input().split())) for _ in range(A[i])]
    proofs.append(proof)

def check_amb(true_men, proofs):
    for true_man in true_men:
        proof = proofs[true_man]
        for x, y in proof:
            if (x-1 in true_men) and (y == 0):
                return True
            if (x-1 not in true_men) and (y == 1):
                return True
    return False


max_pat = 0
for i in range(1 << n):
    true_men = []
    for j in range(n):
        if ((i >> j) & 1) == 1:
            true_men.append(j)
    is_amb = check_amb(true_men, proofs)
    if is_amb is False:
        max_pat = max(len(true_men), max_pat)

print(max_pat)




