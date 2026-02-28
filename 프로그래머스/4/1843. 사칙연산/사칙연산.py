# 구간 DP
def solution(arr):
    # 숫자, 연산자 분리
    nums = [int(x) for x in arr[0::2]]
    ops = arr[1::2]
    n = len(nums)
    
    # 최댓값 구하기용 dp, 최솟값 구하기용 dp
    max_dp = [[-float('inf')] * n for _ in range(n)]
    min_dp = [[float('inf')] * n for _ in range(n)]
    
    for i in range(n):
        max_dp[i][i] = nums[i]
        min_dp[i][i] = nums[i]
    
    # 3중 for문 : 구간 dp의 핵심
    for step in range(1, n): # 구간 길이를 1 ~ n - 1
        for i in range(n - step): # i : 구간의 시작점
            j = i + step # j : 구간의 끝점 (시작점 + 길이)
            
            for k in range(i, j): # k는 i와 j를 가르는 분할점 (연산자 위치)
                if ops[k] == '+':
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k+1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k+1][j])
                elif ops[k] == '-':
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k+1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k+1][j])
                    
    return max_dp[0][n-1]
                

