def solution(s):
    if len(s) == 1:
        return 1
        
    answer = len(s)

    for unit in range(1, len(s) // 2 + 1):
        compressed_len = 0
        prev = s[:unit] # 첫 번째 블록
        cnt = 1       # 반복 횟수

        for i in range(unit, len(s), unit):
            curr = s[i : i + unit] # 현재 블록
            
            if prev == curr:
                cnt += 1
            else:
                # 이전 블록 정산
                # (압축되면 '숫자길이' + '단위길이', 안 되면 '단위길이')
                if cnt > 1:
                    compressed_len += len(str(cnt)) + unit
                else:
                    compressed_len += unit
                
                # 초기화
                prev = curr
                cnt = 1
        
        if cnt > 1:
            compressed_len += len(str(cnt)) + len(prev)
        else:
            compressed_len += len(prev)
            
        answer = min(answer, compressed_len)

    return answer