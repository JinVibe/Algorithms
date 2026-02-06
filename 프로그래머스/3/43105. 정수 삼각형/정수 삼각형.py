def solution(triangle):
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            if i == 0:
                pass
            elif j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i])-1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] = max(triangle[i - 1][j - 1] + triangle[i][j],
                                    triangle[i - 1][j] + triangle[i][j])
                
            
    return max(triangle[len(triangle) - 1])

# 7 
# 10 15
# 18 16 15
# 20 25 20 19
# 24 30 27 26 24 -> 30