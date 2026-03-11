def solution(s):
    answer = []
    # 양쪽 괄호 제거
    s = s[1:-1]
    
    # 왼쪽 괄호 인덱스랑 오른쪽 괄호 인덱스를 저장해서 리스트로 바꿈
    left = []
    right = []
    
    for i in range(len(s)):
        if s[i] == '{':
            left.append(i)
        elif s[i] == '}':
            right.append(i)
            
    arr = []
    # 각 괄호에서 숫자들만 뽑아내서 리스트에 저장
    for i in range(len(left)):
        arr.append(list(map(int, s[left[i] + 1 : right[i]].split(','))))
    # 리스트 정렬 - 리스트 길이 기준
    arr.sort(key=len)
    
    # 요소 내에서 작은 거부터 시작해 하나씩 추가 -> 좀 더 효율적으로 못 만드려나..
    for subset in arr:
        for num in subset:
            if num not in answer:
                answer.append(num)
                break
    
    return answer

# 튜플은 중복된 원소 가짐
# 원소에 순서가 있어 순서 다르면 안 됨
# 튜플 개수는 유한함
