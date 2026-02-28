def solution(money):
    n = len(money)
    # 원형 : 첫 집을 무조건 터는 경우와 안 터는 경우로 나누자
    dp1 = [0] * n
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])
    
    for i in range(2, n - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + money[i])
    
    dp2 = [0] * len(money)
    dp2[0] = 0
    dp2[1] = money[1]

    for i in range(2, n):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])
            
    return max(max(dp1), max(dp2))

# 1 2 3 1
# index 0과 2번을 훔치면 최댓값 : 4