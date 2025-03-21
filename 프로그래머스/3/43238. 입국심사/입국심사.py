def solution(n, times):
    low = 1
    high = max(times) * n # 걸릴 수 있는 최대 시간
    
    while low <= high:
        mid = (low + high) // 2 # mid가 최소 시간을 뜻하는 값으로 조정 시작
        people = 0
        
        for time in times:
            people += mid // time
            
            if people >= n:
                break
                
        if people >= n: # n명 초과 -> 시간 오버, n명이어도 시간은 남을 수 있음
            answer = mid
            high = mid -1
        else : # n명 미만 -> 시간 부족
            low = mid + 1
            
    return answer
    
    