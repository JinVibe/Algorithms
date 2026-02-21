def backtracking(arr):
    if len(arr) == L:
        if promising(arr):
            print("".join(arr))
            return

    for i in range(len(arr), C):
        if arr[-1] < alpha[i]:
            arr.append(alpha[i])
            backtracking(arr)
            arr.pop()


def promising(arr):
    mo, ja = 0, 0

    for ele in arr:
        if ele in aeiou:
            mo += 1
        else:
            ja += 1

    if mo >= 1 and ja >= 2:
        return True
    else:
        return False


L, C = map(int, input().split())

alpha = input().split()
alpha.sort()

aeiou = "aeiou"

for i in range(C-L+1):
    a = [alpha[i]]
    backtracking(a)



