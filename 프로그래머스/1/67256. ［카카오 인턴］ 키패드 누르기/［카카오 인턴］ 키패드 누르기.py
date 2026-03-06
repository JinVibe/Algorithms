def dist(pos, number):
    if number == 2:
        num_pos = [0, 1]
    elif number == 5:
        num_pos = [1, 1]
    elif number == 8:
        num_pos = [2, 1]
    else:
        num_pos = [3, 1]
        
    return [abs(pos[0] - num_pos[0]) + abs(pos[1] - num_pos[1])], num_pos

def solution(numbers, hand):
    answer = ''
    lp = [3, 0] # 왼손 위치
    rp = [3, 2] # 오른손 위치
    for n in numbers:
        if n in [2, 5, 8, 0]:
            ldist, newp = dist(lp, n)
            rdist, newp = dist(rp, n)
            if ldist < rdist:
                answer += 'L'
                lp = newp
            elif ldist > rdist:
                answer += 'R'
                rp = newp
            else:
                if hand == "left":
                    answer += 'L'
                    lp = newp
                else:
                    answer += 'R'
                    rp = newp
        elif n in [1, 4, 7]:
            answer += 'L'
            if n == 1:
                lp = [0, 0]
            elif n == 4:
                lp = [1, 0]
            else:
                lp = [2, 0]
        else:
            answer += 'R'
            if n == 3:
                rp = [0, 2]
            elif n == 6:
                rp = [1, 2]
            else:
                rp = [2, 2]
        
    return answer