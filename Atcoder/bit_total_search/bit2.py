# https://blog.rossywhite.com/2018/08/06/bit-search/
A = [0, 1, 2, 3]

for i in range(1 << len(A)): # 1をサイズNで左シフト すなわち全パターン数2^Nを表している
    output = []
    for j in range(len(A)):
        if ((i >> j)) & 1 == 1: # 右シフト AN演算子 ある数と1のANDはすなわちある数の末尾が1かの調査。ここでは各桁の調査をしている
            output.append(A[j])
    print(output)

