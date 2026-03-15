from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0
    
    q = deque()
    q.append([begin, 0]) 
    
    visited = [False] * len(words)
    
    while q:
        current_word, step = q.popleft()
        
        if current_word == target:
            return step
        
        for i in range(len(words)):
            if not visited[i]:
                diff_count = 0
                for c1, c2 in zip(current_word, words[i]):
                    if c1 != c2:
                        diff_count += 1
                
                if diff_count == 1:
                    q.append([words[i], step + 1])
                    visited[i] = True
    
    return 0