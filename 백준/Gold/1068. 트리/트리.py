import sys

input = sys.stdin.readline


def dfs(num, arr):
    arr[num] = -2  # 부모의 정보가 -2인 노드를 없는 노드로 취급
    for i in range(len(arr)):
        if num == arr[i]:  # 부모가 없애야 할 노드와 같을 때
            dfs(i, arr)  # 재귀로 들어가 해당 노드도 없는 노드 인식 번호 -2로 change


n = int(input())
parent = list(map(int, input().split()))
d = int(input())

dfs(d, parent)
cnt = 0
for i in range(n):
    if parent[i] != -2 and i not in parent:  # 존재 노드 + i 번째 노드가 누구의 부모도 아님
        cnt += 1

print(cnt)
