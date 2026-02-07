def solution(N, number):
    dp = [set() for i in range(9)]
    
    for i in range(1, 9):
        dp[i].add(int(str(N) * i))
        
    ans = -1
    
    for i in range(1, 9):
        for j in range(i):
            for op1 in dp[j]:
                for op2 in dp[i - j]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op1 != 0:
                        dp[i].add(op2 // op1)                    
        
        if number in dp[i]:
            ans = i
            return ans
    
    return ans


# dp[5][12] = min(
#    (dp[5][5] + dp[5][5] + dp[5][1] + dp[5][1]),
#    (dp[5][11] + dp[5][1]),
#    (dp[5][12]) -> ?)

# 다른 방식의 접근
# 5를 1번 사용 : 5
# 5를 2번 사용 : 55, 5+5, 5-5, 5*5, 5//5
# 5를 3번 사용 : 1번 사용과 2번 사용을 이용
# 5를 4번 사용 : 1번 + 3번, 2번 + 2번
# ...

