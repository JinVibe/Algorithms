from collections import deque

def solution(queue1, queue2):
    cnt = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    # 최악의 경우의 수 (머리 속에서 계산은 정확히 안 되지만 이건 안 넘겠지..?)
    total = (len(queue1) + len(queue2)) * 2
    
    # sum 연산이 시간을 많이 잡아먹음
    # while sum(queue1) != sum(queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    while sum1 != sum2:
        if sum1 > sum2:
            tmp = queue1.popleft()
            queue2.append(tmp)
            sum1 -= tmp
            sum2 += tmp
            cnt += 1
        else:
            tmp = queue2.popleft()
            queue1.append(tmp)
            sum2 -= tmp
            sum1 += tmp
            cnt += 1
        
        if total < cnt:
            return -1
    
    return cnt