def solution(participant, completion):
    dic = {}
    for p in participant:
        dic[p] = dic.get(p, 0) + 1
    for c in completion:
        if c in dic:
            dic[c] -= 1
        
    for ele in dic:
        if dic[ele] == 1:
            return ele